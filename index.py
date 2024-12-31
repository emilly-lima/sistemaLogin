from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database

janela = Tk()
janela.title("Login Acess")
janela.geometry("500x300")
janela.configure(background="white") 
janela.resizable(False, False)
janela.iconbitmap(default="icons/favico.ico")

logo = PhotoImage(file="icons/logo.png", width=88, height=148)

Leftframe = Frame(janela, width=170, height=300, bg="#fff9e2", relief="raise")
Leftframe.pack(side=LEFT)

RightFrame = Frame(janela, width=330, height=300, bg="#f6b073", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(Leftframe, image=logo, bg="#fff9e2")
LogoLabel.place(x=41, y=80)

UserLabel = Label(RightFrame, text="Username:", font=("Calibri", 16, "bold"), bg="#f6b073", fg="white")
UserLabel.place(x=10, y=100)

UserEntry = ttk.Entry(RightFrame, width=20, font=("Calibri", 12))
UserEntry.place(x=130, y=105)

PassLabel = Label(RightFrame, text="Password:", font=("Calibri", 16, "bold"), bg="#f6b073", fg="white")
PassLabel.place(x=10, y=150)

PassEntry = ttk.Entry(RightFrame, width=20, show="*", font=("Calibri", 12))
PassEntry.place(x=130, y=155)

ButtonLogin = ttk.Button(RightFrame, text="Login", width=20)
ButtonLogin.place(x=145, y=200)

def Register():
    ButtonLogin.place(x=5000)
    ButtonRegister.place(x=5000)

    UserLabel.place(x=10, y=150)
    UserEntry.place(x=130, y=155)

    PassLabel.place(x=10, y=200)
    PassEntry.place(x=130, y=205)

    NomeLabel = Label(RightFrame, text="Name:", font=("Calibri", 16, "bold"), bg="#f6b073", fg="white")
    NomeLabel.place(x=10, y=50)

    NomeEntry = ttk.Entry(RightFrame, width=20, font=("Calibri", 12))
    NomeEntry.place(x=130, y=55)

    EmailLabel = Label(RightFrame, text="Email:", font=("Calibri", 16, "bold"), bg="#f6b073", fg="white")
    EmailLabel.place(x=10, y=100)

    EmailEntry = ttk.Entry(RightFrame, width=20, font=("Calibri", 12))
    EmailEntry.place(x=130, y=105)

    def RegisterDatabase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        Username = UserEntry.get()
        Password = PassEntry.get()

        database.cursor.execute("""
            INSERT INTO users (Name, Email, Username, Password) VALUES (?, ?, ?, ?)
        """, (Name, Email, Username, Password))
        database.connection.commit()
        messagebox.showinfo(title="Register Info", message="Account Created Successfully")

    Register = ttk.Button(RightFrame, text="Register", width=20, command=RegisterDatabase)
    Register.place(x=145, y=250)

    def BackLogin():
        UserLabel.place(x=5000)
        UserEntry.place(x=5000)
        PassLabel.place(x=5000)
        PassEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)

        UserLabel.place(x=10, y=100)
        UserEntry.place(x=130, y=105)
        PassLabel.place(x=10, y=150)
        PassEntry.place(x=130, y=155)
        ButtonLogin.place(x=145, y=200)
        ButtonRegister.place(x=145, y=230)

    Back = ttk.Button(RightFrame, text="<", width=10, command=BackLogin)
    Back.place(x=10, y=250)

ButtonRegister = ttk.Button(RightFrame, text="Register", width=20, command=Register)
ButtonRegister.place(x=145, y=230)



janela.mainloop()
