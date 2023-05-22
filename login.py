from tkinter import *
from tkinter import ttk
import mysql
from PIL import Image,ImageTk
from tkinter import messagebox


def main():
   win=Tk()
   app=Login_window(win)
   win.mainloop()


class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
            
        self.bg=ImageTk.PhotoImage(r"face project inages\Background1.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="black")
        frame.place(x=618,y=170,width=340,height=450)
        
        img1=Image.open(r"face project inages\login11.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimage=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimage.place(x=730,y=175,width=100,height=1000)
        
        get_str=Label(frame,text="get started", font=("time new roman",20,"bold"),fg="while",bg="black")
        get_str.place(x=70,y=155)
        
        #Label
        username=lbl=Label(frame,text="Username",font=("time new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)
        
        password=lbl=Label(frame,text="Username",font=("time new roman",15,"bold"),fg="white",bg="black")
        password.place(x=225,y=270)
        self.txtuser=ttk.Entry(frame,font=("time new roman",15,"bold"))
        self.txtuser.place(x=40,y=250,width=270)
        
        #================================= Icon Image ================================================================
        
        img2=Image.open(r"face project inages\login11.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=610,y=323,width=25,height=25)
        
        
        img3=Image.open(r"face project inages\Lock-icon.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3img3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=395,width=25,height=25)
        
        #Login button 
        
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforground="white",activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)
        
        # Register Button
        
        registernbtn=Button(frame,text="New user Register",font=("times new roman",10,"bold"),borderwidth="0",fg="white",bg="black",activeforground="white",activebackground="black")
        registernbtn.place(x=15, y=350, width=160)
        
        # Forget Button
        registernbtn=Button(frame,text="New user Register",command=self.login,font=("times new roman",10,"bold"),borderwidth="0",fg="white",bg="black",activeforgroublack="white",activebackground="black")
        registernbtn.place(x=10, y=370, width=160)
    def register_window(self):
       self.new_window=Toplevel(self.root)
       self.app=Register(self.new_window)
        
    def login(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="rohit" and self.textpass.get()=="123":
                messagebox.showinfo("success","Welcome to my app")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="student",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                
                                                                                        self.txtuser.get(),
                                                                                        self.txt_new_pass.get()   
                                                                                      ))
            
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=""(self.new_window)
                else:
                    if not open_main:
                       return
            conn.commit()
            conn.close()

#======================================  Reset Password ==============================================

    def reset_pass(self):
        if self.combo_security_Q.get()=="":
           messagebox.showerror("Error","Select Security Qustion",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_new_pass.get()=="":
            messagebox.showerror("Error","Please Enter the new Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="student",database="mydata")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security)
            my_cursor.execute(qury,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer",parent=self.root2)
            else:
                query=("Update register set password=%s where email=%s")
                value(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, Please login new password",parent=self.root2)
                self.root2.destroy()
        
   #=======================================  Forget Password Window ============================================     
        
    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="student",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)
            
            if row==None:
                messagebox.showerror("My Error","Please ernter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                security_Q=Label(Frame,text="Select security Qustion",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)
                
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your College name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)
                
                
                Security_A=Label(Frame,text="security Answer",font=("times new roman",15))
                Security_A.place(x=50,y=150)
                
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=100,width=250)
                
                new_password=Label(Frame,text="New Password",font=("times new roman",15),fg="white",bg="black")
                new_password.place(x=50,y=250)
                
                self.txt_new_pass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_new_pass.place(x=50,y=250,width=250)
                
                btn=Button(self.root2,text="Reset",font=("times new roman",15),fg="whitw",bg="green")
                btn.place(x=100,y=290)
            
            
            

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
        
        confirm_pswd=Label(Frame,Text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
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
        b1=Button(Frame,image=self.photoimage,command=self.return_login,borderwidth=0,cursor="hand2")
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
                conn=mysql.connector.connect(host="localhost",user="root",password="student",database="myData")
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
            
        def return_login(self):
            self.root.destroy() 
                
            
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    app=Login_window(root)
    root.mainloop()
