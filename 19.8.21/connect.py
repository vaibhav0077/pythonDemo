import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",passwd="admin123")

if db:
    print("Connected Successfully to ", db)
else:
    print("Connection Failed")
