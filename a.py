import sqlite3
import tkinter as tk
from tkinter import *

my_conn = sqlite3.connect('CPE106L_Payroll\ProjDB.db')

my_w = tk.Tk()
my_w.geometry("400x250")
r_set= my_conn.execute('SELECT * FROM Employee LIMIT 0,10')
i=0
for employee in r_set:
    for j in range(len(employee)):
        e=tk.Label(my_w, width=10, fg='blue',text= employee[j], anchor='w')
        e.grid(row=i, column=j)
    i=i+1
my_w.mainloop()