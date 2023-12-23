from urllib.request import urlopen
import requests


API_KEY = '6ea77b917e9ac025a7fab4f39229fdf1'
base_url =  'https://financialmodelingprep.com/api'


def getfinancedata(symbol):
    data_type = 'income-statement'
    url = f"{base_url}/v3/{data_type}/{symbol}?period=annual&apikey={API_KEY}"
    response = requests.get(url)
    return response.json()
    

                