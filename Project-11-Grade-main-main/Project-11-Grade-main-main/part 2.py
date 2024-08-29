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

    name = Label(login,text='Enter name:',font=('Bahnschrift SemiBold SemiCondensed', 24), fg = 'white', bg='black')
    name.place(x=200, y=60)

    name_box= Entry(login,width=20, font=('Arial', 15))
    name_box.place(x=170,y=120)

    dob = Label(login,text='Enter date of birth:',font=('Bahnschrift SemiBold SemiCondensed', 24), fg = 'white', bg='black')
    dob.place(x=160, y=240)

    open_cal = next = Button(login, text='OPEN', bg='white', fg='black',font=('Bahnschrift SemiBold SemiCondensed', 14),command=dob_screen)
    open_cal.place(x=410,y=245)


    gender = Label(login,text='Select gender:',font=('Bahnschrift SemiBold SemiCondensed', 24), fg = 'white', bg='black')
    gender.place(x=190, y=350)

    r = IntVar()
    Radiobutton(login, text='Male', variable=r,value=1,font=('Bahnschrift SemiBold SemiCondensed', 16)).place(x=250, y=400)
    Radiobutton(login, text='Female', variable=r,value=2,font=('Bahnschrift SemiBold SemiCondensed', 16)).place(x=240, y=440)   


    next = Button(login, text='>>>', bg='black', fg='white', command=open)
    next.place(x=500,y=640)

window.after(3000, login_screen)


def open():
    options = Toplevel()
    options.geometry('600x900')
    options.config(bg='black')
    options.title('FITNESS APP')
    options.iconbitmap("icon.ico")
    options.resizable(False,False)

    BMI_button = Button(options, text='BMI', bg='black', fg='white', height=1, width=15, font=('Bahnschrift SemiBold SemiCondensed',30), command=bmi_window)
    BMI_button.place(x=150, y=50)
    
    Health_button = Button(options,text='Health Score', bg='black', fg='white', height=1, width=15, font=('Bahnschrift SemiBold SemiCondensed',30), command=health_start)
    Health_button.place(x=150, y=200)

    Sugar_levels = Button(options,text='Sugar level tracker', bg='black', fg='white', height=1, width=16, font=('Bahnschrift SemiBold SemiCondensed',30), command=sugar_win)
    Sugar_levels.place(x=140, y=350)

    workouts_button = Button(options,text='Workouts', bg='black', fg='white', height=1, width=16, font=('Bahnschrift SemiBold SemiCondensed',30),command=workout_win)
    workouts_button.place(x=140, y=500)

    close = Button(options, text='<<<',bg='black', fg='white', command=options.destroy)
    close.place(x=500,y=640)
    

def bmi_window():
    calc = Toplevel()
    calc.geometry('600x900')
    calc.config(bg='black')
    calc.title('FITNESS APP')
    calc.iconbitmap("icon.ico")
    calc.resizable(False,False)

    top = Label(calc,text='BMI CALCULATOR' ,font=('Bahnschrift SemiBold SemiCondensed', 40), fg = 'white', bg='black', width=28, height=1)
    top.pack()

    height_label = Label(calc,font=('Bahnschrift SemiBold SemiCondensed', 30), fg = 'white', bg='black', width=17, height=4)
    height_label.place(x=20, y=60)

    height_text = Label(calc,text='HEIGHT (CM)' ,font=('Bahnschrift SemiBold SemiCondensed', 30), fg = 'white', bg='black', width=10, height=1)
    height_text.place(x=180, y=100)

    weight_label = Label(calc ,font=('Bahnschrift SemiBold SemiCondensed', 30,'bold'), fg = 'white', bg='black', width=17, height=4)
    weight_label.place(x=20, y=210)

    weight_text = Label(calc,text='WEIGHT (KG)' ,font=('Bahnschrift SemiBold SemiCondensed', 30,'bold'), fg = 'white', bg='black', width=10, height=1)
    weight_text.place(x=180, y=280)

    height = StringVar()
    weight = StringVar()

    
    height_value = IntVar()
    weight_value = IntVar()

    txt = StringVar()

    def get_height_value():
        return height_value.get()

    def slider1(event):
        return height.set(get_height_value())
    
    def get_weight_value():
        return weight_value.get()

    def slider2(event):
        return weight.set(get_weight_value())

    height_entry = customtkinter.CTkEntry(calc, textvariable=height, bg_color='black',fg_color='white',border_width=0, text_color='black', font=customtkinter.CTkFont(family='Bahnschrift SemiBold SemiCondensed',size=20))
    height_entry.place(x=220, y=170)

    weight_entry = customtkinter.CTkEntry(calc, textvariable=weight, bg_color='black',fg_color='white',border_width=0, text_color='black', font=customtkinter.CTkFont(family='Bahnschrift SemiBold SemiCondensed',size=20))
    weight_entry.place(x=220, y=350)


    height_slider = customtkinter.CTkSlider(calc, variable=height_value,from_=0, to=300, width=260, bg_color='black', fg_color='white', button_hover_color='yellow', command=slider1)
    height_slider.place(x=150, y=220)

    weight_slider = customtkinter.CTkSlider(calc,variable=weight_value,from_=0, to=120, width=260, bg_color='black', fg_color='white', button_hover_color='yellow', command=slider2)
    weight_slider.place(x=150, y=400)

    def BMI():
        cm = int(height_entry.get())
        m = (cm/100)*(cm/100)
        w = int(weight_entry.get())
        bmi = float(format(w/m,'.2f'))
        if(bmi<=18.5):
            txt.set('Underweight')
        elif(bmi<=24.5):
            txt.set('Normal')
        elif(bmi<=29.9):
            txt.set('Overweight')
        elif(bmi<=34.9):
            txt.set('Obese I')
        elif(bmi<=39.9):
            txt.set('Obese II')
        else:
            txt.set('Obese III')


        result1_label = customtkinter.CTkLabel(calc, text=f'{bmi}',font=customtkinter.CTkFont(family='Arial',size=30), text_color='white')
        result1_label.place(x=250, y=580)

        result2_label = customtkinter.CTkLabel(calc, textvariable=txt,font=customtkinter.CTkFont(family='Bahnschrift SemiBold SemiCondensed',size=30), text_color='white')
        result2_label.place(x=235, y=630)

    calc_button = customtkinter.CTkButton(calc,text='CALCULATE', command=BMI, width=170, height=50,hover_color='white', fg_color='white',text_color='black',font=customtkinter.CTkFont(family='Bahnschrift SemiBold SemiCondensed',size=20))
    calc_button.place(x=200, y= 500)

    close = Button(calc, text='<<<',bg='black', fg='white', command=calc.destroy)
    close.place(x=500,y=640)



def health_start():
    hs_calc = Toplevel()
    hs_calc.geometry('600x900')
    hs_calc.config(bg='black')
    hs_calc.title('FITNESS APP')
    hs_calc.iconbitmap("icon.ico")
    hs_calc.resizable(False,False)

    top = Label(hs_calc,text='HEALTH SCORE CALCULATOR' ,font=('Bahnschrift SemiBold SemiCondensed', 40), fg = 'white', bg='black', width=28, height=1)
    top.pack()

    def hs_entry():
        steps = int(e1.get())
        cal = int(e2.get())
        age = int(e3.get())

        if age<13:
            m1 = "Too young."

        elif 13 <= age < 60:
            step_score = steps/200
            cal_score = cal/50
            scr_count = step_score+cal_score
            m1 = scr_count

            if m1 <=20:
                m3 = Label(hs_calc, text='You need to get some exercise NOW!!',font=('Arial',16),fg='white', bg='black')
                m3.place(x=130,y=670)

            elif 20 < scr_count <= 40:
                m4 = Label(hs_calc, text="It's time for you to be more active",font=('Arial',16),fg='white', bg='black')
                m4.place(x=140,y=670)

            elif 40 < scr_count <= 60:
                m5 = Label(hs_calc, text="Keep going...you are making good progress",font=('Arial',16),fg='white', bg='black')
                m5.place(x=100,y=670)

            elif 60 < scr_count <= 80:
                m6 = Label(hs_calc, text="Good work...push for more",font=('Arial',16),fg='white', bg='black')
                m6.place(x=170,y=670)

            elif 80 < scr_count <= 90:
                m7 = Label(hs_calc, text="You are an athlete....go for 100%",font=('Arial',16),fg='white', bg='black')
                m7.place(x=140,y=670)

            elif 90 < scr_count < 100:
                m8 = Label(hs_calc, text="You are a beast...keep pushing!!!",font=('Arial',16),fg='white', bg='black')
                m8.place(x=140,y=670)

            elif scr_count>=100:
                m9 = Label(hs_calc, text="""You have done it...good work...
                           keep this up and you will be in the top 1%""",font=('Arial',16),fg='white', bg='black')
                m9.place(y=660)  
                        
                

        elif age > 60:
            step_score = steps/160
            cal_score = cal/50
            scr_count = step_score+cal_score
            m1 = scr_count
            m2 = Label(hs_calc, text='''
            You dont need this health score.
            Just make sure to stay active and go on regular walks.''',
            font=('Arial', 14), fg='white', bg='black')
            m2.place(y=630)


        score_text = Label(hs_calc,text='Your score is', font=('Bahnschrift SemiBold SemiCondensed',24),fg='white',bg='black')
        score_text.place(x=210, y=580)


        score = Label(hs_calc, text=m1, font=('Arial',20), fg='white', bg='black')
        score.place(x=255, y=620)

    steps_label = Label(hs_calc, text='Enter steps',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    steps_label.place(x=130,y=80)
    e1 = Entry(hs_calc,width=30, font=('Arial', 15))
    e1.place(x=130, y=130)


    cal_label = Label(hs_calc, text='Enter calories burned',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    cal_label.place(x=130,y=230)
    e2 = Entry(hs_calc,width=30, font=('Arial', 15))
    e2.place(x=130, y=280) 


    age_label = Label(hs_calc, text='Enter age',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    age_label.place(x=130,y=380)
    e3 = Entry(hs_calc,width=30, font=('Arial', 15))
    e3.place(x=130, y=430)
  
    calc_button = Button(hs_calc,text='CALCULATE', font=('Bahnschrift SemiBold SemiCondensed',18),bg='white',fg='black',command=hs_entry)
    calc_button.place(x=230,y=500)
    
    close = Button(hs_calc, text='<<<',bg='black', fg='white', command=hs_calc.destroy)
    close.place(x=500,y=640)


def sugar_win():
    sugar_gen = Toplevel()
    sugar_gen.geometry('600x900')
    sugar_gen.config(bg='black')
    sugar_gen.title('FITNESS APP')
    sugar_gen.iconbitmap("icon.ico")
    sugar_gen.resizable(False,False)  

    
    def graphing():
        global levels
        months = ['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec'] 
        s1_value = int(s1.get())
        s2_value = int(s2.get())
        s3_value = int(s3.get())
        s4_value = int(s4.get())
        s5_value = int(s5.get())
        s6_value = int(s6.get())
        s7_value = int(s7.get())
        s8_value = int(s8.get())
        s9_value = int(s9.get())
        s10_value = int(s10.get())
        s11_value = int(s11.get())
        s12_value = int(s12.get())
        levels = [s1_value,s2_value,s3_value,s4_value,s5_value,s6_value,s7_value,s8_value,s9_value,s10_value,s11_value,s12_value]


        plt.plot(months,levels,marker = 'o', markerfacecolor='black',color='black')
        plt.xlabel('MONTHS')
        plt.ylabel('SUGAR LEVELS')
        plt.title('SUGAR LEVEL GRAPH')
        plt.show()

    top_name = Label(sugar_gen,text='SUGAR LEVEL GRAPH' ,font=('Bahnschrift SemiBold SemiCondensed', 40), fg = 'white', bg='black', width=28, height=1)
    top_name.pack()

    
    s_level = Label(sugar_gen, text='Enter sugar levels',font=('Bahnschrift SemiBold SemiCondensed',24), fg='white', bg='black')
    s_level.place(x=170,y=80)

    
    s1_name = Label(sugar_gen,text='January:', font=('Bahnschrift SemiBold SemiCondensed',18),fg='white',bg='black')
    s1_name.place(x=50,y=180)
    s1 = Entry(sugar_gen,width=10, font=('Arial', 15))
    s1.place(x=35,y=220)
    
    

    s2_name = Label(sugar_gen,text='February:', font=('Bahnschrift SemiBold SemiCondensed',18),fg='white',bg='black')
    s2_name.place(x=243,y=180)
    s2 = Entry(sugar_gen,width=10, font=('Arial', 15))
    s2.place(x=235,y=220)
    

    s3_name = Label(sugar_gen,text='March:', font=('Bahnschrift SemiBold SemiCondensed',18),fg='white',bg='black')
    s3_name.place(x=455,y=180)
    s3 = Entry(sugar_gen,width=10, font=('Arial', 15))
    s3.place(x=435,y=220)
    

    s4_name = Label(sugar_gen,text='April:', font=('Bahnschrift SemiBold SemiCondensed',18),fg='white',bg='black')
    s4_name.place(x=60,y=280)
    s4 = Entry(sugar_gen,width=10, font=('Arial', 15))
    s4.place(x=35,y=320)
    

    s5_name = Label(sugar_gen,text='May:', font=('Bahnschrift SemiBold SemiCondensed',18),fg='white',bg='black')
    s5_name.place(x=265,y=280)
    s5 = Entry(sugar_gen,width=10, font=('Arial', 15))
    s5.place(x=235,y=320)
    

    s6_name = Label(sugar_gen,text='June:', font=('Bahnschrift SemiBold SemiCondensed',18),fg='white',bg='black')
    s6_name.place(x=465,y=280)
    s6 = Entry(sugar_gen,width=10, font=('Arial', 15))
    s6.place(x=435,y=320)
    

    s7_name = Label(sugar_gen,text='July:', font=('Bahnschrift SemiBold SemiCondensed',18),fg='white',bg='black')
    s7_name.place(x=65,y=380)
    s7 = Entry(sugar_gen,width=10, font=('Arial', 15))
    s7.place(x=35,y=420)
    

    s8_name = Label(sugar_gen,text='August:', font=('Bahnschrift SemiBold SemiCondensed',18),fg='white',bg='black')
    s8_name.place(x=255,y=380)
    s8= Entry(sugar_gen,width=10, font=('Arial', 15))
    s8.place(x=235,y=420)
    

    s9_name = Label(sugar_gen,text='September:', font=('Bahnschrift SemiBold SemiCondensed',18),fg='white',bg='black')
    s9_name.place(x=435,y=380)
    s9= Entry(sugar_gen,width=10, font=('Arial', 15))
    s9.place(x=435,y=420)
    

    s10_name = Label(sugar_gen,text='October:', font=('Bahnschrift SemiBold SemiCondensed',18),fg='white',bg='black')
    s10_name.place(x=50,y=480)
    s10 = Entry(sugar_gen,width=10, font=('Arial', 15))
    s10.place(x=35,y=520)
    

    s11_name = Label(sugar_gen,text='November:', font=('Bahnschrift SemiBold SemiCondensed',18),fg='white',bg='black')
    s11_name.place(x=235,y=480)
    s11 = Entry(sugar_gen,width=10, font=('Arial', 15))
    s11.place(x=235,y=520)
    

    s12_name = Label(sugar_gen,text='December:', font=('Bahnschrift SemiBold SemiCondensed',18),fg='white',bg='black')
    s12_name.place(x=435,y=480)
    s12 = Entry(sugar_gen,width=10, font=('Arial', 15))
    s12.place(x=435,y=520)
    


    calc_button = Button(sugar_gen,text='Generate Graph', font=('Bahnschrift SemiBold SemiCondensed',26),fg='black',bg='white', command=graphing)
    calc_button.place(x=170, y=600)


    close = Button(sugar_gen, text='<<<',bg='black', fg='white', command=sugar_gen.destroy)
    close.place(x=500,y=640)

def knee_screen():
    k_screen = Toplevel()
    k_screen.geometry('900x200')
    k_screen.config(bg='black')
    k_screen.title('FITNESS APP')
    k_screen.iconbitmap("icon.ico")
    k_screen.resizable(False,False)

    msg = Label(k_screen, text='1) Begin in a push-up position on your knees. Break at the elbow and shoulder joint.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg.pack()

    msg2 = Label(k_screen, text='2) Lower your body, keeping elbows close.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg2.pack()

    msg3 = Label(k_screen, text='3) Push back up to the starting position.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg3.pack()

def inc_screen():
    i_screen = Toplevel()
    i_screen.geometry('900x200')
    i_screen.config(bg='black')
    i_screen.title('FITNESS APP')
    i_screen.iconbitmap("icon.ico")
    i_screen.resizable(False,False)

    msg = Label(i_screen, text='1) Stand facing bench or sturdy elevated platform.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg.pack()

    msg2 = Label(i_screen, text='2) Place hands on edge of bench or platform, slightly wider than shoulder width.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg2.pack()

    msg3 = Label(i_screen, text='3) Slowly lower your body until your chest almost touches the bench.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg3.pack()

    msg4 = Label(i_screen, text='4) Push body up until arms are extended.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg4.pack()

def push():
    p_screen = Toplevel()
    p_screen.geometry('900x200')
    p_screen.config(bg='black')
    p_screen.title('FITNESS APP')
    p_screen.iconbitmap("icon.ico")
    p_screen.resizable(False,False)

    msg = Label(p_screen, text='1) Place your hands firmly on the ground, directly under shoulders.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg.pack()

    msg2 = Label(p_screen, text='2) Flatten your back so your entire body is straight and slowly lower your body.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg2.pack()

    msg3 = Label(p_screen, text='3) Draw shoulder blades back and down, keeping elbows tucked close to your body.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg3.pack()

    msg4 = Label(p_screen, text='4) Exhale as you push back to the starting position.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg4.pack()

def dip_screen():
    d_screen = Toplevel()
    d_screen.geometry('900x200')
    d_screen.config(bg='black')
    d_screen.title('FITNESS APP')
    d_screen.iconbitmap("icon.ico")
    d_screen.resizable(False,False)

    msg = Label(d_screen, text='1) Hold your body with arms locked above the equipment.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg.pack()

    msg2 = Label(d_screen, text='2) Lower your body slowly while leaning forward, flare out your elbows.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg2.pack()

    msg3 = Label(d_screen, text='3) Raise your body above the bars until your arms are locked.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg3.pack()


def dec_screen():
    de_screen = Toplevel()
    de_screen.geometry('900x200')
    de_screen.config(bg='black')
    de_screen.title('FITNESS APP')
    de_screen.iconbitmap("icon.ico")
    de_screen.resizable(False,False)

    msg = Label(de_screen, text='1) Use a bench to elevate your feet.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg.pack()

    msg2 = Label(de_screen, text='2) Put your hands slightly wider than shoulder-width.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg2.pack()

    msg3 = Label(de_screen, text='3) Slowly lower your body until your chest almost touches the ground.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg3.pack()

    msg4 = Label(de_screen, text='4) Raise your body until you almost lock your elbows.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg4.pack()


def chest_wkt():
    chest_screen = Toplevel()
    chest_screen.geometry('600x900')
    chest_screen.config(bg='black')
    chest_screen.title('FITNESS APP')
    chest_screen.iconbitmap("icon.ico")
    chest_screen.resizable(False,False) 

    msg = Label(chest_screen, text='For hitting chest here are',font=('Bahnschrift SemiBold SemiCondensed',28), fg='white', bg='black')
    msg.pack(pady=20)

    msg2 = Label(chest_screen, text='some workouts with increasing intensity',font=('Bahnschrift SemiBold SemiCondensed',28), fg='white', bg='black')
    msg2.pack()

    knee = Button(chest_screen,text='Knee pushups', font=('Bahnschrift SemiBold SemiCondensed',30),bg='white',fg='black', command=knee_screen)
    knee.pack(pady=20)

    inc = Button(chest_screen,text='Incline pushups', font=('Bahnschrift SemiBold SemiCondensed',30),bg='white',fg='black', command=inc_screen)
    inc.pack(pady=10)

    pushups = Button(chest_screen,text='Pushups', font=('Bahnschrift SemiBold SemiCondensed',30),bg='white',fg='black', command=push)
    pushups.pack(pady=10)

    dips = Button(chest_screen,text='Dips', font=('Bahnschrift SemiBold SemiCondensed',30),bg='white',fg='black', command=dip_screen)
    dips.pack(pady=10)

    dec = Button(chest_screen,text='Decline pushups', font=('Bahnschrift SemiBold SemiCondensed',30),bg='white',fg='black', command=dec_screen)
    dec.pack(pady=10)

    close = Button(chest_screen, text='<<<',bg='black', fg='white', command=chest_screen.destroy)
    close.place(x=500,y=640)

def sq():
    sq_screen = Toplevel()
    sq_screen.geometry('900x200')
    sq_screen.config(bg='black')
    sq_screen.title('FITNESS APP')
    sq_screen.iconbitmap("icon.ico")
    sq_screen.resizable(False,False)

    msg = Label(sq_screen, text='1) Stand with your feet shoulder width apart.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg.pack()

    msg2 = Label(sq_screen, text='2) Flex your knees and hips and sit back into the squat while lowering your body.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg2.pack()

    msg3 = Label(sq_screen, text='3) Continue down to full depth.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg3.pack()

    msg4 = Label(sq_screen, text='4) Return to starting position.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg4.pack()

def lunges():
    l_screen = Toplevel()
    l_screen.geometry('900x200')
    l_screen.config(bg='black')
    l_screen.title('FITNESS APP')
    l_screen.iconbitmap("icon.ico")
    l_screen.resizable(False,False)

    msg = Label(l_screen, text='1) Step forward with one leg.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg.pack()

    msg2 = Label(l_screen, text='2) Lower your body until your rear knee nearly touches the ground.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg2.pack()

    msg3 = Label(l_screen, text='3) Ensure you remain upright, and your front knee stay above the front foot.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg3.pack()

    msg4 = Label(l_screen, text='4) Push off the floor with your front foot until you return to the starting position.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg4.pack()

    msg5 = Label(l_screen, text='Switch legs',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg5.pack()

def jsq_screen():
    jsqs = Toplevel()
    jsqs.geometry('900x200')
    jsqs.config(bg='black')
    jsqs.title('FITNESS APP')
    jsqs.iconbitmap("icon.ico")
    jsqs.resizable(False,False)

    msg = Label(jsqs, text='1) Stand with your feet shoulder-width apart.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg.pack()

    msg2 = Label(jsqs, text='2) Start by doing a regular squat, then engage your core and jump up explosively.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg2.pack()

    msg3 = Label(jsqs, text='3) When you land, lower your body back into the squat position.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg3.pack()


def bsq_screen():
    bsqs = Toplevel()
    bsqs.geometry('900x200')
    bsqs.config(bg='black')
    bsqs.title('FITNESS APP')
    bsqs.iconbitmap("icon.ico")
    bsqs.resizable(False,False)

    msg = Label(bsqs, text='1) Stand with your back to a bench and place one of your feet on the bench.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg.pack()

    msg2 = Label(bsqs, text='2) Squat down until your front leg is about parallel to the floor.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg2.pack()

    msg3 = Label(bsqs, text='3) Go back to the starting position.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg3.pack()


def quads_wkt():
    quads_screen = Toplevel()
    quads_screen.geometry('600x900')
    quads_screen.config(bg='black')
    quads_screen.title('FITNESS APP')
    quads_screen.iconbitmap("icon.ico")
    quads_screen.resizable(False,False)


    msg = Label(quads_screen, text='Here are some workouts to hit your Quads',font=('Bahnschrift SemiBold SemiCondensed',26), fg='white', bg='black')
    msg.pack(pady=20)

    squats = Button(quads_screen,text='Squats', font=('Bahnschrift SemiBold SemiCondensed',30),bg='white',fg='black', command=sq)
    squats.pack(pady=20)

    lung = Button(quads_screen,text='Forward lunges', font=('Bahnschrift SemiBold SemiCondensed',30),bg='white',fg='black', command=lunges)
    lung.pack(pady=10)

    jsq = Button(quads_screen,text='Jump squats', font=('Bahnschrift SemiBold SemiCondensed',30),bg='white',fg='black', command=jsq_screen)
    jsq.pack(pady=10)

    bsq = Button(quads_screen,text='Bulgarian split squats', font=('Bahnschrift SemiBold SemiCondensed',30),bg='white',fg='black', command=bsq_screen)
    bsq.pack(pady=10)

    close = Button(quads_screen, text='<<<',bg='black', fg='white', command=quads_screen.destroy)
    close.place(x=500,y=640)
    

def bw_screen():
    bw_select = Toplevel()
    bw_select.geometry('600x900')
    bw_select.config(bg='black')
    bw_select.title('FITNESS APP')
    bw_select.iconbitmap("icon.ico")
    bw_select.resizable(False,False) 

    mus = Label(bw_select, text='What muscles do you want to workout?',font=('Bahnschrift SemiBold SemiCondensed',28), fg='white', bg='black')
    mus.pack(pady=20)

    chest = Button(bw_select,text='Chest', font=('Bahnschrift SemiBold SemiCondensed',30),bg='white',fg='black', command=chest_wkt)
    chest.pack(pady=60)

    quads = Button(bw_select,text='Quads', font=('Bahnschrift SemiBold SemiCondensed',30),bg='white',fg='black', command=quads_wkt)
    quads.pack(pady=60)

    close = Button(bw_select, text='<<<',bg='black', fg='white', command=bw_select.destroy)
    close.place(x=500,y=640)


def dc():
    dcurls = Toplevel()
    dcurls.geometry('900x200')
    dcurls.config(bg='black')
    dcurls.title('FITNESS APP')
    dcurls.iconbitmap("icon.ico")
    dcurls.resizable(False,False)

    msg = Label(dcurls, text="1) Stand up straight with a dumbbell in each hand at arm's length.",font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg.pack()

    msg2 = Label(dcurls, text='2) Raise one dumbbell and twist your forearm until it is vertical and your palm faces the shoulder.',font=('Bahnschrift SemiBold SemiCondensed',17), fg='white', bg='black')
    msg2.pack()

    msg3 = Label(dcurls, text='3) Lower to original position and repeat with opposite arm.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg3.pack()


def dhcurls():
    dhammer = Toplevel()
    dhammer.geometry('900x200')
    dhammer.config(bg='black')
    dhammer.title('FITNESS APP')
    dhammer.iconbitmap("icon.ico")
    dhammer.resizable(False,False)

    msg = Label(dhammer, text="1) Hold the dumbbells with a neutral grip (thumbs facing the ceiling).",font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg.pack()

    msg2 = Label(dhammer, text='2) Slowly lift the dumbbell up to chest height.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg2.pack()

    msg3 = Label(dhammer, text='3) Return to starting position and repeat.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg3.pack()

def dr():
    drev = Toplevel()
    drev.geometry('900x200')
    drev.config(bg='black')
    drev.title('FITNESS APP')
    drev.iconbitmap("icon.ico")
    drev.resizable(False,False)

    msg = Label(drev, text="1) Grab the dumbbells with a pronated (overhand) grip.",font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg.pack()

    msg2 = Label(drev, text="You can do this exercise thumbless if it's more comfortable on your wrists.",font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg2.pack()

    msg3 = Label(drev, text='2) Flex at the elbows until your biceps touch your forearms.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg3.pack()

    msg4 = Label(drev, text='Try not to let your elbows flair outward.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg4.pack()

def drdrow():
    drows = Toplevel()
    drows.geometry('900x200')
    drows.config(bg='black')
    drows.title('FITNESS APP')
    drows.iconbitmap("icon.ico")
    drows.resizable(False,False)

    msg = Label(drows, text="1) Hinge forward at the hips while maintaining a flat back.",font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg.pack()

    msg2 = Label(drows, text="Try to get your torso as close to parallel with the ground as your mobility will allow for.",font=('Bahnschrift SemiBold SemiCondensed',19), fg='white', bg='black')
    msg2.pack()

    msg3 = Label(drows, text='Let your arms hang in front of you.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg3.pack()

    msg4 = Label(drows, text='Pull your elbows back towards the ceiling while flaring your elbows outward.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg4.pack()


def biceps_wkt():
    bi_screen = Toplevel()
    bi_screen.geometry('600x900')
    bi_screen.config(bg='black')
    bi_screen.title('FITNESS APP')
    bi_screen.iconbitmap("icon.ico")
    bi_screen.resizable(False,False)


    msg = Label(bi_screen, text='For hitting biceps here are',font=('Bahnschrift SemiBold SemiCondensed',28), fg='white', bg='black')
    msg.pack(pady=20)

    msg2 = Label(bi_screen, text='some workouts with increasing intensity',font=('Bahnschrift SemiBold SemiCondensed',28), fg='white', bg='black')
    msg2.pack()

    dcurl = Button(bi_screen,text='Dumbell curl', font=('Bahnschrift SemiBold SemiCondensed',30),bg='white',fg='black', command=dc)
    dcurl.pack(pady=20)

    dhcurl = Button(bi_screen,text='Dumbell hammer curl', font=('Bahnschrift SemiBold SemiCondensed',30),bg='white',fg='black', command=dhcurls)
    dhcurl.pack(pady=10)
    
    drcurl = Button(bi_screen,text='Dumbell reverse curl', font=('Bahnschrift SemiBold SemiCondensed',30),bg='white',fg='black', command=dr)
    drcurl.pack(pady=10)

    drdr = Button(bi_screen,text='Dumbell real delt row', font=('Bahnschrift SemiBold SemiCondensed',30),bg='white',fg='black', command=drdrow)
    drdr.pack(pady=10)

    close = Button(bi_screen, text='<<<',bg='black', fg='white', command=bi_screen.destroy)
    close.place(x=500,y=640)

def dpress():
    press = Toplevel()
    press.geometry('900x200')
    press.config(bg='black')
    press.title('FITNESS APP')
    press.iconbitmap("icon.ico")
    press.resizable(False,False)

    msg = Label(press, text="1) Start by lying flat on a bench with a dumbbell in each hand.",font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg.pack()

    msg2 = Label(press, text="2) Hold the dumbbells at chest level with your palms facing forward.",font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg2.pack()

    msg3 = Label(press, text='3) Engage your core and press the dumbbells upward until your arms are fully extended.',font=('Bahnschrift SemiBold SemiCondensed',19), fg='white', bg='black')
    msg3.pack()

def skull():
    skullcrush = Toplevel()
    skullcrush.geometry('900x200')
    skullcrush.config(bg='black')
    skullcrush.title('FITNESS APP')
    skullcrush.iconbitmap("icon.ico")
    skullcrush.resizable(False,False)

    msg = Label(skullcrush, text="1) Lay flat on the floor or a bench with your fists extended to the ceiling and a neutral grip.",font=('Bahnschrift SemiBold SemiCondensed',19), fg='white', bg='black')
    msg.pack()

    msg2 = Label(skullcrush, text="2) Break at the elbows until your fists are by your temples.",font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg2.pack()

    msg3 = Label(skullcrush, text='Then extend your elbows and flex your triceps at the top.',font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg3.pack()

def seated():
    sover = Toplevel()
    sover.geometry('920x200')
    sover.config(bg='black')
    sover.title('FITNESS APP')
    sover.iconbitmap("icon.ico")
    sover.resizable(False,False)

    msg = Label(sover, text="1) Sit on the bench and hold a dumbbell with both hands. Raise the dumbbell overhead at arms length,",font=('Bahnschrift SemiBold SemiCondensed',17), fg='white', bg='black')
    msg.pack()

    msg2 = Label(sover, text="holding the weight up with the palms of your hands.",font=('Bahnschrift SemiBold SemiCondensed',20), fg='white', bg='black')
    msg2.pack()

    msg3 = Label(sover, text='2) Keep your elbows in while you lower the weight behind your head, your upper arms stationary.',font=('Bahnschrift SemiBold SemiCondensed',17), fg='white', bg='black')
    msg3.pack()

    msg4 = Label(sover, text='3) Raise the weight back to starting position.',font=('Bahnschrift SemiBold SemiCondensed',19), fg='white', bg='black')
    msg4.pack()

def kick():
    kickback = Toplevel()
    kickback.geometry('960x200')
    kickback.config(bg='black')
    kickback.title('FITNESS APP')
    kickback.iconbitmap("icon.ico")
    kickback.resizable(False,False)

    msg = Label(kickback, text="1) Start by standing with your feet shoulder-width apart and holding a dumbbell in one hand.",font=('Bahnschrift SemiBold SemiCondensed',18), fg='white', bg='black')
    msg.pack()

    msg2 = Label(kickback, text="2) Bend at the waist and place your opposite hand on your knee for support.",font=('Bahnschrift SemiBold SemiCondensed',18), fg='white', bg='black')
    msg2.pack()

    msg3 = Label(kickback, text='3) From this starting position, extend your arm backwards so that the dumbbell is behind your body.',font=('Bahnschrift SemiBold SemiCondensed',18), fg='white', bg='black')
    msg3.pack()

    msg4 = Label(kickback, text='4) Make sure to keep your elbow close to your body and your core engaged throughout the movement.',font=('Bahnschrift SemiBold SemiCondensed',18), fg='white', bg='black')
    msg4.pack()


def triceps_wkt():
    tri_screen = Toplevel()
    tri_screen.geometry('600x900')
    tri_screen.config(bg='black')
    tri_screen.title('FITNESS APP')
    tri_screen.iconbitmap("icon.ico")
    tri_screen.resizable(False,False)


    msg = Label(tri_screen, text='For hitting triceps here are',font=('Bahnschrift SemiBold SemiCondensed',28), fg='white', bg='black')
    msg.pack(pady=20)

    msg2 = Label(tri_screen, text='some workouts with increasing intensity',font=('Bahnschrift SemiBold SemiCondensed',28), fg='white', bg='black')
    msg2.pack()

    dbpress = Button(tri_screen,text='Dumbell bench press', font=('Bahnschrift SemiBold SemiCondensed',30),bg='white',fg='black', command=dpress)
    dbpress.pack(pady=20)

    dskull = Button(tri_screen,text='Dumbell skullcrusher', font=('Bahnschrift SemiBold SemiCondensed',30),bg='white',fg='black', command=skull)
    dskull.pack(pady=10)
    
    dsote = Button(tri_screen,text='Dumbell seated overhead tricep extension', font=('Bahnschrift SemiBold SemiCondensed',24),bg='white',fg='black', command=seated)
    dsote.pack(pady=10)

    dkick = Button(tri_screen,text='Dumbell tricep kickback', font=('Bahnschrift SemiBold SemiCondensed',30),bg='white',fg='black', command=kick)
    dkick.pack(pady=10)

    close = Button(tri_screen, text='<<<',bg='black', fg='white', command=tri_screen.destroy)
    close.place(x=500,y=640)


def w_screen():
    w_select = Toplevel()
    w_select.geometry('600x900')
    w_select.config(bg='black')
    w_select.title('FITNESS APP')
    w_select.iconbitmap("icon.ico")
    w_select.resizable(False,False) 

    mus = Label(w_select, text='What muscles do you want to workout?',font=('Bahnschrift SemiBold SemiCondensed',28), fg='white', bg='black')
    mus.pack(pady=20)

    biceps = Button(w_select,text='Biceps', font=('Bahnschrift SemiBold SemiCondensed',30),bg='white',fg='black', command=biceps_wkt)
    biceps.pack(pady=60)

    triceps = Button(w_select,text='Triceps', font=('Bahnschrift SemiBold SemiCondensed',30),bg='white',fg='black', command=triceps_wkt)
    triceps.pack(pady=60)

    close = Button(w_select, text='<<<',bg='black', fg='white', command=w_select.destroy)
    close.place(x=500,y=640)    
    

def workout_win():
    workout_screen = Toplevel()
    workout_screen.geometry('600x900')
    workout_screen.config(bg='black')
    workout_screen.title('FITNESS APP')
    workout_screen.iconbitmap("icon.ico")
    workout_screen.resizable(False,False) 

    work_eq = Label(workout_screen, text='What type of workout equipment',font=('Bahnschrift SemiBold SemiCondensed',26), fg='white', bg='black')
    work_eq.pack(pady=20)

    work_eq2 = Label(workout_screen, text='do you have?',font=('Bahnschrift SemiBold SemiCondensed',26), fg='white', bg='black')
    work_eq2.pack()
    

    body_weight = Button(workout_screen,text='Bodyweights', font=('Bahnschrift SemiBold SemiCondensed',30),bg='white',fg='black', command=bw_screen)
    body_weight.pack(pady=60)

    weight = Button(workout_screen,text='Weights', font=('Bahnschrift SemiBold SemiCondensed',30),bg='white',fg='black', command=w_screen)
    weight.pack(pady=20)



    close = Button(workout_screen, text='<<<',bg='black', fg='white', command=workout_screen.destroy)
    close.place(x=500,y=640)




my_pic = Image.open('Logoo.png')
resized = my_pic.resize((500,500))
new_pic = ImageTk.PhotoImage(resized)

logo = Label(window, image=new_pic, bg='black')
logo.pack()






slogan = Label(window,text="FlexZone", fg='white', bg='black', font=('Bahnschrift SemiBold SemiCondensed',50))
slogan.pack()


window.mainloop()


