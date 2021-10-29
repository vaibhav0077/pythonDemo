# def hello():  
#     def hi():  
#         print("Hello")  
#     return hi  
# new = hello()  
# print(new())



# def divide(x,y):  
#     print(x/y)  
# def outer_div(func):  
#     def inner(x,y):  
#         if(x<y):  
#             x,y = y,x  
#         return func(x,y)
#     print(inner)  
#     return inner  
# divide1 = outer_div(divide)  
# print(divide1(2,4))


# def outer_div(func):  
#     def inner(x,y):  
#         if(x<y):  
#            x,y = y,x  
#         return func(x,y)  
#     return inner  
# # syntax of generator  
# @outer_div  
# def divide(x,y):  
#      print(x/y) 

# divide1 = outer_div(divide)  
# divide1(4,21)  



from mod_decorator import *  
@do_twice  
def say_hello():  
    print("Hello There")  
say_hello()  

@do_n_times(23)
def say_hello():  
    print("Hello n times")  
say_hello() 

@do_twice  
def display(name):  
     print(f"Hello {name}")  
display("abvde")  