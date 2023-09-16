import requests

key = "8c0b623ea5msh98642c408604475p1c7ea9jsn360b852a561d"

#get python dictionary data
def get_esg_info(ticker):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-esg-scores"

    querystring = {"symbol":ticker,"region":"US","lang":"en-US"}

    headers = {
        "X-RapidAPI-Key": "8c0b623ea5msh98642c408604475p1c7ea9jsn360b852a561d",
        "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    data = requests.get(url, headers=headers, params=querystring).json()
    newData = data["quoteSummary"]["result"][0]["esgScores"]

    keys = ["environmentScore", "governanceScore", "socialScore"]
    
    return(getValues(newData, keys))




