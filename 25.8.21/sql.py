import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin123"
)

print(mydb)