from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import *
import pymysql
from tkinter import messagebox

class Login_window:
    def __init__(self, root):
        self.root=root
        self.root.title("Login Form")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        #________Background colours
        left_lbl=Label(self.root,bg="lightgray",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl = Label(self.root, bg="lightgray", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)
        #_________Frames
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)

        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)

        email=Label(login_frame,text="EMAIL ADDRESS",font=("times new roman",18,"bold"),bg="white",fg="green").place(x=250,y=150)
        self.txt_email = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=250, y=180,width=350,height=35)

        pass_ = Label(login_frame, text="PASSWORD", font=("times new roman", 18, "bold"), bg="white",fg="green").place(x=250, y=250)
        self.txt_pass_ = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_pass_.place(x=250, y=280, width=350, height=35)

        btn_reg=Button(login_frame,text="Register New Account?",command=self.register_window,font=("times new roman",14),bg="white",cursor="hand2",bd=0,fg="#B00857").place(x=250,y=320)
        btn_login = Button(login_frame, text="LOGIN",command=self.login, font=("times new roman", 20,"bold"), bg="#B00857",cursor="hand2", fg="white").place(x=250, y=380,width=180,height=40)

        #__________clock
        self.lbl=Label(self.root,text="\nFLAPPY BIRD",font=("Book Antiqua",25,"bold"),compound=BOTTOM,fg="white",bg="#081923",bd=0)
        self.lbl.place(x=90,y=120,height=450,width=350)
        self.working()

    def register_window(self):
        self.root.destroy()
        import register

    def login(self):
            if self.txt_email.get()=="" or self.txt_pass_.get()=="":
                messagebox.showerror("Error","All Fields are Required",parent=self.root)
            else:
                try:
                    con=pymysql.connect(host="localhost",user="root",password="",database="loginpage")
                    cur=con.cursor()
                    cur.execute("select * from users where email=%s and password=%s",(self.txt_email.get(),self.txt_pass_.get()))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error", "INVALID EMAIL & PASSWORD", parent=self.root)

                    else:
                        messagebox.showinfo("Success", "Welcome", parent=self.root)
                        self.root.destroy()
                        import main
                    con.close()
                except Exception as es:
                    messagebox.showerror("Error", f"Error Due to:{str(es)}", parent=self.root)



    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)

        #_________for clock Image
        bg=Image.open("login/c.png")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))


        #____________Hour Line Image

        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)

        # ____________Min Line Image
        draw.line((origin, 200 + 80 * sin(radians(min_)), 200 - 80 * cos(radians(min_))), fill="white", width=3)

        # ____________Sec Line Image

        draw.line((origin, 200 + 100 * sin(radians(sec_)), 200 - 100 * cos(radians(sec_))), fill="yellow", width=2)
        draw.ellipse((195, 195, 210, 210), fill="#1AD5D5")
        clock.save("login/clock_new.png")

    def working(self):
        h=datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360

        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="login/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)


root=Tk()
obj=Login_window(root)
root.mainloop()