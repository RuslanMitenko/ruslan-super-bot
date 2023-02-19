from config_data.config import RAPID_API_KEY
import json
import requests


def fin_info(symbol: str, period: str) -> dict:
    url = "https://real-time-finance-data.p.rapidapi.com/company-income-statement"

    querystring = {"symbol": symbol, "period": period}

    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "real-time-finance-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring, timeout=3)
    print(response.text)
    js = json.loads(response.text)

    return js
