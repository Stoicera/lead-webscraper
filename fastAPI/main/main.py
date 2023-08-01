from fastapi import FastAPI
import threading
import requests
from bs4 import BeautifulSoup
from typing import List, Union
from pydantic import BaseModel

class Data(BaseModel):
    Website: str
    Name: str
    Adresse: str
    Kontaktart: str
    Kontaktdaten: str
    Email: str

app = FastAPI()
scraped_data = []

base_url = 'https://firmen.wko.at/'
page_prefix = '?page='

def extract_data_from_url(url: str, data: List[Union[Data, str]]):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')

    names = soup.find_all('h3', itemprop='name')
    location_data = soup.find_all('div', class_='col-md-4 col1')
    contact_data = soup.find_all('div', class_='col-md-4 col2')

    if names and location_data and contact_data:
        for i in range(min(len(names), len(location_data), len(contact_data))):
            name = names[i].text
            location = location_data[i].find('div', itemprop='streetAddress').get_text(strip=True)
            contact_type = contact_data[i].find('span', class_='type')
            contact_email = contact_data[i].find('div', class_='icon-email vcard__info')

            if contact_type:
                contact_type = contact_type.get_text(strip=True)
                contact_value = contact_data[i].find('a').get('href')
            else:
                contact_type = 'Kein Wert'
                contact_value = 'Kein Wert'

            if contact_email is None:
                contact_email = 'Kein Wert'
            else:
                contact_email = contact_email.get_text(strip=True)

            contact_website_type = contact_data[i].find('div', class_='icon-web vcard__info')

            if contact_website_type is None:
                data.append(Data(
                    Website = 'Keine Website',
                    Name = name,
                    Adresse = location,
                    Kontaktart = contact_type,
                    Kontaktdaten = contact_value,
                    Email = contact_email
                ))
            else:
                data.append(Data(
                    Website = 'Website',
                    Name = name,
                    Adresse = location,
                    Kontaktart = contact_type,
                    Kontaktdaten = contact_value,
                    Email = contact_email
                ))

    else:
        data.append('Keine Unternehmen gefunden oder die Unternehmen besitzen bereits eine Website')

def bulkrequest(search_term: str, pages: int):
    if search_term:
        if pages:
            threads = []

            def extract_data_threaded(url, data):
                extract_data_from_url(url, data)

            for i in range(pages):
                thread = threading.Thread(target=extract_data_threaded,
                                          args=(base_url + search_term + page_prefix + str(i + 1), scraped_data))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

        else:
            print('Ungültige Eingabe für die Anzahl der Seiten.')
    else:
        print('Ungültiger Suchbegriff.')

@app.get("/data/{search_term}/{pages}")
async def get_data(search_term: str, pages: int):
    scraped_data.clear()
    bulkrequest(search_term, pages)
    return scraped_data

if __name__ == "__main__":
    bulkrequest()
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)
