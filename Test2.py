import tkinter as tk
import cv2
from PIL import Image,ImageTk

global page1
global page2
global page3
global page4

root = tk.Tk()
root.title("Main Window")
root.geometry("800x800")
root.resizable(width=False, height=False)

# Open the image
image=Image.open("./pics.png")
image1=Image.open("./pic.png")

# Convert the image to a PhotoImage object
photo = ImageTk.PhotoImage(image)
photo1=ImageTk.PhotoImage(image1)

font = ('broadway', 20, 'bold') 
font1= ('Bodoni MT', 14, 'bold')


page1 = tk.Label(root, image=photo)
page1.pack(fill="both", expand=True)

label = tk.Label(page1, text="Welcome to sign language Converter", font=font , bg='black', fg='white', wraplength=250)
label.pack(pady=50, anchor='w', padx=30)


fourth_label= tk.Label(page1, text="This technology uses computer vision and machine learning algorithms to recognize and interpret sign language gestures, which are then translated into text in real-time. It can be used to break down language barriers and increase understanding.", font=font1, fg='white', wraplength=300, bg='black', justify='left')
fourth_label.pack( pady=80, anchor="w", padx=30)


def on_button_click():
    page4 = tk.Label(root)
    page4.pack(fill="both", expand=True)

    page2 = tk.Label(page4, image=photo1)
    page2.pack(fill="both", expand=True)

    
    
    def on_camera_button_click():
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            frame=cv2.flip(frame,1)
            cv2.imshow("Camera", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
    
    camera_button = tk.Button(page2, text="Open Camera", command=on_camera_button_click)
    camera_button.pack()

    text1 = tk.Text(page2, height=30, width=30, bg='white')
    text1.pack(pady=50, anchor='ne')


    def on_third_page_button_click():
        page3 = tk.Toplevel(root)
        page3.title("Text to sign converter")
        page3.geometry("800x800+100+150")
        
        third_label = tk.Label(page3, text="Text to sign converter")
        third_label.pack()
        
        scrollbar = tk.Scrollbar(page3)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        options = [str(i) for i in range(1, 31)]
        
        my_list = tk.Listbox(page3, yscrollcommand=scrollbar.set, selectmode=tk.SINGLE)
        for option in options:
            my_list.insert(tk.END, option)
        my_list.pack(side=tk.LEFT, fill=tk.BOTH)
        
        scrollbar.config(command=my_list.yview)
    
    third_page_button = tk.Button(page2, text="Go to Text to sign converter", command=on_third_page_button_click, bg="lightyellow")
    third_page_button.pack()

button = tk.Button(page1, text="Go to Sign to text converter", command=on_button_click, bg="white")
button.pack(pady=50, anchor='w', padx=50)

def page3():
    page3.pack()

def show_page1():
    page1.pack()
    page4.pack()

def show_page2():
    page4.pack()
    page1.pack_forget() 
    page3.pack_forget()

def show_page3():
    page3.pack()
    page1.pack_forget()
    page4.pack_forget()

root.mainloop()


