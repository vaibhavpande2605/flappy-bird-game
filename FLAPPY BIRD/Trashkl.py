login_frame = Frame(self.root, bg="white")
login_frame.place(x=250, y=140, width=800, height=500)

title = Label(login_frame, text="LOGIN HERE", font=("times new roman", 30, "bold"), bg="white", fg="#08A3D2").place(
    x=250, y=50)

email = Label(login_frame, text="EMAIL ADDRESS", font=("times new roman", 18, "bold"), bg="white", fg="green").place(
    x=130, y=150)
self.txt_email = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
self.txt_email.place(x=130, y=180, width=350, height=35)

password = Label(login_frame, text="PASSWORD", font=("times new roman", 18, "bold"), bg="white", fg="green").place(
    x=130, y=250)
self.txt_pass = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
self.txt_pass.place(x=130, y=280, width=350, height=35)

btn_reg = Button(login_frame, text="Register New Account?", font=("times new roman", 14), bg="white", bd=0,
                 fg="#B00857", cursor="hand2").place(x=130, y=320)

btn_login = Button(login_frame, text="Login", command=self.login(), font=("times new roman", 20, "bold"), bg="#B00857",
                   fg="white", cursor="hand2").place(x=130, y=390, width=180, height=40)


def login(self):
    if self.txt_email.get() == "" or self.txt_pass.get() == "":
        messagebox.showerror("Error", "All fields are required", parent=self.root)