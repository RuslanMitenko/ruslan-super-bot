from config_data.config import RAPID_API_KEY
import json
import requests


def search_ticker(query: str) -> dict:
    url = "https://real-time-finance-data.p.rapidapi.com/search"
    querystring = {"query": query}
    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": 'real-time-finance-data.p.rapidapi.com'
    }

    response = requests.request("GET", url, headers=headers, params=querystring, timeout=3)
    js = json.loads(response.text)

    return js
