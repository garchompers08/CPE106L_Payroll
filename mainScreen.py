from tkinter import *
import os

main_screen = Tk()   
main_screen.geometry("300x250") 
main_screen.title("Start Page") 

def loginUI():
    main_screen.destroy()
    import loginUI

def registerUI():
    main_screen.destroy()
    import RegisterUI

def dashboardUI():
    main_screen.destroy()
    import dashboard

Label(text="Choose Login Or Register", bg="grey", width="300", height="2", font=("Calibri", 13)).pack() 
Label(text="").pack() 
Button(main_screen,text="Login", height="2", width="30",command = loginUI).pack() 
Button(main_screen,text="Register", height="2", width="30",command = registerUI).pack()
Button(main_screen,text="Dashboard", height="2", width="30",command = dashboardUI).pack()

main_screen.mainloop() 


