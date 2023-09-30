import sqlite3, config
from polygon import RESTClient
import datetime as dt
import pandas as pd

client= RESTClient(config.API_KEY)

connection = sqlite3.connect(config.DB_FILE)
connection.row_factory=sqlite3.Row
cursor = connection.cursor()
cursor.execute("""SELECT id, symbol, name FROM stock""")
rows = cursor.fetchall()
symbols = [row['symbol'] for row in rows] # row comprehension
# print(symbols)
stock_dict = {}
for item in rows:
    symbol = item['symbol']
    # symbols.append(symbol)
    stock_dict[symbol]= item['id']
    # print(stock_dict)

print(symbols)
print(stock_dict)
for stockticker in symbols:
    print("processing symbol -", stockticker)
    barsets = client.get_aggs(stockticker, 1, "day", '2022-09-20', '2023-09-22', None, None, None,)
    df =  pd.DataFrame(barsets)
    df['date'] = pd.to_datetime(df['timestamp'], unit='ms') # convert timestamp from millisec to date time format using pandas df
    # print(df)
    for bar in df.itertuples():
        stock_id= stock_dict[symbol]
        print(stock_id)
        # cursor.execute(f"""INSERT INTO stock_price(stock_id, open, high, low, close, volume, vwap, transactions, otc, timestamp, date)
        # VALUES(11, {bar[1]}, {bar[2]}, {bar[3]}, {bar[4]}, {bar[5]}, {bar[6]}, {bar[8]}, '{bar[9]}', {bar[7]}, '{bar[10]}')""")
    print("Data processed for", stockticker)

#     for bar in barsets:
#         print(bar)
#         stock_id= stock_dict[symbol]
#         # cursor.execute("""
#         #           INSERT INTO stock_price (stock_id, date, open, high, low, close, volume) 
#         #           VALUES(?,?,?,?,?,?,?)""", (stock_id, bar.timestamp, bar.open, bar.high, bar.low, bar.close, bar.volume))
# connection.commit()

