from tkinter import PhotoImage
import tkinter as tk
from tkinter import *


# dictionary of colors:
color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}

# setting root window:
root = tk.Tk()
root.title("Tkinter Navbar")
root.config(bg="gray17")
root.geometry("400x600+850+50")

# setting switch state:
btnState = False

# loading Navbar icon image:
navIcon = PhotoImage(file="CPE106L_Payroll\menu.png")
closeIcon = PhotoImage(file="CPE106L_Payroll\menu.png")

#setting dashboard
def dashboardUI():
    root.destroy()
    import dashboard

#setting entInfo
def entInfo():
    root.destroy()
    import entInfo

#setting empInfo
def empInfo():
    root.destroy()
    import empInfo

#setting addInfo
def addInfo():
    root.destroy()
    import addInfo

#setting payEmp
def payEmp():
    root.destroy()
    import payEmp


# setting switch function:
def switch():
    global btnState
    if btnState is True:
        # create animated Navbar closing:
        for x in range(301):
            navRoot.place(x=-x, y=0)
            topFrame.update()

        # resetting widget colors:
        brandLabel.config(bg="gray17", fg="white")
        homeLabel.config(bg=color["orange"])
        topFrame.config(bg=color["orange"])
        root.config(bg="gray17")

        # turning button OFF:
        btnState = False
    else:
        # make root dim:
        brandLabel.config(bg=color["nero"], fg="#5F5A33")
        homeLabel.config(bg=color["nero"])
        topFrame.config(bg=color["nero"])
        root.config(bg=color["nero"])

        # created animated Navbar opening:
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True

# top Navigation bar:
topFrame = tk.Frame(root, bg=color["orange"])
topFrame.pack(side="top", fill=tk.X)

# Header label text:
homeLabel = tk.Label(topFrame, text="Payroll Management System for SME's ", font="Montserrat 8", bg=color["orange"], fg="gray17", height=2, padx=20)
homeLabel.pack(side="right")

# Main label text:
brandLabel = tk.Label(root, text="Pay Employee", font="montserrat 30", bg="gray17", fg="white")
brandLabel.place(x=100, y=50)


# Navbar button:
navbarBtn = tk.Button(topFrame, image=navIcon, bg=color["orange"], activebackground=color["orange"], bd=0, padx=20, command=switch)
navbarBtn.place(x=10, y=10)

# setting Navbar frame:
navRoot = tk.Frame(root, bg="gray17", height=1000, width=300)
navRoot.place(x=-300, y=0)
tk.Label(navRoot, font="Bahnschrift 15", bg=color["orange"], fg="black", height=2, width=300, padx=20).place(x=0, y=0)

# set y-coordinate of Navbar widgets:
y = 80
# option in the navbar:
options = ["Payroll Management System", "All Employee", "Employee Info", "Enter Info", "Pay Employee"]
# Navbar Option Buttons:

PMS=tk.Button(navRoot, text="Payroll Management System", font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="white", bd=0, command=dashboardUI).place(x=25, y=y+40)
Emp=tk.Button(navRoot, text="All Employee", font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="white", bd=0, command=empInfo).place(x=25, y=y+80)
Inf=tk.Button(navRoot, text="Employee Info", font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="white", bd=0, command=addInfo).place(x=25, y=y+120)
EnterInfo=tk.Button(navRoot, text="Enter info of Employee", font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="white", bd=0, command=entInfo).place(x=25, y=y+160)
Pay=tk.Button(navRoot, text="Pay Employee", font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="white", bd=0, command=payEmp).place(x=25, y=y+200)





# Navbar Close Button:
closeBtn = tk.Button(navRoot, image=closeIcon, bg=color["orange"], activebackground=color["orange"], bd=0, command=switch)
closeBtn.place(x=250, y=10)

# window in mainloop:
root.mainloop()