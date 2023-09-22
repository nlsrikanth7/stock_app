import sqlite3, config

connection = sqlite3.connect(config.DB_FILE)
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

# cursor.execute("""SELECT id, symbol, name FROM stock""")
# rows=cursor.fetchall()
# symbols = [row['symbol'] for row in rows] # scheduling a cron job - scheduler

cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES ('ADBE', 'Adobe Inc.', 'NASDAQ')")
cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES ('TSLA', 'Tesla Inc.', 'NASDAQ')")
cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES ('AMZN', 'Amazon.com', 'NASDAQ')")
cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES ('DE', 'Deere & Co.', 'NASDAQ')")
cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES ('AAPL', 'Apple Inc.', 'NASDAQ')")
cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES ('GOOG', 'Alphabet Inc.', 'NASDAQ')")
cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES ('RIVN', 'Rivian Automotive Inc.', 'NASDAQ')")
cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES ('LCID', 'Lucid Inc.', 'NASDAQ')")
cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES ('META', 'Meta Platforms Inc', 'NASDAQ')")
cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES ('MSFT', 'Microsoft Corp', 'NASDAQ')")
cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES ('NFLX', 'Netflix', 'NASDAQ')")
cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES ('S&P 500', 'S&P 500 INDEXSP.INX', 'NASDAQ')")

connection.commit()
