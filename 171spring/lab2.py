import datetime
now = datetime.datetime.now()
currentYear = now.year
currentMonth = now.month
currentDay = now.day

byear=int(input("enter your birth year:"))
bmonth=int(input("enter your birth month:"))
bday=int(input("enter your birth day:"))
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

if step5<18:
    Step1=18-step5-1
    Step2=12-step3-1
    Step3=30-step4
    print("you are:",step5,"years old.")
    print("you still have:",Step1,"years;",Step2,"months;",Step3,"days old to drink alcohol.")
    print("Not old enough to drive a car and drink alcohol")
elif step5>=18 and round(step5)<21:
    Step1=21-step5-1
    Step2=12-(step3-step5*12)-1
    Step3=30-step4
    print("you are:",step5,"years; old.")
    print("you still have:",Step1,"years;",Step2,"months;",Step3,"days old to drink alcohol.")
    print("old enough to drive a car.")

else:
    print("you are:",step5,"years old.")
    print("old enough to drive a car and drink alcohol")

