from tkinter import *

root = Tk()
#creating a label widget
# myabel1 = Label(root, text="hello World1").grid(row=0, column=1)
# myabel2 = Label(root, text="hello World2").grid(row=0, column=2)
# myabel3 = Label(root, text="hello World3").grid(row=0, column=3)
#showing ontu a screen
# myabel1.pack()
# myabel2.pack()
# myabel3.pack()

# myabel1.grid(row=0, column=1)
# myabel2.grid(row=0, column=2)
# myabel3.grid(row=0, column=3)

# myabel1.grid(row=1, column=1)
# myabel2.grid(row=1, column=2)
# myabel3.grid(row=1, column=3)

#creating Buttton
def myClick():
    myabel1 = Label(root, text="hello World1")
    myabel1.pack()


btn1 = Button(root, text="Click Me", padx=12, pady=12, command=myClick, fg="red", bg="#00ff00")
btn1.pack()

btn2 = Button(root, text="Not Clickable", state=DISABLED)
btn2.pack() 

root.geometry("500x500")
root.minsize(200,200)
root.maxsize(1000,800)








#showing in window
root.mainloop()