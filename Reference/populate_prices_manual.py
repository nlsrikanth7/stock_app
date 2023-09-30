import sqlite3, config
from polygon import RESTClient
import datetime as dt
import pandas as pd
#import plotly.graph_objects as go
#from plotly.offline import plot


client= RESTClient(config.API_KEY)

connection = sqlite3.connect(config.DB_FILE)
connection.row_factory=sqlite3.Row
cursor = connection.cursor()

# insert to sql db using pandas df and row by row. Also map foreign key manually.
stockticker = 'AMZN'
barsets = client.get_aggs(stockticker, 1, "day", '2022-01-01', '2022-12-31', None, None,)
df =  pd.DataFrame(barsets)
df['date'] = pd.to_datetime(df['timestamp'], unit='ms') # convert timestamp from millisec to date time format using pandas df
for bar in df.itertuples():
    cursor.execute(f"""INSERT INTO stock_price(stock_id, open, high, low, close, volume, vwap, transactions, otc, timestamp, date)
    VALUES(6, {bar[1]}, {bar[2]}, {bar[3]}, {bar[4]}, {bar[5]}, {bar[6]}, {bar[8]}, '{bar[9]}', {bar[7]}, '{bar[10]}')""")
print("Data processed for", stockticker)


# stockticker = 'RIVN'
# barsets = client.get_aggs(stockticker, 1, "day", '2022-01-01', '2022-12-31', None, None,)
# df =  pd.DataFrame(barsets)
# df['date'] = pd.to_datetime(df['timestamp'], unit='ms') # convert timestamp from millisec to date time format using pandas df
# for bar in df.itertuples():
#     cursor.execute(f"""INSERT INTO stock_price(stock_id, open, high, low, close, volume, vwap, transactions, otc, timestamp, date)
#     VALUES(7, {bar[1]}, {bar[2]}, {bar[3]}, {bar[4]}, {bar[5]}, {bar[6]}, {bar[8]}, '{bar[9]}', {bar[7]}, '{bar[10]}')""")
# print("Data processed for", stockticker)


# stockticker = 'LCID'
# barsets = client.get_aggs(stockticker, 1, "day", '2022-01-01', '2022-12-31', None, None,)
# df =  pd.DataFrame(barsets)
# df['date'] = pd.to_datetime(df['timestamp'], unit='ms') # convert timestamp from millisec to date time format using pandas df
# for bar in df.itertuples():
#     cursor.execute(f"""INSERT INTO stock_price(stock_id, open, high, low, close, volume, vwap, transactions, otc, timestamp, date)
#     VALUES(8, {bar[1]}, {bar[2]}, {bar[3]}, {bar[4]}, {bar[5]}, {bar[6]}, {bar[8]}, '{bar[9]}', {bar[7]}, '{bar[10]}')""")
# print("Data processed for", stockticker)


# stockticker = 'META'
# barsets = client.get_aggs(stockticker, 1, "day", '2022-01-01', '2022-12-31', None, None,)
# df =  pd.DataFrame(barsets)
# df['date'] = pd.to_datetime(df['timestamp'], unit='ms') # convert timestamp from millisec to date time format using pandas df
# for bar in df.itertuples():
#     cursor.execute(f"""INSERT INTO stock_price(stock_id, open, high, low, close, volume, vwap, transactions, otc, timestamp, date)
#     VALUES(9, {bar[1]}, {bar[2]}, {bar[3]}, {bar[4]}, {bar[5]}, {bar[6]}, {bar[8]}, '{bar[9]}', {bar[7]}, '{bar[10]}')""")
# print("Data processed for", stockticker)

# stockticker = 'MSFT'
# barsets = client.get_aggs(stockticker, 1, "day", '2022-01-01', '2022-12-31', None, None,)
# df =  pd.DataFrame(barsets)
# df['date'] = pd.to_datetime(df['timestamp'], unit='ms') # convert timestamp from millisec to date time format using pandas df
# for bar in df.itertuples():
#     cursor.execute(f"""INSERT INTO stock_price(stock_id, open, high, low, close, volume, vwap, transactions, otc, timestamp, date)
#     VALUES(10, {bar[1]}, {bar[2]}, {bar[3]}, {bar[4]}, {bar[5]}, {bar[6]}, {bar[8]}, '{bar[9]}', {bar[7]}, '{bar[10]}')""")
# print("Data processed for", stockticker)

# stockticker = 'NFLX'
# barsets = client.get_aggs(stockticker, 1, "day", '2022-01-01', '2022-12-31', None, None,)
# df =  pd.DataFrame(barsets)
# df['date'] = pd.to_datetime(df['timestamp'], unit='ms') # convert timestamp from millisec to date time format using pandas df
# for bar in df.itertuples():
#     cursor.execute(f"""INSERT INTO stock_price(stock_id, open, high, low, close, volume, vwap, transactions, otc, timestamp, date)
#     VALUES(11, {bar[1]}, {bar[2]}, {bar[3]}, {bar[4]}, {bar[5]}, {bar[6]}, {bar[8]}, '{bar[9]}', {bar[7]}, '{bar[10]}')""")
# print("Data processed for", stockticker)

# stockticker = 'S&P 500'
# barsets = client.get_aggs(stockticker, 1, "day", '2022-01-01', '2022-12-31', None, None,)
# df =  pd.DataFrame(barsets)
# df['date'] = pd.to_datetime(df['timestamp'], unit='ms') # convert timestamp from millisec to date time format using pandas df
# for bar in df.itertuples():
#     cursor.execute(f"""INSERT INTO stock_price(stock_id, open, high, low, close, volume, vwap, transactions, otc, timestamp, date)
#     VALUES(12, {bar[1]}, {bar[2]}, {bar[3]}, {bar[4]}, {bar[5]}, {bar[6]}, {bar[8]}, '{bar[9]}', {bar[7]}, '{bar[10]}')""")
# print("Data processed for", stockticker)



# print(df)
# insert to sql db using pandas df
# df.to_sql(name='stock_price',con=connection,if_exists= 'append', index =  False)

# dailystockdata['Date'] = dailystockdata['timestamp'].apply(lambda x: pd.to_datetime(x*1000000))
# dailystockdata = dailystockdata.set_index('Date')

# insert to sql using each row at a time
# for bar in barsets:
#     cursor.execute("""
#                   INSERT INTO stock_price (stock_id, date, open, high, low, close, volume) 
#                   VALUES(?,?,?,?,?,?,?)""", (1, bar.timestamp, bar.open , bar.high, bar.low, bar.close, bar.volume))
# print("Data processed for ADBE")

#barsets = client.get_aggs("TSLA", 1, "day", '2022-01-01', '2022-12-31', None, None, None,)
# for row in df:
#     print(row[2])
    # cursor.execute(f"""INSERT INTO stock_price (stock_id, open, high, low, close, volume, date) 
    # VALUES(2,{row[1]},{row[2]},{row[3]},{row[4]},{row[5]}, {row[7]},)""")
    # cursor.execute("""
    #               INSERT INTO stock_price (stock_id, date, open, high, low, close, volume) 
    #               VALUES(?,?,?,?,?,?,?)""", (2, bar.date, bar.open, bar.high, bar.low, bar.close, bar.volume))
# print("Data processed for TSLA")

# barsets = client.get_aggs("AMZN", 1, "day", '2022-01-01', '2022-12-31', None, None, None,)
# for bar in barsets:
#     cursor.execute("""
#                   INSERT INTO stock_price (stock_id, date, open, high, low, close, volume) 
#                   VALUES(?,?,?,?,?,?,?)""", (3, bar.timestamp, bar.open, bar.high, bar.low, bar.close, bar.volume))
# print("Data processed for AMZN")

# barsets = client.get_aggs("DE", 1, "day", '2022-01-01', '2022-12-31', None, None, None,)
# for bar in barsets:
#     cursor.execute("""
#                   INSERT INTO stock_price (stock_id, date, open, high, low, close, volume) 
#                   VALUES(?,?,?,?,?,?,?)""", (4, bar.timestamp, bar.open, bar.high, bar.low, bar.close, bar.volume))
# print("Data processed for DE")

# barsets = client.get_aggs("AAPL", 1, "day", '2022-01-01', '2022-12-31', None, None, None,)
# for bar in barsets:
#     cursor.execute("""
#                   INSERT INTO stock_price (stock_id, date, open, high, low, close, volume) 
#                   VALUES(?,?,?,?,?,?,?)""", (5, bar.timestamp, bar.open, bar.high, bar.low, bar.close, bar.volume))
# print("Data processed for AAPL")

# barsets = client.get_aggs("GOOG", 1, "day", '2022-01-01', '2022-12-31', None, None, None,)
# for bar in barsets:
#     cursor.execute("""
#                   INSERT INTO stock_price (stock_id, date, open, high, low, close, volume) 
#                   VALUES(?,?,?,?,?,?,?)""", (6, bar.timestamp, bar.open, bar.high, bar.low, bar.close, bar.volume))
# print("Data processed for GOOG")

# barsets = client.get_aggs("RIVN", 1, "day", '2022-01-01', '2022-12-31', None, None, None,)
# for bar in barsets:
#     cursor.execute("""
#                   INSERT INTO stock_price (stock_id, date, open, high, low, close, volume) 
#                   VALUES(?,?,?,?,?,?,?)""", (7, bar.timestamp, bar.open, bar.high, bar.low, bar.close, bar.volume))
# print("Data processed for RIVN")

# barsets = client.get_aggs("LCID", 1, "day", '2022-01-01', '2022-12-31', None, None, None,)
# for bar in barsets:
#     cursor.execute("""
#                   INSERT INTO stock_price (stock_id, date, open, high, low, close, volume) 
#                   VALUES(?,?,?,?,?,?,?)""", (8, bar.timestamp, bar.open, bar.high, bar.low, bar.close, bar.volume))
# print("Data processed for LCID")


# barsets = client.get_aggs("META", 1, "day", '2022-01-01', '2022-12-31', None, None, None,)
# for bar in barsets:
#     cursor.execute("""
#                   INSERT INTO stock_price (stock_id, date, open, high, low, close, volume) 
#                   VALUES(?,?,?,?,?,?,?)""", (9, bar.timestamp, bar.open, bar.high, bar.low, bar.close, bar.volume))
# print("Data processed for META")

# barsets = client.get_aggs("MSFT", 1, "day", '2022-01-01', '2022-12-31', None, None, None,)
# for bar in barsets:
#     cursor.execute("""
#                   INSERT INTO stock_price (stock_id, date, open, high, low, close, volume) 
#                   VALUES(?,?,?,?,?,?,?)""", (10, bar.timestamp, bar.open, bar.high, bar.low, bar.close, bar.volume))
# print("Data processed for MSFT")

# barsets = client.get_aggs("NFLX", 1, "day", '2022-01-01', '2022-12-31', None, None, None,)
# for bar in barsets:
#     cursor.execute("""
#                   INSERT INTO stock_price (stock_id, date, open, high, low, close, volume) 
#                   VALUES(?,?,?,?,?,?,?)""", (11, bar.timestamp, bar.open, bar.high, bar.low, bar.close, bar.volume))
# print("Data processed for NFLX")

# barsets = client.get_aggs("^GSPC", 1, "day", '2022-01-01', '2022-12-31', None, None, None,)
# for bar in barsets:
#     cursor.execute("""
#                   INSERT INTO stock_price (stock_id, date, open, high, low, close, volume) 
#                   VALUES(?,?,?,?,?,?,?)""", (12, bar.timestamp, bar.open, bar.high, bar.low, bar.close, bar.volume))
# print("Data processed for S&P 500")

connection.commit()