
def subStringChecking(str1 , subStr):
    lengthOfStr = len(str1)
    lengthOfSubStr = len(subStr)

    if lengthOfSubStr > lengthOfStr:
        print ('Invalid Input')
        return 1
    else:
        i= 0
        j= 0
        x = 0

        # print(lengthOfStr)
        # print(lengthOfSubStr)
        while True:

            if i < lengthOfSubStr and subStr[i] == str1[j] and j < lengthOfStr :
                # print("i:",i)
                # print("j:",j)
                i+=1
                j+=1
                x = j-1
            elif j < (lengthOfStr-1) and i != (lengthOfSubStr):
                # print("jj:",j)
                j+=1
            else:
                break

        
        if i == (lengthOfSubStr):
                print(" \""+ subStr +"\" " + " found in " +" \""+ str1 +"\" " + " AT index of " + str(x) )
        else: 
                print("SubString Does Not Found")        


            


str1 = str(input("Enter a String : "))
subStr = str(input("Enter a word to find in string : "))


subStringChecking(str1, subStr)


