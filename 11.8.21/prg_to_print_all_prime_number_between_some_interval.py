

def printingPrimeNum(startNum, endNum):
    
    temp = 0
    if (startNum <= 1 or startNum > 0 )and endNum>2:
        print("2")
    if startNum ==2  or endNum==2:
        print("2")
        
    elif startNum>=endNum :
        print("Invalid input")
    
    else :
        for i in range(startNum, endNum+1):
            
            for j in range (2, i):
                if i%j == 0:
                    break
                elif j==(i-1) :
                    print(i)
                    break

    





startNum = int(input("Enter the Startin Number : "))
endNum = int(input("Enter the ending number : "))


printingPrimeNum(startNum, endNum)