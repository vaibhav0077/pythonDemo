import collections 
from collections import defaultdict   
from collections import Counter

d1=collections.OrderedDict()    
d1['A']=10    
d1['C']=12    
d1['B']=11    
d1['D']=13    
    
for k,v in d1.items():    
    print (k,v)    


number = defaultdict(int)      
number['one'] = 1      
number['two'] = 2      
number[3] = 20      
print(number)
print(number['two'])  
print(number[3])


c = Counter()    
list = [1,2,3,4,5,7,8,5,9,6,10]      
print(Counter(list))
print(c)
Counter({1:5,2:4})      
list = [1,2,4,7,5,1,6,7,6,9,1]      
c = Counter(list)      
print(c[1])    