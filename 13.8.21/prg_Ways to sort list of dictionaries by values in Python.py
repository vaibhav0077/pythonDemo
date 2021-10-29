
from operator import itemgetter 

listInfo  = [] 
info = {}
n = int(input("Number Of Students : "))

for y in range(n):

    id = str(input("Enter Id of Student : "))
    name = str(input("Enter Name Of Student : "))
    std = str(input("Enter Standard of student : "))
    info["Id"] = id
    info["name"] = name
    info["std"] = std
    print("INFO : ", info)
    listInfo.append(info.copy())
    info.clear()
    print("ListInfo : " , listInfo)

print(listInfo)

print(sorted(listInfo , key=itemgetter("std") ))
print(sorted(listInfo , key=itemgetter("name") ))
print(sorted(listInfo , key=itemgetter("Id") ))





    


