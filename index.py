from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk 

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
    
if __name__ == "__main__":
    root= Tk()
    app = Login_window(root)
    root.mainloop()