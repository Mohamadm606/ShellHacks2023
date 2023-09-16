import requests
import json 

def print_esg_info(ticker):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-esg-scores"

    querystring = {"symbol":ticker,"region":"US","lang":"en-US"}

    headers = {
        "X-RapidAPI-Key": "8c0b623ea5msh98642c408604475p1c7ea9jsn360b852a561d",
        "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(json.dumps(response.json(), sort_keys=True, indent=4))


def get_ticker(str):

    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

    querystring = {"q":str,"region":"US"}

    headers = {
        "X-RapidAPI-Key": "8c0b623ea5msh98642c408604475p1c7ea9jsn360b852a561d",
        "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    
    print(json.dumps(response.json(), sort_keys=True, indent=4))

get_ticker("tesla")
