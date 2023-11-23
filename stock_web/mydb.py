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
cursorObject.execute("CREATE DATABASE IF NOT EXISTS Economic_Indicies")
print('All done! ')

# Connect to mysql (2nd Method)
# try:
#     pymysql.install_as_MySQLdb()
#     with connect(
#         host = "127.0.0.1",
#         user = 'root',
#         password = 'Shrikanth_1',
#         database = 'Economic_Indicies',
#         # auth_plugin = 'mysql_native_password',
#     ) as dataBase:
#         print (dataBase)
#         cursorObject = dataBase.cursor()
#         cursorObject.execute("CREATE DATABASE IF NOT EXISTS Economic_Indicies")
#         print('All done! ')
# except Error as e:
#     print(e)