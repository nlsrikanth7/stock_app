# import sqlite3, config
import yfinance as yf
from getpass import getpass
import mysql.connector
from mysql.connector import connect, Error, errorcode
import logging
import time

# Set up logger
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Also log to a file
# file_handler = logging.FileHandler("cpy-errors.log")
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler) 


mydb= mysql.connector.connect(
        host = "localhost",
        user ="root",
        passwd ="Shrikanth_1",
        database = "stocks_db")

# print(mydb)
  
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE stocks_db")
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)

# mycursor.execute("CREATE TABLE stocklist (stockid INTEGER(10), Stocksymbol VARCHAR(255), Stockname VARCHAR(255))")
# mycursor.execute("CREATE TABLE stockprices (stockid int(10),Datetime date,Open int(10),High int(10),Close int(10),ADJCLOSE int(10),VOLULME int(10))")
# mycursor.execute("SHOW TABLES")
# for tables in mycursor:
#     print(tables)

getstocklist = "INSERT INTO stocklist (stockid, Stocksymbol, Stockname) VALUES (%s, %s, %s)"

# stock1 = (1, "AMZN", 'Amazon')
# mycursor.execute(getstocklist, stock1)

# stocklistdata = [
#     ((1, "AMZN", "Amazon")),
#     ((2, "TSLA", "Tesla")),
#     ((3, "AAPL", "AAPL")),
#     ((4,"GOOG", "Google")),
#     ((5, "NFLX", "Netflix"))
# ]
# mycursor.executemany(getstocklist, stocklistdata)

# sql = "SELECT * FROM stocklist WHERE stockid = 4"
# sql = "SELECT * FROM stocklist WHERE stocksymbol LIKE '%A%'"
# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for result in myresult:
#     print(result)

# sql = "UPDATE stocklist SET Stockname = 'GOOGLE' WHERE Stocksymbol = 'GOOG' "

# mycursor.execute(sql)
# mycursor.execute("SELECT * FROM stocklist LIMIT 3 OFFSET 2")
# sql = "SELECT * FROM stocklist ORDER BY Stocksymbol DESC"
sql ="DELETE FROM stocklist WHERE Stocksymbol = 'AMZN'"
# sql = "DROP TABLE IF EXISTS stocklist"
mycursor.execute(sql)
# myresult = mycursor.fetchall()

# for result in myresult:
    # print(result)

mydb.commit()











# Reference below and trials

# try:
#   mydb = mysql.connector.connect(host="localhost", user='root',passwd = "Shrikanth_1", database = "stocksdb")
#   mycursor = mydb.cursor()
# #   mycursor.execute("CREATE DATABASE stocksdb")
# except mysql.connector.Error as err:
#   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#     print("Something is wrong with your user name or password")
#   elif err.errno == errorcode.ER_BAD_DB_ERROR:
#     print("Database does not exist")
#   else:
#     print(err)
# else:
#   mydb.close()


# #Creat a table 
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE stocks(id INTEGER, symbol VARCHAR, name VARCHAR)")


# def create_database(cursor):
#     try:
#         cursor.execute(
#             "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
#     except mysql.connector.Error as err:
#         print("Failed creating database: {}".format(err))
#         exit(1)



# DB_NAME = 'stocksdb'

# TABLES = {}
# TABLES['stocks'] = (
#     "CREATE TABLE `stocks` ("
#     "  `symbol` varchar(14) NOT NULL,"
#     "  `name` varchar(16) NOT NULL,"
#     "  PRIMARY KEY (`stock_id`)"
#     "))

#Create a database called stocks_db

#  CREATE TABLE IF NOT EXISTS stock_price(
#    id INTEGER PRIMARY KEY,
#    stock_id INTEGER,
#    timestamp NOT NULL,
#    open NOT NULL,
#    high NOT NULL,
#    low NOT NULL,
#    close NOT NULL,
#    volume NOT NULL,
#    vwap NOT NULL,
#    transactions NOT NULL,
#    date NOT NULL,
#    otc STRING,
#    FOREIGN KEY (stock_id) REFERENCES stock(id)


# print(mydb)

# mycursor = mydb.cursor()

#Check all the databases 
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)

# try:
#     with connect(
#         host = "127.0.0.1",
#         user = input("Enter Username: "),
#         password = getpass('Enter password: '),
#     ) as connection:
#         # print (connection)
# except Error as e:
#     print(e)


# connection = sqlite3.connect(config.DB_FILE)

# mycursor.execute("""CREATE TABLE stock (
#      id INTEGER PRIMARY KEY,
#      symbol TEXT NOT NULL UNIQUE,
#      name TEXT NOT NULL,
#      exchange TEXT NOT NULL
#     )
# """)

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS stock_price(
#    id INTEGER PRIMARY KEY,
#    stock_id INTEGER,
#    timestamp NOT NULL,
#    open NOT NULL,
#    high NOT NULL,
#    low NOT NULL,
#    close NOT NULL,
#    volume NOT NULL,
#    vwap NOT NULL,
#    transactions NOT NULL,
#    date NOT NULL,
#    otc STRING,
#    FOREIGN KEY (stock_id) REFERENCES stock(id)
# )
# """)

# connection.commit()

