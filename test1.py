import tkinter as tk

root = tk.Tk()
root.title("Page 1")

page1 = tk.Label(root, text="Page 1")
page1.pack()

def show_page1():
    page1.pack()
    page2.pack_forget()
    page3.pack_forget()

def show_page2():
    page2.pack()
    page1.pack_forget()
    page3.pack_forget()

def show_page3():
    page3.pack()
    page1.pack_forget()
    page2.pack_forget()

button_page1 = tk.Button(root, text="Show Page 2", command=show_page2)
button_page1.pack()

page2 = tk.Label(root, text="Page 2")

button_page2 = tk.Button(root, text="Show Page 3", command=show_page3)
button_page2.pack()

back_button2 = tk.Button(root, text="Back to Page 1", command=show_page1)
back_button2.pack()

page3 = tk.Label(root, text="Page 3")

back_button3 = tk.Button(root, text="Back to Page 2", command=show_page2)
back_button3.pack()

root.mainloop()
