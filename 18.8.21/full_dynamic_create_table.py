import mysql.connector

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
                ads += ("`"+colName[y]+"`" + " " + colData[y] + ",")
                y+=1
    ads+=("`"+colName[y]+"`" + " " + colData[y])

    print("\n\nads : ", ads)
    print("line 24 : create table if not exists "+tbName+"("+ads+")")
    mycur.execute("create table if not exists "+tbName+"("+ads+")")

    



# starting

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

print("Table Created")

mycur.close()
mydb.close()

print("Program Terminate")