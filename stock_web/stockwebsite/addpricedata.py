import requests
import yfinance as yf
import pandas as pd
import json
import datetime as dt

def getpricedata(ticker):
    start = dt.datetime(2023,1,1)
    end = dt.datetime.now()
    df = yf.download(ticker, start, end)
    response = requests.get(df)
    return response
                # df = df.to_csv(f'Data/{ticker}.csv')
                # data = pd.read_csv(f'Data/{ticker}.csv')
                # json_records = data.reset_index().to_json(orient='records')
                # arr = []
                # arr = json.loads(json_records)
                # context = {'d': arr}
                # return render(request, 'index.html', context)

    
   