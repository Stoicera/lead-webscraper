# Lead-Webscraper

A Python web crawler that finds leads in your region. Currently specifically adapted to Austria (in code). The project is implemented using both Flask and FastAPI.

## Overview

The Lead-Webscraper is a tool that has been developed to find business contacts and potential clients in Austria. At the moment, its functionality is limited to the Austrian market, but future updates will provide the ability to apply the tool in other countries and regions.

## Features

- **Targeted Lead Search**: The web scraper uses targeted search algorithms to extract relevant information about companies and potential clients in Austria.

- **Contact Information Extraction**: The tool scours websites, online directories, and other sources to find crucial contact information such as email addresses, phone numbers, and location information.

- **Customizable Filters**: The Lead-Webscraper allows users to customize their search criteria, filtering leads by industry, location, or other parameters.

- **Export Results**: Found leads can be exported in various formats to enable seamless integration into CRM systems or other tools.

## Web Server with Flask and FastAPI

The Lead-Webscraper initiates a web server, implemented using both Flask and FastAPI. Here, the found data can be viewed and fetched under the endpoint `/data`. This allows users to access the captured leads in a convenient manner.

## Usage

Currently, the application is restricted to the Austrian market as certain parameters and search algorithms are specifically tailored for this region. Users seeking leads in Austria can deploy the tool straight away.

**Note**: For users outside Austria, a customized version of the web scraper is planned to expand functionality to other countries. We're working on providing an updated version in the near future.

## Updates and Contribution

We believe in continuous improvement and thank the open-source community for their support. We warmly welcome contributions and suggestions from developers and users.

## License

This project is licensed under the [MIT License](LICENSE). You may use, modify, and distribute the code as long as you adhere to the terms of the license.

## Disclaimer

The Lead-Webscraper searches for publicly available information on the internet to find leads. The use of this tool is at the user's own responsibility. We do not assume liability for the use of the found information or for any violations of the data protection regulations or terms of use of the websites searched.

## Contact

For any questions, suggestions, or problems, you can contact us by email at: [artaeon@developerr.me](mailto:artaeon@developerr.me).

---
Please note that this README file is for the current version of the Lead-Webscraper. Future updates will contain more information as new features and customizations are introduced. We look forward to continually improving this tool and making it accessible to users in other regions. Thank you for your interest and support!

**Installation Guide**: The installation guide is provided in the `dev` branch of this repository. Please check out the branch for detailed instructions. The project is available in two versions: one using Flask and the other using FastAPI.