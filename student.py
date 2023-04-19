from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1540x800+0+0")
        self.root.title("Face Recognisation System")
        
        #===============Variable====================================

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()



        img1=Image.open(r"C:\Users\Alok Chaurasiya\OneDrive\Desktop\face recognition systen\face project inages\f12.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)


        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)

        img2=Image.open(r"C:\Users\Alok Chaurasiya\OneDrive\Desktop\face recognition systen\face project inages\f1.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)

        img3=Image.open(r"C:\Users\Alok Chaurasiya\OneDrive\Desktop\face recognition systen\face project inages\f14.jpg")
        img3=img3.resize((500,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        img4=Image.open(r"C:\Users\Alok Chaurasiya\OneDrive\Desktop\face recognition systen\face project inages\f13.jpg")
        img4=img4.resize((1540,720),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1540,height=720)

        title_lbl=Label(bg_img,text="STUDENT  MANAGEMENT  SYSTEM", font=("times new roman",35,"bold"),bg="black",fg="orange")
        title_lbl.place(x=0,y=0,width=1540,height=40)

        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=41,width=1500,height=650)

        # left label frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("time new raman",12,"bold"))
        left_frame.place(x=10,y=10,width=720,height=580)

        img_img=Image.open(r"C:\Users\Alok Chaurasiya\OneDrive\Desktop\face recognition systen\face project inages\f16.jpg")
        img_img=img_img.resize((720,130),Image.ANTIALIAS)
        self.photoimg_img=ImageTk.PhotoImage(img_img)


        f_lbl=Label(left_frame,image=self.photoimg_img)
        f_lbl.place(x=0,y=0,width=720,height=130)

        #current course
        left_in_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="CURRENT COURSE DETAIL",font=("time new raman",12,"bold"))
        left_in_frame.place(x=5,y=130,width=700,height=125)

        # department 
        dep_label=Label(left_in_frame,text="Department :",font=("time new raman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo = ttk.Combobox(left_in_frame, textvariable=self.var_dep,font=("time new raman",12,"bold"),state="readonly",width=17)
        dep_combo["values"]=("Select Department","IT","Civil","Mechanical")
        dep_combo.current(0) 
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # course 
        course_label=Label(left_in_frame,text="Course :",font=("time new raman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo = ttk.Combobox(left_in_frame,textvariable=self.var_course,font=("time new raman",12,"bold"),state="readonly",width=17)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0) 
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # year 

        year_label=Label(left_in_frame,text="Year :",font=("time new raman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo = ttk.Combobox(left_in_frame,textvariable=self.var_year,font=("time new raman",12,"bold"),state="read",width=17)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0) 
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # semester

        sem_label=Label(left_in_frame,text="Semester :",font=("time new raman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo = ttk.Combobox(left_in_frame,textvariable=self.var_semester,font=("time new raman",12,"bold"),state="read",width=17)
        sem_combo["values"]=("Select Semester","semester-I","semester-II","semester-III","semester-IV","semester-V","semester-VI","semester-VII","semester-VIII")
        sem_combo.current(0) 
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class stusent information
        left_class_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="COURSE DETAILS ",font=("time new raman",12,"bold"))
        left_class_frame.place(x=5,y=260,width=700,height=290)

        #student details entry

        #student id
        student_label0=Label(left_class_frame,text="Student Id :",font=("time new raman",12,"bold"),bg="white")
        student_label0.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        student_entry0=ttk.Entry(left_class_frame,textvariable=self.va_std_id,width=20,font=("time new raman",12,"bold"))
        student_entry0.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        student_label1=Label(left_class_frame,text="Student Name :",font=("time new raman",12,"bold"),bg="white")
        student_label1.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_entry1=ttk.Entry(left_class_frame,textvariable=self.var_name,width=20,font=("time new raman",12,"bold"))
        student_entry1.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #Batch
        student_label2=Label(left_class_frame,text="Batch :",font=("time new raman",12,"bold"),bg="white")
        student_label2.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        student_entry2=ttk.Entry(left_class_frame,textvariable=self.var_div,width=20,font=("time new raman",12,"bold"))
        student_entry2.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #Roll.No
        student_label3=Label(left_class_frame,text="Roll No :",font=("time new raman",12,"bold"),bg="white")
        student_label3.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        student_entry3=ttk.Entry(left_class_frame,textvariable=self.var_roll,width=20,font=("time new raman",12,"bold"))
        student_entry3.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #Gender
        student_label4=Label(left_class_frame,text="Gender :",font=("time new raman",12,"bold"),bg="white")
        student_label4.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        student_entry4=ttk.Entry(left_class_frame,textvariable=self.var_gender,width=20,font=("time new raman",12,"bold"))
        student_entry4.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #DOB
        student_label5=Label(left_class_frame,text="DOB :",font=("time new raman",12,"bold"),bg="white")
        student_label5.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        student_entry6=ttk.Entry(left_class_frame,textvariable=self.var_dob,width=20,font=("time new raman",12,"bold"))
        student_entry6.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #Email
        student_label7=Label(left_class_frame,text="Email :",font=("time new raman",12,"bold"),bg="white")
        student_label7.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        student_entry7=ttk.Entry(left_class_frame,textvariable=self.var_email,width=20,font=("time new raman",12,"bold"))
        student_entry7.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        #Phone No
        student_label8=Label(left_class_frame,text="Phone No :",font=("time new raman",12,"bold"),bg="white")
        student_label8.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        student_entry8=ttk.Entry(left_class_frame,textvariable=self.var_phone,width=20,font=("time new raman",12,"bold"))
        student_entry8.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #Address
        student_label9=Label(left_class_frame,text="Address :",font=("time new raman",12,"bold"),bg="white")
        student_label9.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        student_entry9=ttk.Entry(left_class_frame,textvariable=self.var_address,width=20,font=("time new raman",12,"bold"))
        student_entry9.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        #Teacher
        student_label10=Label(left_class_frame,text="Teachers Name :",font=("time new raman",12,"bold"),bg="white")
        student_label10.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        student_entry10=ttk.Entry(left_class_frame,textvariable=self.var_teacher,width=20,font=("time new raman",12,"bold"))
        student_entry10.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio button
        self.var_radio1=StringVar()
        radio_button = ttk.Radiobutton(left_class_frame,variable=self.var_radio1, text="Take Photo Sample", value="yes")
        radio_button.grid(row=6,column=0)
        
        self.var_radio2=StringVar()
        radio_button2 = ttk.Radiobutton(left_class_frame,variable=self.var_radio1, text="No Photo Sample", value="no")
        radio_button2.grid(row=6,column=2)

        #button frame 
        btn_frame = Frame(left_class_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=2,y=200,width=685,height=30)

        #save button
        save_btn=Button(btn_frame,text="SAVE",command=self.add_data,width=17,font=("time new raman",12,"bold"),bg="black",fg="orange")
        save_btn.grid(row=0,column=0,)

        #update button
        update_btn=Button(btn_frame,text="UPDATE",command=self.update_data,font=("time new raman",12,"bold"),bg="black",fg="orange",width=16)
        update_btn.grid(row=0,column=1,)

        #delete button
        delete_btn=Button(btn_frame,text="DELETE",command=self.delete_data,font=("time new raman",12,"bold"),bg="black",fg="orange",width=16)
        delete_btn.grid(row=0,column=2,)

        #reset button
        rest_btn=Button(btn_frame,text="RESET",command=self.reset_data,font=("time new raman",12,"bold"),bg="black",fg="orange",width=16)
        rest_btn.grid(row=0,column=3,)

        #button frame 
        btn_frame1 = Frame(left_class_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=2,y=230,width=685,height=30)

        #take photo button
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="TAKE PHOTO",font=("time new raman",12,"bold"),bg="black",fg="orange",width=35)
        take_photo_btn.grid(row=1,column=1,)

        #update photo button
        update_photo_btn=Button(btn_frame1,text="UPDATE PHOTO",font=("time new raman",12,"bold"),bg="black",fg="orange",width=35)
        update_photo_btn.grid(row=1,column=2,)

        # right label frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT RECODE",font=("time new raman",12,"bold"))
        right_frame.place(x=740,y=10,width=740,height=580)

        rimg_img=Image.open(r"C:\Users\Alok Chaurasiya\OneDrive\Desktop\face recognition systen\face project inages\f11.jpg")
        rimg_img=rimg_img.resize((740,130),Image.ANTIALIAS)
        self.photoimg_rimg=ImageTk.PhotoImage(rimg_img)

        r_lbl=Label(right_frame,image=self.photoimg_rimg)
        r_lbl.place(x=0,y=0,width=740,height=130)

        #==== search system======
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="RECODE DETAILS",font=("time new raman",12,"bold"))
        search_frame.place(x=5,y=130,width=730,height=60)

        search_label9=Label(search_frame,text="SEARCH BY:",font=("time new raman",12,"bold"),bg="orange",fg="yellow",width=15)
        search_label9.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo = ttk.Combobox(left_in_frame,font=("time new raman",12,"bold"),state="read",width=20)
        search_combo["values"]=("select","roll-no","phone_no")
        search_combo.current(0) 
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,font=("time new raman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="SEARCH",font=("time new raman",12,"bold"),bg="black",fg="orange",width=16)
        search_btn.grid(row=0,column=3,padx=4)

        search_btn2=Button(search_frame,text="SHOW ALL",font=("time new raman",12,"bold"),bg="black",fg="orange",width=16)
        search_btn2.grid(row=0,column=4,padx=4)

        #table frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=200,width=730,height=350)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","dob","email","roll","gender","phone",'address',"teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

    
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep" ,width=100)
        self.student_table.column("course" ,width=100)
        self.student_table.column("year" ,width=100)
        self.student_table.column("sem" ,width=100)
        self.student_table.column("id" ,width=100)
        self.student_table.column("name" ,width=100)
        self.student_table.column("roll" ,width=100)
        self.student_table.column("gender" ,width=100)
        self.student_table.column("div" ,width=100)
        self.student_table.column("dob" ,width=100)
        self.student_table.column("email" ,width=100)
        self.student_table.column("phone" ,width=100)
        self.student_table.column("address" ,width=100)
        self.student_table.column("teacher" ,width=100)
        self.student_table.column("photo" ,width=150)

        self.student_table.pack(fill=BOTH ,expand=1) 
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fatch_data()
    
    #==============Function Decleartion===========================

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required" ,parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost" ,username="root" ,password="student" ,database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("inster into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.va_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                                    
                                                                                                        ))
                conn.commit() 
                self.fatch_data()
                conn.close()
                messagebox.showinfo("Success" ,"SUCCESSFULLY" , parent =self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent =self.root)


    #==============fetch data==============================================

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost" ,username="root" ,password="student" ,database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
            conn.close()

    #==================Get cursor============================================
    
    def get_cursor(self ,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

#=============Update data=====================================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required" ,parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to upadte this student details", parent= self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost" ,username="root" ,password="student" ,database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s.Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where student_id=%s",(
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.va_std_id.get(),
                                                                                                                                                                                 ))
                else: 
                    if not update:
                        return
                messagebox.showinfo("Success" ,"student details Upadte Successfully " ,parent=self.root)
                conn.commit()
                self.fatch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #=========Delete Data===================================
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student id must be requried",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do you want this delete student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost" ,username="root" ,password="student" ,database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    conn.commit()
                    self.fatch_data()
                    conn.close()
                    messagebox.showinfo("Delete","Successfully Deleted",parent=self.root)
            except Exception as es:
               messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #================Reset=======================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

#===============Take Photo===================================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required" ,parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost" ,username="root" ,password="student" ,database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where student_id=%s",(
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.va_std_id.get()==id+1
                                                                                                                                                                            ))
                conn.commit()
                self.fatch_data()
                self.reset_data()
                conn.close()
            

#===============load predifine data on face detection on opencv==============
           
                face_classifier=cv2.CascadeClassifier("tempCodeRunnerFile.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1,3,5)

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Genreting DataSet Complete!!!")
                
            except Exception as es:
                 messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)





        
    

if __name__=="__main__":
    root=Tk()
    obj =student(root)
    root.mainloop()