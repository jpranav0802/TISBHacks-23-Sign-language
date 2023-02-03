import tkinter as tk
import tkVideoPlayer
from tkVideoPlayer import TkinterVideo


root = tk.Tk()
root.title("Video Player")

def on_select(value):
    if value == "Hello":
        video = TkinterVideo(root, "v1.mp4")
        video.pack()
        video.play()
    elif value == "Goodye":
        video = TkinterVideo(root, "v2.mp4")
        video.pack()
        video.play()
    elif value == "Thank you":
        video = TkinterVideo(root, "v3.mp4")
        video.pack()
        video.play()
    elif value == "Please":
        video = TkinterVideo(root, "v4.mp4")
        video.pack()
        video.play()
    elif value == "Yes":
        video = TkinterVideo(root, "v5.mp4")
        video.pack()
        video.play()
    elif value == "No":
        video = TkinterVideo(root, "v6.mp4")
        video.pack()
        video.play()
    elif value == "Sorry":
        video = TkinterVideo(root, "v7.mp4")
        video.pack()
        video.play()
    elif value == "Excuse me ":
        video = TkinterVideo(root, "v8.mp4")
        video.pack()
        video.play()
    elif value == "My name is ":
        video = TkinterVideo(root, "v9.mp4")
        video.pack()
        video.play()
    elif value == "Nice to meet you":
        video = TkinterVideo(root, "v10.mp4")
        video.pack()
        video.play()
    elif value == "How are you?":
        video = TkinterVideo(root, "v11.mp4")
        video.pack()
        video.play()
    elif value == "I'm fine":
        video = TkinterVideo(root, "v12.mp4")
        video.pack()
        video.play()
    elif value == "What's your name?":
        video = TkinterVideo(root, "v13.mp4")
        video.pack()
        video.play()
    elif value == "I love you":
        video = TkinterVideo(root, "v14.mp4")
        video.pack()
        video.play()
    elif value == "Help":
        video = TkinterVideo(root, "v15.mp4")
        video.pack()
        video.play()
    elif value == "I'm hungry":
        video = TkinterVideo(root, "video9.mp4")
        video.pack()
        video.play()
    elif value == "I'm thirsty":
        video = TkinterVideo(root, "video10.mp4")
        video.pack()
        video.play()
    elif value == "Do you speak ASL":
        video = TkinterVideo(root, "video6.mp4")
        video.pack()
        video.play()
    elif value == "I don't know":
        video = TkinterVideo(root, "video7.mp4")
        video.pack()
        video.play()
    elif value == "I'm deaf":
        video = TkinterVideo(root, "video8.mp4")
        video.pack()
        video.play()
    elif value == "I'm hearing":
        video = TkinterVideo(root, "video9.mp4")
        video.pack()
        video.play()
    elif value == "I'm blind":
        video = TkinterVideo(root, "video10.mp4")
        video.pack()
        video.play()
    elif value == "Can you repeat that?":
        video = TkinterVideo(root, "video9.mp4")
        video.pack()
        video.play()
    elif value == "Can you show me?":
        video = TkinterVideo(root, "video10.mp4")
        video.pack()
        video.play()
    elif value == "I'm from __":
        video = TkinterVideo(root, "video6.mp4")
        video.pack()
        video.play()
    elif value == "":
        video = TkinterVideo(root, "video7.mp4")
        video.pack()
        video.play()
    elif value == "How much does it cost?":
        video = TkinterVideo(root, "video8.mp4")
        video.pack()
        video.play()
    elif value == "I don't understand":
        video = TkinterVideo(root, "v16.mp4")
        video.pack()
        video.play()
    elif value == "Where is the bathroom":
        video = TkinterVideo(root, "video10.mp4")
        video.pack()
        video.play()
    elif value == "I live in __":
        video = TkinterVideo(root, "video10.mp4")
        video.pack()
        video.play()
        

var = tk.StringVar(root)
var.set("Select Video")

options = ["Hello", "No", "Yes", "Video 4", "Video 5",
           "Video 6", "Video 7", "Video 8", "Video 9", "Video 10"]

dropdown = tk.OptionMenu(root, var, *options, command=lambda value: on_select(value))
dropdown.pack()

root.mainloop()
