from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 
from tkinter import messagebox
import mysql.connector

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
        b2 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2")
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

            


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
