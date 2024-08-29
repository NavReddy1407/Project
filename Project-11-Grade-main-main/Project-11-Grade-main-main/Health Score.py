steps = int(input("How many steps have you walked today?: "))
cal = int(input("How many calories have you burned?: "))
age = int(input("How old are you?: "))

if age < 13:
    print("You are too young to use this app.")

elif 13 <= age < 60:
    step_score = steps/200
    cal_score = cal/50
    scr_count = 0
       
    scr_count += step_score + cal_score
    print("Your health score is ",scr_count)
    if scr_count <= 20:
        print("You need to get some exercise NOW!!")
    
    if 20 < scr_count <= 40:
        print("It looks like its time for you to be more active")
    
    if 40 < scr_count <= 60:
        print("Keep going...I can sense the progress")  
        
    if 60 < scr_count <= 80:
        print("Good work....let's push for more")
    
    if 80 < scr_count <= 90:
        print("Your are an athlete....next time I want 100%")
        
    if 90 < scr_count < 100:
        print("You are a beast...keep pushing!!!")
    
    if scr_count>=100:
        print("You have done it...100 points....good work...keep this up and you will be in the top 1%")

elif age > 60:
    step_score = steps/160
    cal_score = cal/50
    scr_count = 0
       
    scr_count += step_score + cal_score
    print("Your health score is ",scr_count)
    print('''You dont need this health score...your body burns all the calories it needs to in daily life
          Just make sure to stay active and go on regular walks :)''')
