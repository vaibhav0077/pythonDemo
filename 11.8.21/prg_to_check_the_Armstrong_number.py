

num = int(input("Enter a Number : "))
x = int(num)
zz = int(num)
q = 0

while zz > 0:
    zz = int(zz/10)
    q+=1

print("Size of Number is ", q)
sum = 0
while num>0:
    a = int(num%10)
    sum += pow(a,q)
    num = int(num/10)
print("Entered Number is : ", x)
print("Processed Number is : ", sum)


if(x == sum):
    print("Number is armstrong")

else:
    print("Number is Not armstrong")