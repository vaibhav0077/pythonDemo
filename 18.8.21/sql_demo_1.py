
from logging import exception
import mysql.connector
from mysql.connector.cursor import MySQLCursor

mydb = mysql.connector.connect(host="localhost", user="admin", passwd="admin123")

# print(mydb)

if(mydb):
    print("Connected Successfully\n\n")
else:
    print("Connection lost!! \n\n")




mycu = mydb.cursor()

try:
    # mycu.execute("create database Hospital")
    eee = mycu.execute("Show Databases")
    for x in mycu:
        print(x)

    #  tb = mycu.execute("create table employee(name varchar(20) not null,
    #                                       id int(2) not null auto_increment,
    #                                       salary int(5) not null)
    #                                       ")
# db = mycu.execute("create table Employee(name varchar(20) not null, id int(20) not null primary key, salary float not null, Dept_id int not null)")  

    

except exception as e:
    for x in mycu:
        print(x)
    print(" ")




