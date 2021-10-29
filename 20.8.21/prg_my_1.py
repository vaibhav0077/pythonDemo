import tkinter 
import os
import keyboard
def fun(event):
    print("called")
    print("Event : ", event)
    print("Event key" , event.keysym)
def win():
    A = True
    while A == True:
        window = tkinter.Tk()
        window.title('YOU ARE HACKED')
        window.geometry('500x500')
        # window.attributes('-fullscreen',True)
        window.configure(background= "green")
        lbl = tkinter.Label(window, text= 'HACKED GOOD BYE', bg= 'red', font= 200)
        window.bind("<KeyRelease>", fun, fun1)

        lbl.pack()
        window.mainloop()

win()
# quit = False
# while quit == False:
#     win()