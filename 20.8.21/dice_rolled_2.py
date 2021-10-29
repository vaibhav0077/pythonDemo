from tkinter import *
from PIL import Image, ImageTk
import random
root = Tk()
# root.geometry("1000x700")
# root.minsize(1000,700)
# root.maxsize(100,700)
dices = ['dice_1.png', 'dice_2.png','dice_3.png','dice_4.png','dice_5.png','dice_6.png']

img = ImageTk.PhotoImage(Image.open(random.choice(dices)))

label1 = Label(root, image=img)
label1.image = img
# label1.configure(image=img)

def dice_rolled():
    img = ImageTk.PhotoImage(Image.open(random.choice(dices)))
    print(img)  
    label1.configure(image=img)
    label1.image = img
    label1.pack()

btn = Button(root,text="Click To Roll the Dice",bg="black",fg="white",font=("verdana",45), command=dice_rolled)
btn.pack(side=BOTTOM)
label1.pack()
root.mainloop()