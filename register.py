from logging import root
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
   
   

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        #=============== Variable =================
        
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        #======================= Background Images==================================================
        
        self.bg=ImageTk.PhotoImage(r"face project inages\bg2.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        #====================== Left images ======================================================
        
        self.bg1=ImageTk.PhotoImage(r"face project inages\bg2.png")
        bg_lbl=Label(self.root,image=self.bg1)
        bg_lbl.place(x=0,y=0,relwidth=470,relheight=550)
        
        Frame=Frame(self.root,bg="white")
        Frame.place(x=520,y=100,width=800,height=550)
        
        #============= Main Frame ============================
        
        Frame=Frame(self.root,bg="white")
        Frame.place(x=520,y=100,width=800,height=550)
        
        register_lbl=Label(Frame,text="REGISTER HERE",font=("times of roman",25,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)
        
        #================  Label and entry ============================
        #.............. Row1
        
        Frame=Label(Frame,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        Frame_entry.place(x=50,y=100)
        
        Frame_entry=ttk.Entry(Frame,font=("times new roman"))
        Frame_entry,Place(x=50,y=130,width=250)
        
        l_name=Label(Frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)
        
        self.text_lname=ttk.Entry(Frame,textvariable=self.var_fname,font=("times new roman",15))
        self.text_lname.place(x=370,y=250)
        
        #............... Row2 .........
        
        contact=Label(Frame,text="contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(Frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(Frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(Frame,textvariable=self.var_email,font=("times new roman",15))  
        self.txt_email.place(x=370,y=250)     
        
        #.......................  Row 3.....................
        
        security_Q=Label(Frame,text="Select security Qustion",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(Frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"))
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your College name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        
        
        Security_A=Label(Frame,text="security Answer",font=("times new roman",15))
        Security_A.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(Frame,textvariable=self.var_SecurityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)
        
        #..................  Row 4 ......................
        
        pswd=Label(Frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)
        
        self.txt_pswd-ttk.Entry(Frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        confirm_pswd=Label(Frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)
        
        self.txt_confirm_pswd=ttk.Entry(Frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)
        
        #============= Check Button ===================================
        self.var_check=IntVar
        self.Checkbtn=Checkbutton(Frame,text="I agree term & condition",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.Checkbtn.place(x=50,y=.380)
        
        #==================== Button =================================
        img=Image.open(r"face project inages\Register-Now.png")
        img=img.resize((100,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(Frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=470,width=300)
        
        img1=Image.open(r"face project inages\login-button.png")
        img1=img1.resize((100,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(Frame,image=self.photoimage,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=470,width=200)
        
        
        #=======================   Function Declertation ==================
        
        def register_data(self):
            if self.var_fname.get=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
               messagebox.showerror("Error","All field are required")
            elif self.var_pass.get()!=self.var_confpass.get():
               messagebox.showerror("error","password & confirm password must be same")
            elif self.var_check.get()==0:
               messagebox.showerror("Error","Please agree our term & condition")
            else:
                conn=mysql.connector.connect(host="localhost",user="root",password="123456",database="mydata")
                my_cursor=conn.cursor()
                query=("select * from Register where email=%s")
                value=(self.var_email.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row!=None:
                   messagebox.showerror("error","User already exist, please try another email")
                else:
                    my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                             self.var_fname.get(),
                                                                                             self.var_lname.get(),
                                                                                             self.var_contact.get(),
                                                                                             self.var_email.get(),
                                                                                             self.var_securityQ.get(),
                                                                                             self.var_securityA.get(),
                                                                                             self.var_pass.get(),
                                                                                          ))
                
                conn.commit()
                conn.close() 
                messagebox.showinfo("success","Register Successfully")                                                                  
            
                
            
    
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()        