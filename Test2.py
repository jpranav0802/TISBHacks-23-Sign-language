from pty import master_open
import tkinter as tk
import cv2
import subprocess
import datetime

from PIL import Image
from tkinter import Label, OptionMenu, StringVar
from tkinter import filedialog
from tkVideoPlayer import TkinterVideo
from PIL import ImageTk as itk

def run_other_program():
    subprocess.run(["python", "final.py"])

def button_click1():
    second_page = tk.Toplevel(root)
    second_page.title("Sign to text translator")
    second_page.geometry("800x800")
    second_page.resizable(width=False, height=False)
    label2 = tk.Label(second_page, image=img1)
    label2.pack(fill="both", expand=True)

    camera_button = tk.Button(label2, text="Open Camera", command=run_other_program)
    camera_button.pack()

    text1 = tk.Text(label2, height=30, width=30, bg='white')
    text1.pack(pady=50, anchor='ne', padx=35)

    third_page_button = tk.Button(label2, text="Go to Text to sign converter", command=on_third_page_button_click, bg="lightyellow")
    third_page_button.pack()

    second_page.pack(fill="both", expand=True)
    
    
    
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

    

root = tk.Tk()
root.title("Main Window")
frame= tk.Frame(root)
root.geometry("800x800")
root.resizable(width=False, height=False)


img = itk.PhotoImage(file = "pics.png")
img1=itk.PhotoImage(file = "pic.png")
img2 = itk.PhotoImage(file = "picss.png")

font = ('broadway', 20, 'bold') 
font1= ('Bodoni MT', 14, 'bold')

label1 = tk.Label(root, image=img)
label1.pack(fill="both", expand=True)

tlabel1 = Label(label1, text="Welcome to sign language Converter", font=font , bg='black', fg='white', wraplength=250)
tlabel1.pack(pady=50, anchor='w', padx=30)


tlabel2= tk.Label(label1, text="This technology uses computer vision and machine learning algorithms to recognize and interpret sign language gestures, which are then translated into text in real-time. It can be used to break down language barriers and increase understanding.", font=font1, fg='white', wraplength=300, bg='black', justify='left')
tlabel2.pack( pady=80, anchor="w", padx=30)

button1 = tk.Button(label1, text="Go to Sign to text converter", command=button_click1, bg="white")
button1.pack(pady=50, anchor='w', padx=50)





def on_third_page_button_click():
    third_page = tk.Toplevel(root)
    third_page.title("Text to sign converter")
    third_page.geometry("800x800")
    third_page.resizable(width=False, height=False)
    label3 = tk.Label(third_page, image=img2)
    label3.pack(fill="both", expand=True)
        
    third_label = tk.Label(label3, text="Text to sign converter")
    third_label.pack()
        
    clicked = StringVar()
    
    values=[
        "Hello",
        "Goodbye",
        "Thank you",
        "Please",
        "Yes",
        "No",
        "Sorry",
        "Excuse me",
        "My name is ", 
        "Nice to meet you",
        "How are you?",
        "I'm fine",
        "What's your name?",
        "I love you",
        "Help",
        "I don't understand",
        "Where is the bathroom?",
        "How much does it cost?",
        "How do you say in sign language?",
        "I'm hungry",
        "I'm thirsty",
        "Do you speak ASL?",
        "I don't know",
        "I'm deaf",
        "I'm hearing",
        "I'm blind",
        "Can you repeat that?",
        "Can you show me?",
        "I'm from __",
        "I live in __"]

    drop = OptionMenu(label3, clicked, *values)
    drop.pack()
    

# play a video everytime an item from the dropdown menu is selected


   
root.mainloop()
