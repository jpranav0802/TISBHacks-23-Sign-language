from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("800x600")

# Open the image file
img = Image.open("pic.png")

# Convert the image to a PhotoImage object
img = ImageTk.PhotoImage(img)

# Create a label and set the image as the background
label = Label(root, image=img)
label.place(x=0, y=0, relwidth=1, relheight=1)

root.mainloop()


