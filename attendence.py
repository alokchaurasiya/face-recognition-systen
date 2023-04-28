from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1540x800+0+0")
        self.root.title("Face Recognisation System")
    #image 1
        img1=Image.open(r"face project inages\f24.jpg")
        img1=img1.resize((750,220),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=70,width=750,height=220)

    #image 2
        img2=Image.open(r"face project inages\f25.jpg")
        img2=img2.resize((800,220),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=750,y=70,width=800,height=220)

    #title
        title_lbl=Label(self.root,text="ATTENDENCE  MANAGEMENT  SYSTEM", font=("times new roman",35,"bold"),bg="black",fg="orange")
        title_lbl.place(x=0,y=10,width=1540,height=40)

    #Frame
        main_frame = Frame(self.root,bd=2,bg="white")
        main_frame.place(x=15,y=300,width=1500,height=650)

    # left label frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT ATTENDENCE DETAILS",font=("time new raman",12,"bold"))
        left_frame.place(x=10,y=10,width=720,height=580)

        left_inside_frame = Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=7,y=10,width=700,height=420)

    #label and Entry

        #student id
        attendenceid=Label(left_inside_frame,text="Attendence Id :",font=("time new raman",12,"bold"),bg="white")
        attendenceid.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        attendenceId_entry=ttk.Entry(left_inside_frame,width=20,font=("time new raman",12,"bold"))
        attendenceId_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #Roll.NO
        rollLabel=Label(left_inside_frame,text="Roll.No :",font=("time new raman",12,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        atten_roll=ttk.Entry(left_inside_frame,width=20,font=("time new raman",12,"bold"))
        atten_roll.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        #Name
        nameLabel=Label(left_inside_frame,text="Name :",font=("time new raman",12,"bold"),bg="white")
        nameLabel.grid(row=1,column=0)

        atten_name=ttk.Entry(left_inside_frame,width=20,font=("time new raman",12,"bold"))
        atten_name.grid(row=1,column=1,pady=35)

        #Department
        depLabel=Label(left_inside_frame,text="Department :",font=("time new raman",12,"bold"),bg="white")
        depLabel.grid(row=1,column=2)

        atten_dep=ttk.Entry(left_inside_frame,width=20,font=("time new raman",12,"bold"))
        atten_dep.grid(row=1,column=3,pady=35)

        #Date
        timeLabel=Label(left_inside_frame,text="Date :",font=("time new raman",12,"bold"),bg="white")
        timeLabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,width=20,font=("time new raman",12,"bold"))
        atten_time.grid(row=2,column=1,pady=35)

        #Time
        timeLabel=Label(left_inside_frame,text="Time :",font=("time new raman",12,"bold"),bg="white")
        timeLabel.grid(row=2,column=2)

        atten_time=ttk.Entry(left_inside_frame,width=20,font=("time new raman",12,"bold"))
        atten_time.grid(row=2,column=3,pady=35)

        #Attendece
        attendenceLabel=Label(left_inside_frame,text="Attendence Status :",font=("time new raman",12,"bold"),bg="white")
        attendenceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,font='comicsansns 11 bold',state='readonly')
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=35)
        self.atten_status.current(0)

    #BUTTOM

        #button frame 
        btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=2,y=350,width=685,height=30)

        #save button
        save_btn=Button(btn_frame,text="Import.csv",width=17,font=("time new raman",12,"bold"),bg="black",fg="orange")
        save_btn.grid(row=0,column=0,)

        #update button
        update_btn=Button(btn_frame,text="Export.csv",font=("time new raman",12,"bold"),bg="black",fg="orange",width=16)
        update_btn.grid(row=0,column=1,)

        #delete button
        delete_btn=Button(btn_frame,text="Update",font=("time new raman",12,"bold"),bg="black",fg="orange",width=16)
        delete_btn.grid(row=0,column=2,)

        #reset button
        rest_btn=Button(btn_frame,text="Reset",font=("time new raman",12,"bold"),bg="black",fg="orange",width=16)
        rest_btn.grid(row=0,column=3,)


    

    # right label frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="ATTENDENCE RECODE",font=("time new raman",12,"bold"))
        right_frame.place(x=740,y=10,width=740,height=580)

        table_frame = Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=720,height=424)

#============Scroll bar right table================================

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendenceReportTable=ttk.Treeview(table_frame,columns=("id","roll.no","name","department","date","time","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendenceReportTable.xview)
        scroll_y.config(command=self.attendenceReportTable.yview)

        self.attendenceReportTable.heading("id",text="Attendence ID")
        self.attendenceReportTable.heading("roll.no",text="Roll.No")
        self.attendenceReportTable.heading("name",text="Name")
        self.attendenceReportTable.heading("department",text="Department")
        self.attendenceReportTable.heading("date",text="Date")
        self.attendenceReportTable.heading("time",text="Time")
        self.attendenceReportTable.heading("attendence",text="Attendence")

        self.attendenceReportTable["show"]="headings"

        self.attendenceReportTable.column("id" ,width=100)
        self.attendenceReportTable.column("roll.no" ,width=100)
        self.attendenceReportTable.column("name" ,width=100)
        self.attendenceReportTable.column("department" ,width=100)
        self.attendenceReportTable.column("date" ,width=100)
        self.attendenceReportTable.column("time" ,width=100)
        self.attendenceReportTable.column("attendence" ,width=100)

        self.attendenceReportTable.pack(fill=BOTH ,expand=1) 
        



    







if __name__=="__main__":
    root=Tk()
    obj =Attendence(root)
    root.mainloop()