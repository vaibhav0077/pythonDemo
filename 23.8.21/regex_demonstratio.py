import re  
  
str = "How are you. Howa is everything"  
  
matches = re.findall("How", str)  
  
print(matches)  
print(type(matches)) 

matches = re.search("Howa", str)
print(matches.span())  
print(matches.group())  
print(matches.string) 