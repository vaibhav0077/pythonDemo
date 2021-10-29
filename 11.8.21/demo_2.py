print("\n\n\n\n")
"""
c = 5

def add():
    a = 2
    b = 3
    global c
    c = 7
    print ("c : ", c)
    print("Addition of both is : ", a+b)
    del a
    print (a)

add()
print (c)
print(id(a))  
print(id(b))

"""
"""
print(1, 2, 3, 4, 5, 6)

s =  '''A multiline 
        string''' 
print(s)


str1 = 'hello world' #string str1    
str2 = ' how are you world' #string str2    
print (str1[3:9]) #printing first two character using slice operator    
print (str1[4]) #printing 4th character of the string    
print (str1*10) #printing the string twice    
print (str1 + str2) #printing the concatenation of str1 and str2 

"""



"""
list1  = [1, "hi", "Python", 2]    
#Checking type of given list  
print(type(list1))  
  
#Printing the list1  
print (list1)  
  
# List slicing  
print (list1[3:])  
  
# List slicing  
print (list1[0:2])   
  
# List Concatenation using + operator  
print (list1 + list1)  
  
# List repetation using * operator  
print (list1 * 3)  


"""


"""
tup  = ("hi", "Python", 2)    
# Checking type of tup  
print (type(tup))    
  
#Printing the tuple  
print (tup)  
  
# Tuple slicing  
print (tup[1:])    
print (tup[0:1])    
  
# Tuple concatenation using + operator  
print (tup + tup)    
  
# Tuple repatation using * operator  
print (tup * 3)     
  
# Adding value to tup. It will throw an error.  
t[2] = "hi" 

"""

"""

d = {1:'Jimmy', 2:'Alex', 3:'john', 4:'mike'}     
  
# Printing dictionary  
print (d)  
  
# Accesing value using keys  
print("1st name is "+d[1])   
print("2nd name is "+ d[4])    
  
print (d.keys())    
print (d.values())   


"""


"""

# Creating Empty set  
set1 = set()  
  
set2 = {'James', 2, 3,'Python'}  
  
#Printing Set value  
print(set2)  
  
# Adding element to the set  
  
set2.add(10)  
print(set2)  
  
#Removing element from the set  
set2.remove(2)  
print(set2)  


"""


"""

def return_noe():  
  a = 10  
  b = 20  
  c = a + b  
  #return c
x = return_noe()  
print(x)  


"""


"""
text1 = 'hello\
user\
how are you'    
print(text1)  

"""


#print(ord(" "))
"""
str = "Hello"     
str1 = " world"    
print(str*3) # prints HelloHelloHello    
print(str+str1)# prints Hello world     
print(str[4]) # prints o                
print(str[2:4]); # prints ll   
print(str[1:-1]); # prints ell                 
print('H' in str) # prints false as w is not present in str    
print('wo' not in str1) # prints false as wo is present in str1.     
print(r'C://python37') # prints C://python37 as it is written    
print("The string str : %s"%(str)) # prints The string str : Hello   
# escaping single quotes  
print('They said, "What\'s going on?"')  
  
# escaping double quotes  
print("They said, \"What's going on?\"")  

	
print("\1a") # whait is use of ascii bell
	
print("Hello\bWorld") # uses as backslash

print("Hello \f World!") # Ascii Formfeed

print("Hello \t World!") #ascii Horizontal tab

print("Hello \v World!") # ascii Vertical tab NOT WORKING MAY BE
print("Hello \v World!")

print("\110\145\154\154\157") #Character with octal value
print("\x48\x65\x6c\x6c\x6f") #character with hes value


# Using Curly braces  
print("{} and {} both are the best friend".format("Devansh","Abhishek"))  
  
#Positional Argument  
print("{0} and {0} best players ".format("Virat","Rohit"))  
  
#Keyword Argument  
print("{a},{c},{c}".format(a = "James", b = "Peter", c = "Ricky"))  


"""



# Python center() function example  
# Variable declaration  
str = "Hello Javatpoint"  
# Calling function  
str2 = str.center(99)  
# Displaying result  
print("Old value:", str)  
print("New value:", str2)


