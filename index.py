from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk 
from tkinter import messagebox
import mysql.connector


def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Dhruv Rana\OneDrive\Desktop\python_sql\image\image4.jpg")
       
        
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        
        frame = Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        img1=Image.open(r"C:\Users\Dhruv Rana\OneDrive\Desktop\python_sql\image\loginimage.png")
        img1=img1.resize((100,100), Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        get_str=Label(frame,text="Get Started" ,font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95,y=100)
        
        # label
        
        username=lbl=Label(frame, text="username",font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70,y=155)
        
        self.textuser = ttk.Entry (frame, font=("times new roman", 15, "bold"))
        self.textuser.place(x=40,y=180,width=270)
        
        password=Label(frame, text="password",font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70,y=255)
        # password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="red")
        # password.place(x=50, y=120)
        
        self.textpass = ttk.Entry (frame, font=("times new roman", 15, "bold"))
        self.textpass.place(x=40,y=280,width=270)
        
        
        # icon images 
        
        img2=Image.open(r"C:\Users\Dhruv Rana\OneDrive\Desktop\python_sql\image\icon5.png")
        img2=img2.resize((30,30), Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1 = Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=30,height=25)
        
        
        img3=Image.open(r"C:\Users\Dhruv Rana\OneDrive\Desktop\python_sql\image\pass.png")
        img3=img3.resize((30,30), Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1 = Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=420,width=30,height=25)
        
        # login button
        
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman", 15, "bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=320,width=120,height=35)

        # register button
        registerbtn=Button(frame,text="Register",command=self.register_window,font=("times new roman", 15, "bold"),bd=3,borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=20,y=375,width=120,height=35)
                
                
        #  forgot button 
        
        registerbtn=Button(frame,text="Forgot password",command=self.forgot_passworcd_window,font=("times new roman", 15, "bold"),bd=3,borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=190,y=375,width=135)
     
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)   
        
    def login(self):
        if self.textuser.get()=="" or self.textpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.textuser.get()=="Dhruv" and self.textpass.get()=="Ashu":
            messagebox.showinfo("success","welcome to my website")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="mydata")
            cursor = conn.cursor()
            cursor.execute("select * from register where email=%s and password=%s",(
                self.textuser.get(),
                self.textpass.get()
            ))
            
            row=cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & password")
            else:
               messagebox.showinfo("success", "welcome to the system")
            conn.commit()
            conn.close()
            
            
            
            #  set password 
            
            
            
    def reset_pass(self):
        if self.combo_security.get()=="select":
            messagebox.showerror("Error","select the sequrity question")
        elif self.txt_answer.get()=="":
            messagebox.showerror("Error","please enter the answer")
            
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","please enter the new password")
            
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="mydata")
            cursor = conn.cursor() 
            query=("select * from register where email=%s and question=%s and answer=%s")  
            value=(self.textuser.get(),self.combo_security.get(),self.txt_answer.get())
            cursor.execute(query,value)   
            row=cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","enter correct answer")
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.textuser.get())
                cursor.execute(query,value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("info","your password has been reset , please login")
                
            
            
            #  forgot pasword window
            
    def forgot_passworcd_window(self): 
        if self.textuser.get()=="":
            messagebox.showerror("Error","please enter the email address to rest password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="mydata")
            cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.textuser.get(),)
            cursor.execute(query,value)
            row=cursor.fetchone()
            print(row)
            
            if row==None:
                messagebox.showerror("Error","enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x458+618+178")
                
                l=Label(self.root2,text="Forgot Password",font=("times new roman", 20, "bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                question = Label(self.root2, text="Select Security Question", font=("times new roman", 16, "bold"), bg="white")
                question.place(x=50, y=80)
                self.combo_security = ttk.Combobox(self.root2, font=("times new roman", 16), state="readonly")
                self.combo_security["values"] = ("Select", "Your Birth Place", "Your Girlfriend's Name", "Your Friend's Name", "Your Pet's Name")
                self.combo_security.place(x=50, y=110, width=250)
                self.combo_security.current(0)

                # Security Answer
                answer = Label(self.root2, text="Security Answer", font=("times new roman", 16, "bold"), bg="white")
                answer.place(x=50, y=150)
                self.txt_answer = ttk.Entry(self.root2, font=("times new roman", 16))
                self.txt_answer.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New Password", font=("times new roman", 16, "bold"), bg="white")
                new_password.place(x=50, y=220)
                self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 16))
                self.txt_newpass.place(x=50, y=250, width=250)
                
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",16,"bold"),fg="white",bg="green")
                btn.place(x=120,y=300)
                    
            
            
            
class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        # text variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_email = StringVar()
        self.var_contact = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_question = StringVar()
        self.var_answer = StringVar()

        # bg image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Dhruv Rana\OneDrive\Desktop\python_sql\image\register1.png")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # left image
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\Dhruv Rana\OneDrive\Desktop\python_sql\image\image5.jpg")
        bg_lbl = Label(self.root, image=self.bg1)
        bg_lbl.place(x=50, y=100, width=470, height=550)

        # frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)
        
        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)
        
        # Label and Entry for First Name
        fname = Label(frame, text="First Name", font=("times new roman", 16, "bold"), bg="white")
        fname.place(x=50, y=100)
        self.fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 16, "bold"))
        self.fname_entry.place(x=50, y=130, width=250)

        # Last Name
        l_name = Label(frame, text="Last Name", font=("times new roman", 16, "bold"), bg="white")
        l_name.place(x=378, y=100)
        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 16))
        self.txt_lname.place(x=378, y=130, width=250)

        # Email
        email = Label(frame, text="Email", font=("times new roman", 16, "bold"), bg="white")
        email.place(x=50, y=165)
        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 16))
        self.txt_email.place(x=50, y=195, width=250)

        # Contact No
        contact = Label(frame, text="Contact No", font=("times new roman", 16, "bold"), bg="white")
        contact.place(x=378, y=165)
        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 16))
        self.txt_contact.place(x=378, y=195, width=250)

        # Password
        password = Label(frame, text="Password", font=("times new roman", 16, "bold"), bg="white")
        password.place(x=50, y=230)
        self.txt_password = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 16), show="*")
        self.txt_password.place(x=50, y=260, width=250)

        # Confirm Password
        c_password = Label(frame, text="Confirm Password", font=("times new roman", 16, "bold"), bg="white")
        c_password.place(x=378, y=230)
        self.txt_confpassword = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 16), show="*")
        self.txt_confpassword.place(x=378, y=260, width=250)

        # Security Question
        question = Label(frame, text="Select Security Question", font=("times new roman", 16, "bold"), bg="white")
        question.place(x=50, y=300)
        self.combo_security = ttk.Combobox(frame, textvariable=self.var_question, font=("times new roman", 16), state="readonly")
        self.combo_security["values"] = ("Select", "Your Birth Place", "Your Girlfriend's Name", "Your Friend's Name", "Your Pet's Name")
        self.combo_security.place(x=50, y=330, width=250)
        self.combo_security.current(0)

        # Security Answer
        answer = Label(frame, text="Security Answer", font=("times new roman", 16, "bold"), bg="white")
        answer.place(x=378, y=300)
        self.txt_answer = ttk.Entry(frame, textvariable=self.var_answer, font=("times new roman", 16))
        self.txt_answer.place(x=378, y=330, width=250)

        # Check button for agreeing to terms
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions", font=("times new roman", 16, "bold"), bg="white", onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

        # Register Button
        img = Image.open(r"C:\Users\Dhruv Rana\OneDrive\Desktop\python_sql\image\register-button-png-18.png")
        img = img.resize((200, 50), Image.Resampling.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2")
        b1.place(x=10, y=420, width=200)

        # Login Button
        img1 = Image.open(r"C:\Users\Dhruv Rana\OneDrive\Desktop\python_sql\image\pngtree-login-button-png-image_6163957.png")
        img1 = img1.resize((200, 50), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b2 = Button(frame, image=self.photoimage1,command=self.return_login, borderwidth=0, cursor="hand2")
        b2.place(x=378, y=420, width=200)

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_question.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Passwords do not match")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to the terms and conditions")
        else:
            
                # Database connection
                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="mydata")
                cursor = conn.cursor()

                # Insert user data into the database
                query = "INSERT INTO register (fname, lname, email, contact, password, question, answer) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = (self.var_fname.get(), self.var_lname.get(), self.var_email.get(), self.var_contact.get(), self.var_pass.get(), self.var_question.get(), self.var_answer.get())
                cursor.execute(query, values)

                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Registration Successful")
                
                
    def return_login(self):
        self.root.destroy()
        
        
if __name__ == "__main__":
    main()
    root= Tk()
    app = Login_window(root)
    root.mainloop()