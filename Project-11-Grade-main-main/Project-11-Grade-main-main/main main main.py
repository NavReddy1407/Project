from tkinter import *
from PIL import ImageTk, Image
import customtkinter
import matplotlib.pyplot as plt
from tkcalendar import *
from tkinter import messagebox, Listbox, Scrollbar
import hashlib
import sqlite3
import tkinter as tk
import subprocess


window = Tk()
window.geometry('500x650')
window.config(bg='black')
window.title('FITNESS APP')
window.iconbitmap("icon.ico")
window.resizable(False,False)
window.overrideredirect(True)

def dob_screen(): 
    screen = Toplevel()
    screen.geometry('500x400')
    screen.config(bg='black')
    screen.title('FITNESS APP')
    screen.iconbitmap("icon.ico")
    screen.resizable(False,False)

    cal = Calendar(screen,selectmode='day',year=2023,month=12,day=23)
    cal.pack(pady=20,fill='both', expand=True)

    def grab_date():
        global dates
        display = Label(screen, text=cal.get_date(),fg='white',bg='black',font=('Bahnschrift SemiBold SemiCondensed', 16))
        dates = cal.get_date()
        display.pack()
        

    date_button = Button(screen, text='GET DATE', fg='white', bg='black',font=('Bahnschrift SemiBold SemiCondensed', 18), command=grab_date)
    date_button.pack(pady=10)


def login_screen():

    window.destroy()

    login = Tk()
    login.geometry('600x900')
    login.config(bg='black')
    login.title('FITNESS APP')
    login.iconbitmap("icon.ico")
    login.resizable(False,False)
       
    profiles = Button(login, text='GO TO PROFILES', bg='white', fg='black',font=('Bahnschrift SemiBold SemiCondensed', 24), command=pro)
    profiles.pack(pady = 300)


window.after(3000, login_screen)

def pro():
    def run_another_file():
        # Replace 'another_script.py' with the path to your Python file
        subprocess.run(['python', 'tetsssss.py'])

    # Create the main window
    root = tk.Tk()
    root.title("Run Another Script")

    # Create a button and link it to the run_another_file function
    run_button = tk.Button(root, text=">>>", command=run_another_file)
    run_button.pack(pady=20)




my_pic = Image.open('Logoo.png')
resized = my_pic.resize((500,500))
new_pic = ImageTk.PhotoImage(resized)

logo = Label(window, image=new_pic, bg='black')
logo.pack()






slogan = Label(window,text="FlexZone", fg='white', bg='black', font=('Bahnschrift SemiBold SemiCondensed',50))
slogan.pack()


window.mainloop()


