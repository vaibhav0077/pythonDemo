from logging import exception
import mysql.connector  
 

def establishConnection():
     return mysql.connector.connect(host = "localhost", user = "admin",passwd = "admin123",database = "Hospital") 

def creatingTable(self):
    print("Running CreatingTAble")
    try:  
        #Creating a table with name Employee having four columns i.e., name, id, salary, and department id  
        dbs = cur.execute("create table if not exists Employee(name varchar(20) not null, id int(20) not null primary key, salary float not null, Dept_id int not null)")
        # print(dbs)
        print("done")
        
    except:  
    
        cur.execute("show tables")
        for x in cur:
            print(x)
        print("rollback")
        myconn.rollback()  

def alteringTable(self):

    # altering th atble
    try:
        cur.execute("alter table Employee add age int(2) not null")
        print("Table Alteration successfully ddone")
    except:
        print("May be Column Already present")  
        pass

def insertingValues(self):
    try:
        sql = "insert into Employee(name, id, salary, age) values (%s, %s, %s, %s)"  
    
        #The row values are provided in the form of tuple   
        val = ("John", 1, 250,33) 
        #inserting the values into the table  
        cur.execute(sql,val)    
        # #commit the transaction   
        # myconn.commit()  
        print("Successfully inserted") 

    except exception as e:
        print("error while inserting")
        print(e)
        pass

def switch_demo(argu):
    switch = {
        1: creatingTable(),
        2: alteringTable(),
        3: insertingValues(),
        # 4: "April",
        # 5: "May",
        # 6: "June",
        # 7: "July",
        # 8: "August",
        # 9: "September",
        # 10: "October",
        # 11: "November",
        # 12: "December"

    }

#creating the cursor object  
myconn = establishConnection()
if(myconn):
    print("Connected Succefully")
else:
    print("Connection lost")


cur = myconn.cursor()  
argu = int(input("Enter an argument :"))

switch_demo(argu)




myconn.close()  
