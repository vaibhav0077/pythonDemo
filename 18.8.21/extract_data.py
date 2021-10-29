from os import replace
import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "admin123",database = "training")  
  
#creating the cursor object  
cur = myconn.cursor()  
  
try:  
    #Reading the Employee data      
    cur.execute("select ProjectId from Project")  
    
  
    #fetching the rows from the cursor object  
    result = cur.fetchall() 
    le = len(result)
    i = 0
    print(le)
    for x in result:
        result[i] = replace(",","")
        i+=1

    #printing the result 
    print("result",result) 
    print(type(result))
      
    # for x in result:  
    #     print(x);  
except:  
    myconn.rollback()  
  
myconn.close()  