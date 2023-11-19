import yfinance as yf 
import pandas as pd
import datetime as dt
import pandas_datareader as pdr
import pandas_datareader.data as pdrd
import threading
import pymysql
import sqlalchemy
engine = sqlalchemy.create_engine('mysql+pymysql://root:Shrikanth_1@127.0.0.1:3306/stocksdb')


# df = yf.download('AMZN', start='2022-01-01', end='2022-12-30')
# df.to_csv('AMZN.csv')

stock_list = {'COST', 'INTU'}

for stock in stock_list:
    try:
    
        # data= pdrd.get_data_yahoo(f'{stock}', start, end, )
        data = yf.download(tickers=f'{stock}', period="1d", interval="1m")
        data.to_csv(f'Data/{stock}.csv')
    except Exception as e:
        print(f'{stock} ==> {e}')


def getStockData():

    DE = pd.read_csv("Data/DE.csv")
    VRTX = pd.read_csv("Data/VRTX.csv")

    engine = sqlalchemy.create_engine('mysql+pymysql://root:Shrikanth_1@127.0.0.1:3306/stocksdb')
    data.to_sql(name='stock_table', con=engine, index=False, if_exists = 'append')
    print("Entry Done For")