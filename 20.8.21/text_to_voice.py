from gtts import gTTS
import os
from tkinter import *  
import time as t
root = Tk()
ss = StringVar()
def playing():
    if str(ss.get()) == "" :
        tts=gTTS(text='''Dilbar dilbar…


 
Chadha jo mujhpe suroor hai
Asar tera yeh zaroor hai
Teri nazar ka kasoor hai

Dilbar dilbar…

Aa paas aa tu kyun door hai
Yeh ishq ka jo fitoor hai
Nashe mein dil tere choor hai

Dilbar dilbar…

Ab toh hosh na khabar hai
Yeh kaisa asar hai
Hosh na khabar hai
Yeh kaisa asar hai
Tumse milne ke baad dilbar
Tumse milne ke baad dilbar''',lang="hi")
        tts.save("hello.mp3")
        os.system("start hello.mp3")
    else:
        print(str(ss.get()))
        tts=gTTS(text=str(ss.get()),lang="hi")
        tts.save("hello.mp3")
        os.system("start hello.mp3")

def clearing():

    name_entry.delete(0, END)
    name_entry.insert(0, "")
    
def quitting():
    root.destroy()

T = Text(root, height = 5, width = 52)

name_label =Label(root, text = 'Enter The String : ', font=('calibre',25, 'bold'))

name_entry = Entry(root,textvariable=ss, font=('calibre',25,'normal'))

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
  


btn1 = Button(root , text="PLAY" , font = ("verdana" , 15),command=playing)
btn1.grid(row=1,column=0)

btn2 = Button(root , text="CLEAR" , font = ("verdana" , 15),command=clearing)
btn2.grid(row=1,column=1)

btn3 = Button(root , text="QUIT" , font = ("verdana" , 15),command=quitting)
btn3.grid(row=1,column=4)

def show():
    label.config( text = clicked.get() )


options = [
	"en",
	"hi"
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set( "en" )

# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.grid(row=3 , column=0)

# Create button, it will change label text
button = Button( root , text = "click Me" , command = show ).grid(row=6, column=0)

# Create Label
label = Label( root , text = " " )
label.grid(row=4 , column=0)

print(clicked)
root.mainloop()

