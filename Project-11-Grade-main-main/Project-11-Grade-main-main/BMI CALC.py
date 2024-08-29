system = input("What metric system do you choose(metric(kg,cm) or metric(pounds,feet)): ")

if system == 'metric' or system == 'Metric':
    wt = int(input("What is your weight(in kg): "))
    h = int(input("What is your height(in cm): "))
    bmi = wt/((h/100)*2)
    print("Your BMI is",bmi)