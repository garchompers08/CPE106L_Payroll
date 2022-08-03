from tkinter import *


def RegisterUI():
    register_screen = Tk()
    register_screen.title("Register")
    register_screen.geometry("300x400")

    Label(register_screen, text="Please enter your details").pack()
    Label(register_screen, text="").pack()
    Label(register_screen, text="Username").pack()

    username_register_entry = Entry(register_screen, textvariable="username")
    username_register_entry.pack()

    Label(register_screen, text="First Name").pack()
    FN_register_entry = Entry(register_screen, textvariable="First Name")
    FN_register_entry.pack()

    Label(register_screen, text="Last Name").pack()
    LN_register_entry = Entry(register_screen, textvariable="Last Name")
    LN_register_entry.pack()

    Label(register_screen, text="").pack()
    Label(register_screen, text="Password").pack()

    password__login_entry = Entry(register_screen, textvariable="password", show= '*')
    password__login_entry.pack()

    Label(register_screen, text="").pack()
    Label(register_screen, text="Confirm Password").pack()

    password__login_entry = Entry(register_screen, textvariable="Confirmpassword", show= '*')
    password__login_entry.pack()

    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1).pack()
    register_screen.mainloop()

RegisterUI()