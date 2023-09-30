import sqlite3, config
from polygon import RESTClient
import datetime as dt
import pandas as pd
import yfinance as yf

client= RESTClient(config.API_KEY)

# connection = sqlite3.connect(config.DB_FILE)
# # connection.row_factory=sqlite3.Row
# cursor = connection.cursor()

# assets = client.get_ticker_types(asset_class='stocks', locale='us')

# stocklist = pd.DataFrame()
counter = 0
Tickers =[]

if counter <= 10:
    for t in client.list_tickers(market='stocks', exchange= 'nasdaq', active= False, limit = 10):
        

         #add to the list
         Tickers.append(t.ticker)
         #increment counter 
         counter+= 1

         print(Tickers)






# cursor.execute("""SELECT id, symbol, name FROM stock""")
# rows=cursor.fetchall()
# symbols = [row['symbol'] for row in rows] # scheduling a cron job - scheduler

# cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES ('ADBE', 'Adobe Inc.', 'NASDAQ')")
# cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES ('TSLA', 'Tesla Inc.', 'NASDAQ')")
# cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES ('AMZN', 'Amazon.com', 'NASDAQ')")
# # cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES ('DE', 'Deere & Co.', 'NASDAQ')")
# cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES ('AAPL', 'Apple Inc.', 'NASDAQ')")
# cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES ('GOOG', 'Alphabet Inc.', 'NASDAQ')")
# # cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES ('RIVN', 'Rivian Automotive Inc.', 'NASDAQ')")
# # cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES ('LCID', 'Lucid Inc.', 'NASDAQ')")
# cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES ('META', 'Meta Platforms Inc', 'NASDAQ')")
# cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES ('MSFT', 'Microsoft Corp', 'NASDAQ')")
# cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES ('NFLX', 'Netflix', 'NASDAQ')")
# # cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES ('S&P 500', 'S&P 500 INDEXSP.INX', 'NASDAQ')")

# connection.commit()



# 1. Get/ingest all the stock from NASDAQ into data base from yahoo finance or Google finance
# 2. Create a SQL Data base 
# 3. Store all the stock symbols and data into the database 
# 4. Create a front UI to visualize the stock data 
# 5. Develop a technical indicator of stocks 
