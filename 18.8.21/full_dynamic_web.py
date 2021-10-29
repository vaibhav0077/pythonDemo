from logging import exception
import mysql.connector


# def createDatabse(dbName):
#     str1 = "create databse if not exists " + dbName

#     try:
#         return str1
#     except:
#         print("line 13 something happens ")

#     finally:
#         return basicConnection(dbName)


def basicConnection(dbName):
    try:
        return mysql.connector.connect(host="localhost", user="root", passwd="admin123", database=dbName)
    except:
        return False

def creatingCursor(mydb):
    return mydb.cursor()

def createTable(mycur, tbName, tbCol,colName, colData):
    y = 0
    ads = ""
    while y<tbCol-1:
                ads += (colName[y] + " " + colData[y] + ",")
                y+=1
    ads+=(colName[y] + " " + colData[y])
    print("line 24 : create table if not exists "+tbName+"("+ads+")")
    mycur.execute("create table if not exists "+tbName+"("+ads+")")


def insertValues(sss,colvalues, tbCol,enteringNoOfRows,mycur):
    sql = sss
    qqqq = 0
    print("line 29 ",colValues)
    # length = len(colValues)
    nn = ()
    l1 = []
    while qqqq < enteringNoOfRows:
        z = 0
        # nn = "("

        #     # val = ("John", "aa") 
        #     # #inserting the values into the table  
        #     # cur.execute(sql,val)  
        
        # while z < tbCol-1:
        #     nn+="\"" + colValues[z] +"\", "
        #     z+=1

        # nn+="\"" + colValues[z] +"\",) "

        
        
        str1 = " \"" + str(colValues[z]) + "\""
        l1.append(str1)
        str1  = ""   
        nn = tuple(l1)

        
        print("\n\n\n")
        print("linr 67 Type nn  : ",type(nn))
        print("line 45 nn:",nn)
        print("line 46:",sql) #"insert into Employee(name, id, salary, age) values (%s, %s, %s, %s)"  
        try:
            mycur.execute(sql,nn) #insert into a(a) values (%s)
        except exception as e:
            print(e)
        qqqq+=1

# STARTING 

dbName = str(input("Enter your database name : "))
mydb = basicConnection(dbName)

if(mydb):
    print("Connected Succesfully")
else:
    print("CONNECTION FAILED!!!!")

mycur = creatingCursor(mydb)

if(mycur):
    print("cursor created Succesfully")
else:
    print("cursor  FAILED!!!!")


tbName = str(input("Enter Table name : "))
tbCol = int(input("Enter no. of colums : "))
x = 0
colName = []
colData= []
s,ss ="",""

while x < tbCol:
    s = str(input("Enter " + str((x+1)) + " column name  : "))
    ss = str(input("Enter " + str((x+1)) + " column datatype  : "))
    colName.append(s)
    colData.append(ss)
    s,ss ="",""
    x+=1

createTable(mycur, tbName, tbCol,colName, colData)
#sql quer creater
xx = 0
sss = ""
sss  =  "insert into "+tbName+"("
while xx <tbCol-1:
   sss+=colName[xx] +", "
   xx+=1 

sss += colName[xx]+ ") values ("
xx = 0
while xx <tbCol-1:
   sss+="%s, "
   xx+=1
sss+="%s)" 


#creating user input valuing

enteringNoOfRows = int(input("Enter no of rows : "))
q = 0
qq = 0
colValues = []
while q < enteringNoOfRows:
    q+=1
    qq = 0
    while qq < tbCol:
        colValues.append(str(input("Enter data for column "+ str(qq+1) +"row "+str(q)+ " : ")))
        print("colvalues line no 105: ", colValues)
        qq+=1

insertValues(sss, colValues, tbCol, enteringNoOfRows,mycur)



