


def converTingInString(strArr):
    x = 0
    word = ""
    while x < len(strArr):
        word += strArr[x]
        x+=1
    return word

def countingOccurence(strList):
    q = 0
    w = 0
    l = len(strList)
    print("l : ", l)
    wordsWithFrequency = [[]]*0
    
    while l > (q+w) :
        print("again")
        
        tempStr = strList[q]
        print("l:", l)
        print("q+W : ", q+w)
        print("Q : " ,q)
        print("w : ",w)
        print("temstr: ", tempStr)
        q+= 1
        
        freq = 1
        while l > (q+w):
            print("l:", l)
            print("q+W : ", q+w)
            print("Q : " ,q)
            print("w : ",w)
            print("temstr: ", tempStr)
           
            if tempStr != strList[q+w] and q+w < l:
                w+=1
            else:
                w+=1
                freq+=1
                strList.remove(tempStr)
                l-=1
                print("freq : ", freq)
        
        wordsWithFrequency.append([tempStr ,freq])   
        tempStr = ""
        w = 0    
            

    print(wordsWithFrequency)




str1 = str(input("Enter your String : "))
strList = []
strArr = []
temp =0
length = len(str1)
print("length : ", length)

while True:
    if length <= temp:
        break
    if str1[temp] != " ":
    #    print(str1[temp]) 
       strArr.append(str1[temp])
       temp+=1     
    #    print("strArr:",strArr)
    #    print("Temp : ", temp)
    else :
        temp+=1
        strList.append(converTingInString(strArr))
        # print("strlist : ",strList)
        strArr = []

    if temp == length :
        strList.append(converTingInString(strArr))
        # print("strlist : ",strList)
    

print (strList)
    
countingOccurence(strList)
