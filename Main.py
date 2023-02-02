import tkinter as tk
import cv2
from PIL import Image
from tkinter import Label
from PIL import ImageTk as itk


root = tk.Tk()
root.title("Main Window")
root.geometry("800x800")
root.resizable(width=False, height=False)

global sixth_label


img = itk.PhotoImage(file = "pics.png")
img1=itk.PhotoImage(file = "pic.png")

font = ('broadway', 20, 'bold') 
font1= ('Bodoni MT', 14, 'bold')

fifth_label = tk.Label(root, image=img)
fifth_label.pack(fill="both", expand=True)

label = Label(fifth_label, text="Welcome to sign language Converter", font=font , bg='black', fg='white', wraplength=250)
label.pack(pady=50, anchor='w', padx=30)


fourth_label= tk.Label(fifth_label, text="This technology uses computer vision and machine learning algorithms to recognize and interpret sign language gestures, which are then translated into text in real-time. It can be used to break down language barriers and increase understanding.", font=font1, fg='white', wraplength=300, bg='black', justify='left')
fourth_label.pack( pady=80, anchor="w", padx=30)


def on_button_click():
    second_page = tk.Toplevel(root)
    second_page.title("Sign to text translator")
    second_page.geometry("800x800")
    # second_page.pack(fill="both", expand=True)

    sixth_label = tk.Label(second_page, image=img1)
    
    sixth_label.pack(fill="both", expand=True)

def on_button_click():
    second_page = tk.Toplevel(root)
    second_page.title("Sign to text translator")
    second_page.geometry("800x800")

    sixth_label = tk.Label(second_page, image=img1)
    sixth_label.place(x = 0, y = 0)
    
    camera_button = tk.Button(second_page, text="Open Camera", command=on_camera_button_click)
    camera_button.pack()

    text1 = tk.Text(second_page, height=30, width=30, bg='white')
    text1.pack(pady=50, anchor='ne')
    
    third_page_button = tk.Button(second_page, text="Go to Text to sign converter", command=on_third_page_button_click, bg="lightyellow")
    third_page_button.pack()

    
    
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
    
    camera_button = tk.Button(sixth_label, text="Open Camera", command=on_camera_button_click)
    camera_button.pack()

    text1 = tk.Text(sixth_label, height=30, width=30, bg='white')
    text1.pack(pady=50, anchor='ne')


def on_third_page_button_click():
    third_page = tk.Toplevel(root)
    third_page.title("Text to sign converter")
    third_page.geometry("800x800")
        
    third_label = tk.Label(third_page, text="Text to sign converter")
    third_label.pack()
        
    scrollbar = tk.Scrollbar(third_page)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
    options = [str(i) for i in range(1, 31)]
        
    my_list = tk.Listbox(third_page, yscrollcommand=scrollbar.set, selectmode=tk.SINGLE)
    for option in options:
        my_list.insert(tk.END, option)
    my_list.pack(side=tk.LEFT, fill=tk.BOTH)
        
    scrollbar.config(command=my_list.yview)
def sixth_label():
    third_page_button = tk.Button(sixth_label, text="Go to Text to sign converter", command=on_third_page_button_click, bg="lightyellow")
    third_page_button.pack()

button = tk.Button(fifth_label, text="Go to Sign to text converter", command=on_button_click, bg="white")
button.pack(pady=50, anchor='w', padx=50)

root.mainloop()
