
import tkinter as tk
import cv2
import subprocess


from PIL import Image
from tkinter import Label, OptionMenu, StringVar
from tkinter import filedialog
from tkVideoPlayer import TkinterVideo 
from PIL import ImageTk as itk

root = tk.Tk()
root.title("Main Window")
frame= tk.Frame(root)   
root.geometry("800x800")
root.resizable(width=False, height=False)

v1 = TkinterVideo(root, "v1.mp4")
v2 = TkinterVideo(root, "v2.mp4")
v3 = TkinterVideo(root, "v3.mp4")
v4 = TkinterVideo(root, "v4.mp4")
v5 = TkinterVideo(root, "v5.mp4")
v6 = TkinterVideo(root, "v6.mp4")
v7 = TkinterVideo(root, "v7.mp4")
v8 = TkinterVideo(root, "v8.mp4")
v9 = TkinterVideo(root, "v9.mp4")
v10 = TkinterVideo(root, "v10.mp4")
v11 = TkinterVideo(root, "v11.mp4")
v12 = TkinterVideo(root, "v12.mp4")
v13 = TkinterVideo(root, "v13.mp4")
v14 = TkinterVideo(root, "v14.mp4")
v15 = TkinterVideo(root, "v15.mp4")
v16 = TkinterVideo(root, "v16.mp4")
v17 = TkinterVideo(root, "v17.mp4")
v18 = TkinterVideo(root, "v18.mp4")
v19 = TkinterVideo(root, "v19.mp4")
v20 = TkinterVideo(root, "v20.mp4")
v21 = TkinterVideo(root, "v21.mp4")
v22 = TkinterVideo(root, "v22.mp4")
v23 = TkinterVideo(root, "v23.mp4")
v24 = TkinterVideo(root, "v24.mp4")
v25 = TkinterVideo(root, "v25.mp4")
v26 = TkinterVideo(root, "v26.mp4")
v27 = TkinterVideo(root, "v27.mp4")
v28 = TkinterVideo(root, "v28.mp4")
v29 = TkinterVideo(root, "v29.mp4")
v30 = TkinterVideo(root, "v30.mp4")



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
    
    def on_select(values):
        if values == "Hello":
            video = TkinterVideo(label3, "v1.mp4")
            video.pack()
            video.play()
        elif values == "Goodye":
            video = TkinterVideo(label3, "v2.mp4")
            video.pack()
            video.play()
        elif values == "Thank you":
            video = TkinterVideo(label3, "v3.mp4")
            video.pack()
            video.play()
        elif values == "Please":
            video = TkinterVideo(label3, "v4.mp4")
            video.pack()
            video.play()
        elif values == "Yes":
            video = TkinterVideo(label3, "v5.mp4")
            video.pack()
            video.play()
        elif values == "No":
            video = TkinterVideo(label3, "v6.mp4")
            video.pack()
            video.play()
        elif values == "Sorry":
            video = TkinterVideo(label3, "v7.mp4")
            video.pack()
            video.play()
        elif values == "Excuse me ":
            video = TkinterVideo(label3, "v8.mp4")
            video.pack()
            video.play()
        elif values == "My name is ":
            video = TkinterVideo(label3, "v9.mp4")
            video.pack()
            video.play()
        elif values == "Nice to meet you":
            video = TkinterVideo(label3, "v10.mp4")
            video.pack()
            video.play()
        elif values == "How are you?":
            video = TkinterVideo(label3, "v11.mp4")
            video.pack()
            video.play()
        elif values == "I'm fine":
            video = TkinterVideo(label3, "v12.mp4")
            video.pack()
            video.play()
        elif values == "What's your name?":
            video = TkinterVideo(label3, "v13.mp4")
            video.pack()
            video.play()
        elif values == "I love you":
            video = TkinterVideo(label3, "v14.mp4")
            video.pack()
            video.play()
        elif values == "Help":
            video = TkinterVideo(label3, "v15.mp4")
            video.pack()
            video.play()
        elif values == "I'm hungry":
            video = TkinterVideo(label3, "v20.mp4")
            video.pack()
            video.play()
        elif values == "I'm thirsty":
            video = TkinterVideo(label3, "v21.mp4")
            video.pack()
            video.play()
        elif values == "Do you speak ASL":
            video = TkinterVideo(label3, "v22.mp4")
            video.pack()
            video.play()
        elif values == "I don't know":
            video = TkinterVideo(label3, "v23.mp4")
            video.pack()
            video.play()
        elif values == "I'm deaf":
            video = TkinterVideo(label3, "v24.mp4")
            video.pack()
            video.play()
        elif values == "I'm hearing":
            video = TkinterVideo(label3, "v25.mp4")
            video.pack()
            video.play()
        elif values == "I'm blind":
            video = TkinterVideo(label3, "v26.mp4")
            video.pack()
            video.play()
        elif values == "Can you repeat that?":
            video = TkinterVideo(label3, "v27.mp4")
            video.pack()
            video.play()
        elif values == "Can you show me?":
            video = TkinterVideo(label3, "v28.mp4")
            video.pack()
            video.play()
        elif values == "I'm from __":
            video = TkinterVideo(label3, "v29.mp4")
            video.pack()()
            video.play()
        elif values == "How much does it cost?":
            video = TkinterVideo(label3, "v18.mp4")
            video.pack()
            video.play()
        elif values == "I don't understand":
            video = TkinterVideo(label3, "v16.mp4")
            video.pack()
            video.play()
        elif values == "Where is the bathroom":
            video = TkinterVideo(label3, "v17.mp4")
            video.pack()
            video.play()
        elif values == "I live in __":
            video = TkinterVideo(label3, "v30.mp4")
            video.pack()
            video.play()
    
    drop = OptionMenu(label3, clicked, *values, command=lambda value: on_select(value))
    drop.pack()
    videoplayer=TkinterVideo(label3, pre_load=False)
    label3.pack(fill="both", expand=True)
    
    
   
root.mainloop()
