import mysql.connector
from mysql.connector import connect, Error
import pymysql

pymysql.install_as_MySQLdb()

# Connect to mysql (1st method)
dataBase = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    passwd = 'Shrikanth_1'
)
print(dataBase)


# prepare a cursor object 
cursorObject = dataBase.cursor()

# # Create a database 
cursorObject.execute("CREATE DATABASE IF NOT EXISTS StockWebApplication")
print('All done! ')
