from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__ (self,root):
        self.root=root 
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        # text variable 
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_email=StringVar()
        self.var_contact=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_question=StringVar()
        self.var_answer=StringVar()
        
        # bg image 
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Dhruv Rana\OneDrive\Desktop\python_sql\image\register1.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        # left image 
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\Dhruv Rana\OneDrive\Desktop\python_sql\image\image5.jpg")
        bg_lbl=Label(self.root,image=self.bg1)
        bg_lbl.place(x=50,y=100,width=470,height=550)
        
        # main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)
        
        # Label and entry
        fname=Label(frame,text="First Name",font=("times new roman",16,"bold"),bg="white")
        fname.place(x=50,y=100)
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",16,"bold"))
        fname_entry.place(x=50,y=130,width=250)
        
        l_name=Label(frame,text="Last Name",font=("times new roman",16,"bold"),bg="white")
        l_name.place(x=378,y=100)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",16))
        self.txt_lname.place(x=378,y=130,width=250)
        
        email=Label(frame,text="Email",font=("times new roman",16,"bold"),bg="white")
        email.place(x=50,y=165)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",16))
        self.txt_email.place(x=50,y=195,width=250)
        
        contact=Label(frame,text="Contact No",font=("times new roman",16,"bold"),bg="white")
        contact.place(x=378,y=165)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",16))
        self.txt_contact.place(x=378,y=195,width=250)
        
        password=Label(frame,text="Password",font=("times new roman",16,"bold"),bg="white")
        password.place(x=50,y=230)
        
        self.txt_password=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",16))
        self.txt_password.place(x=50,y=260,width=250)
        
        c_password=Label(frame,text="Confirm Password",font=("times new roman",16,"bold"),bg="white")
        c_password.place(x=378,y=230)
        
        self.txt_password=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",16))
        self.txt_password.place(x=378,y=260,width=250)
        
        question=Label(frame,text="Select Security Question",font=("times new roman",16,"bold"),bg="white")
        question.place(x=50,y=300)
        
        self.combo_security=ttk.Combobox(frame,textvariable=self.var_question,font=("times new roman",16),state="readonly")
        self.com
