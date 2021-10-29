from tkinter import *  
import time as t
top = Tk()  
top.geometry("400x250")  




name1 = Label(top,text = "abcde").grid(row = 0, column = 0)  
e1 = Entry(top).grid(row = 0, column = 1)  
password1 = Label(top,text = "frghut").grid(row = 1, column = 0)  
e2 = Entry(top).grid(row = 1, column = 1)  
submit1 = Button(top, text = "Submit").grid(row = 4, column = 0) 

name = Label(top, text = "Name").place(x = 0,y = 70)  
email = Label(top, text = "Email").place(x = 0, y = 90)  
password = Label(top, text = "Password").place(x = 0, y = 130)  
e1 = Entry(top).place(x = 80, y = 70)  
e2 = Entry(top).place(x = 80, y = 90)  
e3 = Entry(top).place(x = 80, y = 130)  




# t.sleep(10)
top.mainloop()  