import requests
import json
import time

allowed_stores = ("1", "7", "8", "11", "25")

def get_dict_response(url):
    payload = {}
    files = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload, files = files)
    response_utf8 = response.text.encode('utf8')
    res = json.loads(response_utf8)

    return res

def get_free_games():
    store_url = "https://www.cheapshark.com/api/1.0/stores"
    stores = get_dict_response(store_url)

    res = [{store['storeID'] : store['storeName']} for store in stores]
    store_dict = {}
    for entry in res:
        store_dict.update(entry)

    game_url = "https://www.cheapshark.com/api/1.0/deals?upperPrice=0"
    games = get_dict_response(game_url)
    res = [(game['title'], store_dict[game['storeID']]) 
            for game in games 
            if (game['storeID'] in allowed_stores)]

    return res
