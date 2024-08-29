from tkinter import *
from PIL import ImageTk, Image
import customtkinter
import matplotlib.pyplot as plt


window = Tk()
window.geometry('600x900')
window.config(bg='black')
window.title('FITNESS APP')
window.iconbitmap("icon.ico")
window.resizable(False,False)


def open():
    options = Toplevel()
    options.geometry('600x900')
    options.config(bg='black')
    options.title('FITNESS APP')
    options.iconbitmap("icon.ico")
    options.resizable(False,False)

    BMI_button = Button(options, text='BMI', bg='black', fg='white', height=1, width=15, font=('Impact',30), command=bmi_window)
    BMI_button.place(x=150, y=50)
    
    Health_button = Button(options,text='Health Score', bg='black', fg='white', height=1, width=15, font=('Impact',30), command=health_start)
    Health_button.place(x=150, y=200)

    Sugar_levels = Button(options,text='Sugar level tracker', bg='black', fg='white', height=1, width=16, font=('Impact',30), command=sugar_win)
    Sugar_levels.place(x=140, y=350)

    workouts_button = Button(options,text='Workouts', bg='black', fg='white', height=1, width=16, font=('Impact',30),command=workout_win)
    workouts_button.place(x=140, y=500)

    close = Button(options, text='<<<',bg='black', fg='white', command=options.destroy)
    close.place(x=500, y=720)
    

def bmi_window():
    calc = Toplevel()
    calc.geometry('600x900')
    calc.config(bg='black')
    calc.title('FITNESS APP')
    calc.iconbitmap("icon.ico")
    calc.resizable(False,False)

    top = Label(calc,text='BMI CALCULATOR' ,font=('Impact', 40), fg = 'white', bg='black', width=28, height=1)
    top.pack()

    height_label = Label(calc,font=('Impact', 30), fg = 'white', bg='black', width=17, height=4)
    height_label.place(x=20, y=60)

    height_text = Label(calc,text='HEIGHT (CM)' ,font=('Impact', 30), fg = 'white', bg='black', width=10, height=1)
    height_text.place(x=180, y=100)

    weight_label = Label(calc ,font=('Impact', 30,'bold'), fg = 'white', bg='black', width=17, height=4)
    weight_label.place(x=20, y=210)

    weight_text = Label(calc,text='WEIGHT (KG)' ,font=('Impact', 30,'bold'), fg = 'white', bg='black', width=10, height=1)
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

    height_entry = customtkinter.CTkEntry(calc, textvariable=height, bg_color='black',fg_color='white',border_width=0, text_color='black', font=customtkinter.CTkFont(family='Impact',size=20))
    height_entry.place(x=220, y=170)

    weight_entry = customtkinter.CTkEntry(calc, textvariable=weight, bg_color='black',fg_color='white',border_width=0, text_color='black', font=customtkinter.CTkFont(family='Impact',size=20))
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

        result2_label = customtkinter.CTkLabel(calc, textvariable=txt,font=customtkinter.CTkFont(family='Impact',size=30), text_color='white')
        result2_label.place(x=235, y=630)

    calc_button = customtkinter.CTkButton(calc,text='CALCULATE', command=BMI, width=170, height=50,hover_color='white', fg_color='white',text_color='black',font=customtkinter.CTkFont(family='Impact',size=20))
    calc_button.place(x=200, y= 500)

    close = Button(calc, text='<<<',bg='black', fg='white', command=calc.destroy)
    close.place(x=500, y=720)



def health_start():
    hs_calc = Toplevel()
    hs_calc.geometry('600x900')
    hs_calc.config(bg='black')
    hs_calc.title('FITNESS APP')
    hs_calc.iconbitmap("icon.ico")
    hs_calc.resizable(False,False)

    top = Label(hs_calc,text='HEALTH SCORE CALCULATOR' ,font=('Impact', 40), fg = 'white', bg='black', width=28, height=1)
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
            m2.place(y=640)


        score_text = Label(hs_calc,text='Your score is', font=('Impact',24),fg='white',bg='black')
        score_text.place(x=210, y=580)


        score = Label(hs_calc, text=m1, font=('Arial',20), fg='white', bg='black')
        score.place(x=255, y=620)

    steps_label = Label(hs_calc, text='Enter steps',font=('Impact',20), fg='white', bg='black')
    steps_label.place(x=130,y=80)
    e1 = Entry(hs_calc,width=30, font=('Arial', 15))
    e1.place(x=130, y=130)


    cal_label = Label(hs_calc, text='Enter calories burned',font=('Impact',20), fg='white', bg='black')
    cal_label.place(x=130,y=230)
    e2 = Entry(hs_calc,width=30, font=('Arial', 15))
    e2.place(x=130, y=280) 


    age_label = Label(hs_calc, text='Enter age',font=('Impact',20), fg='white', bg='black')
    age_label.place(x=130,y=380)
    e3 = Entry(hs_calc,width=30, font=('Arial', 15))
    e3.place(x=130, y=430)
  
    calc_button = Button(hs_calc,text='CALCULATE', font=('Impact',18),bg='white',fg='black',command=hs_entry)
    calc_button.place(x=230,y=500)
    
    close = Button(hs_calc, text='<<<',bg='black', fg='white', command=hs_calc.destroy)
    close.place(x=500, y=720)


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

    top_name = Label(sugar_gen,text='SUGAR LEVEL GRAPH' ,font=('Impact', 40), fg = 'white', bg='black', width=28, height=1)
    top_name.pack()

    
    s_level = Label(sugar_gen, text='Enter sugar levels',font=('Impact',24), fg='white', bg='black')
    s_level.place(x=170,y=80)

    
    s1_name = Label(sugar_gen,text='January:', font=('Impact',18),fg='white',bg='black')
    s1_name.place(x=50,y=180)
    s1 = Entry(sugar_gen,width=10, font=('Arial', 15))
    s1.place(x=35,y=220)
    
    

    s2_name = Label(sugar_gen,text='February:', font=('Impact',18),fg='white',bg='black')
    s2_name.place(x=243,y=180)
    s2 = Entry(sugar_gen,width=10, font=('Arial', 15))
    s2.place(x=235,y=220)
    

    s3_name = Label(sugar_gen,text='March:', font=('Impact',18),fg='white',bg='black')
    s3_name.place(x=455,y=180)
    s3 = Entry(sugar_gen,width=10, font=('Arial', 15))
    s3.place(x=435,y=220)
    

    s4_name = Label(sugar_gen,text='April:', font=('Impact',18),fg='white',bg='black')
    s4_name.place(x=60,y=280)
    s4 = Entry(sugar_gen,width=10, font=('Arial', 15))
    s4.place(x=35,y=320)
    

    s5_name = Label(sugar_gen,text='May:', font=('Impact',18),fg='white',bg='black')
    s5_name.place(x=265,y=280)
    s5 = Entry(sugar_gen,width=10, font=('Arial', 15))
    s5.place(x=235,y=320)
    

    s6_name = Label(sugar_gen,text='June:', font=('Impact',18),fg='white',bg='black')
    s6_name.place(x=465,y=280)
    s6 = Entry(sugar_gen,width=10, font=('Arial', 15))
    s6.place(x=435,y=320)
    

    s7_name = Label(sugar_gen,text='July:', font=('Impact',18),fg='white',bg='black')
    s7_name.place(x=65,y=380)
    s7 = Entry(sugar_gen,width=10, font=('Arial', 15))
    s7.place(x=35,y=420)
    

    s8_name = Label(sugar_gen,text='August:', font=('Impact',18),fg='white',bg='black')
    s8_name.place(x=255,y=380)
    s8= Entry(sugar_gen,width=10, font=('Arial', 15))
    s8.place(x=235,y=420)
    

    s9_name = Label(sugar_gen,text='September:', font=('Impact',18),fg='white',bg='black')
    s9_name.place(x=435,y=380)
    s9= Entry(sugar_gen,width=10, font=('Arial', 15))
    s9.place(x=435,y=420)
    

    s10_name = Label(sugar_gen,text='October:', font=('Impact',18),fg='white',bg='black')
    s10_name.place(x=50,y=480)
    s10 = Entry(sugar_gen,width=10, font=('Arial', 15))
    s10.place(x=35,y=520)
    

    s11_name = Label(sugar_gen,text='November:', font=('Impact',18),fg='white',bg='black')
    s11_name.place(x=235,y=480)
    s11 = Entry(sugar_gen,width=10, font=('Arial', 15))
    s11.place(x=235,y=520)
    

    s12_name = Label(sugar_gen,text='December:', font=('Impact',18),fg='white',bg='black')
    s12_name.place(x=435,y=480)
    s12 = Entry(sugar_gen,width=10, font=('Arial', 15))
    s12.place(x=435,y=520)
    


    calc_button = Button(sugar_gen,text='Generate Graph', font=('Impact',26),fg='black',bg='white', command=graphing)
    calc_button.place(x=170, y=600)


    close = Button(sugar_gen, text='<<<',bg='black', fg='white', command=sugar_gen.destroy)
    close.place(x=500, y=720)
    

def workout_win():
    workout_screen = Toplevel()
    workout_screen.geometry('600x900')
    workout_screen.config(bg='black')
    workout_screen.title('FITNESS APP')
    workout_screen.iconbitmap("icon.ico")
    workout_screen.resizable(False,False) 



    close = Button(workout_screen, text='<<<',bg='black', fg='white', command=workout_screen.destroy)
    close.place(x=500, y=720)




my_pic = Image.open('logo.png')
resized = my_pic.resize((700,500))
new_pic = ImageTk.PhotoImage(resized)


logo = Label(window, image=new_pic, bg='black')
logo.pack()



next_button = Button(window, text='>>>', bg='black', fg='white', command=open)
next_button.place(x=500, y=720)


slogan = Label(window,text='Sore today. Strong tomorrow.', fg='white', bg='black', font=('Impact',30))
slogan.pack()


window.mainloop()


