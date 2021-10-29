from math import exp
from tkinter import *
from PIL import Image, ImageTk
import random


def dice_rolled():
    num = random.randint(1, 6)
    print(num)
    
    
    # Read the Image
    # image = Image.open("dice_1.png")
    # print(image)
    image = image_setter(num)
    print(image)

    # Reszie the image using resize() method
    resize_image = image.resize((500, 500))
    
    img = ImageTk.PhotoImage(image.resize((500, 500)))

    # create label and add resize image
    
    label1 = Label(root, image=img)
    label1.configure(image=img)
    label1.image = img
    
    label1.pack(expand=True)
    



def image_setter(num):
    switcher={
                1:Image.open("dice_1.png"),
                2:Image.open("dice_2.png"),
                3:Image.open("dice_3.png"),
                4:Image.open("dice_4.png"),
                5:Image.open("dice_5.png"),
                6:Image.open("dice_6.png")
             }
    return switcher.get(num)


root = Tk()

root.geometry("1000x700")
root.minsize(1000,700)
root.maxsize(100,700)

btn = Button(root,text="Click To Roll the Dice",bg="black",fg="white",font=("verdana",45), command=dice_rolled)
btn.pack(side=BOTTOM)


# image = Image.open("dice_1.png")
# resize_image = image.resize((500, 500))
    
# img = ImageTk.PhotoImage(resize_image)

# # create label and add resize image
    
# label1 = Label(image=img)
# label1.configure = img
# label1.pack()

root.mainloop()