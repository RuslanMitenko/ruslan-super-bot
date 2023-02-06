#
# import requests
#
# from config_data.config import RAPID_API_KEY
#
# import json
#
#
# url = "https://real-time-finance-data.p.rapidapi.com/search"
# querystring = {"query": 'Microsoft'}
# headers = {
#     "X-RapidAPI-Key": RAPID_API_KEY,
#     "X-RapidAPI-Host": 'real-time-finance-data.p.rapidapi.com'
# }
#
# response = requests.request("GET", url, headers=headers, params=querystring, timeout=3)
#
# print(response.text)
#
# js = json.loads(response.text)
#
# name = js['data']['stock'][0].get('name')
# price = js['data']['stock'][0].get('price')
#
# print(name)
# print(price)

from database import actions
from database.models import db, History

# db.create_tables([History])

db_write = actions.ActInterface.create()

data = [{"message": 'что-то'}]
db_write(db, History, data)

db_read = actions.ActInterface.retrieve()

retrieve = (db, History, History.id, History.create_at, History.message)
print(retrieve)
for elem in retrieve:
    # text = text + f'elem.id elem.message \n'
    print(History.id, History.create_at, History.message)
