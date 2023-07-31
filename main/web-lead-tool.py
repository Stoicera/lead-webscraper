from flask import Flask, jsonify
import threading
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
scraped_data = []

base_url = 'https://firmen.wko.at/'
page_prefix = '?page='


def extract_data_from_url(url, data):
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
                contact_type = 'No Value'
                contact_value = 'No Value'

            if contact_email is None:
                contact_email = 'No Value'
            else:
                contact_email = contact_email.get_text(strip=True)

            contact_website_type = contact_data[i].find('div', class_='icon-web vcard__info')

            if contact_website_type is None:
                data.append({
                    'Website': 'Keine Website',
                    'Name': name,
                    'Adresse': location,
                    'Kontaktart': contact_type,
                    'Kontaktdaten': contact_value,
                    'Email': contact_email
                })
            else:
                data.append({
                    'Website': 'Website',
                    'Name': name,
                    'Adresse': location,
                    'Kontaktart': contact_type,
                    'Kontaktdaten': contact_value,
                    'Email': contact_email
                })

    else:
        data.append('Keine Unternehmen gefunden oder die Unternehmen besitzen bereits eine Website')

def bulkrequest():
    search_term = input('Geben Sie den Suchbegriff ein (z.B. "einzelunternehmen", "gmbh"): ')
    if search_term:
        pages = int(input('Geben Sie die Anzahl der zu analysierenden Seiten ein: '))
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


@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(scraped_data)


if __name__ == '__main__':
    bulkrequest()
    app.run(host='localhost', port=8080)
