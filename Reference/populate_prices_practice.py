import sqlite3, config
from polygon import RESTClient

client= RESTClient(config.API_KEY)

connection = sqlite3.connect(config.DB_FILE)
connection.row_factory=sqlite3.Row
cursor = connection.cursor()
cursor.execute("""SELECT id, symbol, name FROM stock""")
rows = cursor.fetchall()

# for row in rows:
#     barsets = client.get_aggs(row, 1, "minute", '2022-05-20', '2022-05-25', None, None, None,)
#     print (barsets)

#     for bar in barsets:
#             cursor.execute("""
#                   INSERT INTO stock_price (stock_id, date, open, high, low, close, volume) 
#                   VALUES(?,?,?,?,?,?,?)""", (stock_id, bar.timestamp, bar.open, bar.high, bar.low, bar.close, bar.volume))


symbols = [row['symbol'] for row in rows] # row comprehension
#print(symbols)
stock_dict = {}
for row in rows:
    symbol = row['symbol']
    symbols.append(symbol)
    stock_dict[symbol]= row['id']

# client= RESTClient(config.API_KEY)

# chunk_size = 2
# for i in range(0,len(symbols), chunk_size):
#     symbol_chunk=symbols[i:i+chunk_size]
#     barsets = client.get_aggs('symbol_chunk', 1, "minute", '2022-05-20', '2022-05-25', None, None, None,)

#     for symbol in barsets:
#         print(f"processing symbol {symbol}")
#         for bar in barsets[symbol]:
#             stock_id= stock_dict[symbol]
#             cursor.execute("""
#                 INSERT INTO stock_price (stock_id, date, open, high, low, close, volume) 
#                 VALUES(?,?,?,?,?,?,?)""", (stock_id, bar.timestamp, bar.open, bar.high, bar.low, bar.close, bar.volume))

# connection.commit()

