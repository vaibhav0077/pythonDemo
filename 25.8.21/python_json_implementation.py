import json

# # print(dir(json))
 
# # Key:value mapping  
# student  = [{  
#     "Name" : "Peter",  
#     "Roll_no" : "0090014",  
#     "Grade" : "A",  
#     "Age": 20,  
#     "Subject": ["Computer Graphics", "Discrete Mathematics", "Data Structure"]  
# },
# {
#     "Name" : "Vaibhav",  
#     "Roll_no" : "0090015",  
#     "Grade" : "A+",  
#     "Age": 20,  
#     "Subject": ["Computer Graphics", "Discrete Mathematics", "Data Structure"] 
# } ] 
# # Dump will write the data in file
# with open("data1.json","w") as write_file:  
#     json.dump(student,write_file) 

# # Load will wirte the data in another variable
# with open("data.json", "r") as read_file:  
#     b = json.load(read_file)  
# # print(b) 


# #Python  list conversion to JSON  Array   
# print((['Welcome', "to", "javaTpoint"]))  
  
# #Python  tuple conversion to JSON Array   
# print(json.dumps(("Welcome", "to", "javaTpoint")))  
  
# # Python string conversion to JSON String   
# print(json.dumps("Hello"))  
  
# # Python int conversion to JSON Number   
# print(json.dumps(1234))  
  
# # Python float conversion to JSON Number   
# print(json.dumps(23.572))  
  
# # Boolean conversion to their respective values   
# print(json.dumps(True))  
# print(json.dumps(False))  
  
# # None value to null   
# print(json.dumps(None)) 

# a = (10,20,30,40,50,60,70)  
# print(type(a))  
# b = json.dumps(a)
# print(json.dumps(a))  
# print(type(json.loads(b))) 
# print (b) 

with open("data.json", "r") as aa:
    c = json.load(aa)
    # ds = json.loads(aa)
# he json.load() function is used to load JSON file, whereas json.loads() function is used to load string.
print(c)
# print(str(ds))     // ERRORS


