from tkinter import *   
  
top = Tk() 


  
top.geometry("200x100")  
  
def fun():  
   msg = Tk()
   label1 = Label(msg, text="Hello Buddy")
   label1.pack()
   msg.mainloop()
  
b1 = Button(top,text = "Red",command = fun,activeforeground = "red",activebackground = "pink",pady=10)  
b2 = Button(top, text = "Blue",activeforeground = "blue",activebackground = "pink",pady=10)   
b3 = Button(top, text = "Green",activeforeground = "green",activebackground = "pink",pady = 10)  
b4 = Button(top, text = "Yellow",activeforeground = "yellow",activebackground = "pink",pady = 10)  
  
b1.pack(side = LEFT)  
b2.pack(side = RIGHT)  
b3.pack(side = TOP)  
b4.pack(side = BOTTOM)  

top.mainloop()  