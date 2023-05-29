from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import os 

class About:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1540x800+0+0")
        self.root.title("Face Recognisation System")

        #title
        title_lbl=Label(self.root,text="ABOUT", font=("times new roman",35,"bold"),bg="black",fg="orange")
        title_lbl.place(x=0,y=10,width=1540,height=40)

        

if __name__=="__main__":
    root=Tk()
    obj =About(root)
    root.mainloop()