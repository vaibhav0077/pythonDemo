def generator():
    n=1
    while n<10:
        yield n*n
        n+=1    


values = generator()
print("Values :", values)

for i in values:
    print(i)


list = [1,2,3,4,5,6,7]  
  
# List Comprehension  
z = [x**3 for x in list]  
  
# Generator expression  
a = ("AAA : ",str(x**3 for x in list)  )
  
print(a)  
print(z)  