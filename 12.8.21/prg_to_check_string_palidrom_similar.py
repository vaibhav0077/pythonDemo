
str1 = str(input("Enter a word : "))
lengthOfstring = len(str1)

print("length is : ", lengthOfstring )


#Checking Symmetric
if(lengthOfstring%2 == 0):
    j = 0       
    while str1[j] == str1[int(lengthOfstring/2) + j] and j < int(lengthOfstring/2)-1:
        
        j+=1
        # print(j)

    if j+1 == (lengthOfstring/2):
        print(str1 + " is Symmetric")
    else : 
        print(str1 + " is not Symmetric")

else :
    print(str1 + " is not Symmetric")

#checking Palidrome
i = 0
while str1[i] == str1[int(lengthOfstring-i-1)] and i < int(lengthOfstring/2):
        i+=1
# print(i)
if i == int(lengthOfstring/2) or i == int( (lengthOfstring+1)/2 ):
        print(str1 + " is Palidrome")
else: 
        print(str1 + " is not Palidrome")

        