import tkinter as tk
from tkinter import messagebox 
from PIL import Image,ImageTk


root =tk.Tk()
root.title("JOB Profile GUI")
try: 
    image = Image.open(r"c:\Users\sharm\OneDrive\Desktop\python project\Beginnier python project\Project 2 JOB PROFILE GUI\001.jpg")
    image = image.resize((150,150,),Image.ANTIALIAS) # Resize the image to fit the label
    profile_pic = ImageTk.PhotoImage(image)
    image_label = tk.Label(root,image = profile_pic)
    image_label.pack(pady=10)
except Exception as e:
    print("Error",f"Image not found:{e}")
    image_label =tk.Label(root,text = "Image not found")
    image_label.pack(pady=10)
label = tk.Label(root,text= " Name : Shubham Sharma \n Phone number :9519168978  \n Mail id = sharmashubham0715@gmail.com")
label.pack(padx=20,pady=20)
close_button = tk.Button(root,text = "close" ,command = root.quit)
close_button.pack(pady =10)
root.mainloop() # yeh aapka GUI event loop shuru karta hai jo window ko display karta hai aur user interaction ka intezaar karta hai

