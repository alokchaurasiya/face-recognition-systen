from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1540x800+0+0")
        self.root.title("SUPPORT")

     #Title
        title_lbl=Label(self.root,text="HELP DESK", font=("times new roman",40,"bold"),fg="Red")
        title_lbl.place(x=0,y=0,width=1540,height=65)
    
     #Image left
        img_top=Image.open(r"face project inages\f23.jpg")
        img_top=img_top.resize((1550,650),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=75,width=1550,height=650)

        dev_label=Label(f_lbl,text="alokchaurasiya0414@gmail.com", font=("times new roman",20,"bold"),fg="blue")
        dev_label.place(x=185,y=300)


if __name__=="__main__":
    root=Tk()
    obj =help(root)
    root.mainloop()