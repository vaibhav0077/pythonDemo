def do_twice(func):  
    def wrapper_do_twice():  
        func()  
        func()  
    # def wrapper_do_twice(name):  
    #     func(name)  
    #     func(name) 
    return wrapper_do_twice

def do_n_times(func , n):
    def aa():
        x = 0
        while x<n:
            func()
            x+=1
    return aa