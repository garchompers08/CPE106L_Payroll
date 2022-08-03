
import string
from tkinter import PhotoImage
import tkinter as tk
from tkinter import *
import sqlite3
#from tkinter import messagebox

my_path = "CPE106L_Payroll\ProjDB.db"
my_conn = sqlite3.connect(my_path)
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

#setting entInfo
def entInfo():
    root.destroy()
    import entInfo


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
brandLabel = tk.Label(root, text="Employee Info", font="montserrat 16", bg="gray17", fg="white")
brandLabel.place(x=70, y=50)

brandLabel2 = tk.Label(root, text="Enter Name", font="montserrat 11", bg="gray17", fg="white")
brandLabel2.place(x=70, y=110)

entryName = tk.Entry(root, font = ("montserrat 11"), width = 34)
entryName.place(x=70, y=140)

searchBtn = tk.Button(root, text = "Search", bg=color["orange"], command=lambda: emp_details(entryName.get()))
searchBtn.place(x=180, y=170)

brandLabel3 = tk.Label(root, text="Employee Info", font="montserrat 11", bg="gray17", fg="white")


def emp_details(var):
    
    cursor = my_conn.cursor()
    sql_select_info = """SELECT * from Employee where firstname = ?"""
    cursor.execute(sql_select_info,(var,))
    record = cursor.fetchall()
    for employee in cursor: 
        for j in range(len(employee)):
            e = Entry(root, width=10, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, employee[j])
        i=i+1
    cursor.close()
    

"""
def emp_details(firstname):
    try: 
        val = string(firstname)
        try:
            my_data = (val,)
            q = "SELECT * FROM Employee WHERE firstname =?"
            my_cursor = my_conn.execute(q, my_data)
            data_row = my_cursor.fetchone()
            my_str.set(data_row)
        except sqlite3.Error as my_error:
            print("error: ", my_error)
    except:
        my_str.set("Check input")
"""


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