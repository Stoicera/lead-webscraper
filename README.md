# Python Web Scraper

This repository contains two implementations of a simple Python web scraper. One implementation uses Flask, and the other uses FastAPI. Both implementations collect data from `https://firmen.wko.at/` and provide it through a web API.

## Flask Version

### Prerequisites

To run the Flask version, you need to install the following Python packages:

```bash
pip install flask requests beautifulsoup4
```

### Execution

Navigate to the Flask folder in the command line and start the Flask app with the following command:

```bash
python app.py
```

The API is then accessible at `http://localhost:5000/data`.

**Disclaimer:** For the Flask version, the data retrieval process is configured on the server through the console. The user is prompted to input what they want to search for and how many pages they want to analyze, etc.

## FastAPI Version

### Prerequisites

To run the FastAPI version, you need to install the following Python packages:

```bash
pip install fastapi uvicorn requests beautifulsoup4 pydantic
```

### Execution

Navigate to the FastAPI folder in the command line and start the FastAPI app with the following command:

```bash
python app.py
```

The API is then accessible at `http://localhost:8080/data/{search_term}/{pages}`. Replace `{search_term}` with the search term and `{pages}` with the number of pages to analyze.