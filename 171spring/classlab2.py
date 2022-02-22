import datetime
now = datetime.datetime.now()
currentYear = now.year
currentMonth = now.month
currentDay = now.day
def answer(step5,step3,step4):
    if step5<18:
        Step1=18-step5-1
        Step2=12-(step3-step5*12)-1
        Step3=30-step4
        print("You are:",step5,"years old.")
        print("You still have:",Step1,"years;",Step2,"months;",Step3,"days old to drve a car.")
        print("Not old enough to drive a car.")
        print("Not old enough to drive a car and drink alcohol")
    elif step5>=18 and round(step5)<21:
        Step1=21-step5-1
        Step2=12-(step3-step5*12)-1
        Step3=30-step4
        print("You are:",step5,"years old.")
        print("You still have:",Step1,"years;",Step2,"months;",Step3,"days old to drink alcohol.")
        print("Old enough to drive a car.")
        print("Not old enough to drive a car and drink alcohol")

    else:
        print("You are:",step5,"years old.")
        print("Old enough to drive a car and drink alcohol")
        
def count(byear,bmonth,bday):
    step1=currentYear-byear
    step2=(step1*12)+currentMonth
    step3=step2-bmonth
    step4=currentDay-bday
    if step4<0:
        step3=step3-1
        step4=step4+30
    step5=step3/12
    if round(step5)>step5:
        step5=round(step5)-1
    else:
        step5=round(step5)
    answer(step5,step3,step4)

def main():
    byear=int(input("enter your birth year:"))
    bmonth=int(input("enter your birth month:"))
    bday=int(input("enter your birth day:"))
    count(byear,bmonth,bday)
main()
