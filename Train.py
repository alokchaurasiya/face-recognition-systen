from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

class train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1540x800+0+0")
        self.root.title("Face Recognisation System")

        #Title
        title_lbl=Label(self.root,text="TRAIN DATASET", font=("times new roman",35,"bold"),bg="black",fg="orange")
        title_lbl.place(x=0,y=0,width=1540,height=40)
        
        #Image
        img_top=Image.open(r"face project inages\f26.png")
        img_top=img_top.resize((1550,800),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1550,height=800)

        #Photo Button
        img10=Image.open(r"face project inages\f18.jpg")
        img10=img10.resize((420,420),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(self.root,image=self.photoimg10,cursor="hand2",command=self.train_classifier)
        b1.place(x=950,y=200,width=420,height=420)

        b1=Button(self.root,text="Train Face",cursor="hand2",command=self.train_classifier,font=("times new roman",15,"bold"),bg="black",fg="orange")
        b1.place(x=950,y=570,width=420,height=60)
        
    
    def train_classifier(self):
        data_dir=("data")
        print(data_dir)
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)] 
        

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNP=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            

            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training...",imageNP)
            cv2.waitKey(1)==13
        ids=np.array(ids) 

    #==========Train the classifier========================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("DataTrain.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed!!",parent=self.root)



if __name__=="__main__":
    root=Tk()
    obj =train(root)
    root.mainloop()