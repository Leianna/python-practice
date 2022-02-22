from math import *

'''price'''
SS=float(15.99)
PP=float(11.50)
MC=float(9.99)
IT=float(1.99)
LM=float(2.99)
CJ=float(2.50)
GB=float(3.99)
RW=float(4.99)
BE=float(2.59)
choice="yes"
age=int(input("Please enter your age:"))
while choice=="yes":
    meal=str(input("Enter the meal you want: \n1)Smoked Salmon \n2)Pasta Primavera \n3)Macaroni and Cheese \nplease enter 1,2or3:"))
    if meal=="quit":
        break
    while meal!="1" and meal!="2" and meal!="3":
        print("System Error, please try again")
        meal=input("Enter the meal you want: \n1)Smoked Salmon \n2)Pasta Primavera \n3)Macaroni and Cheese \nplease enter 1,2or3:")
    if meal=="1" or meal=="2" or meal=="3":
        if meal=="1" and int(age)<21:
            drink=input("Please enter the drink you want: \n1)Iced tea($1.99) \n2)Lemonade($2.99) \nPlease enter 1or2:")
            while drink!="1" and drink!="2" and drink!="quit":
                print("System Error, please try again")
                drink=str(input("Please enter the drink you want: \n1)Iced tea($1.99) \n2)Lemonade($2.99) \nPlease enter 1or2:"))
            if drink=="quit":
                break
            elif drink=="1":
                price=SS+IT
                print("Smoked Salmon ( $15.99)")
                print("Iced tea ($1.99)")
                tax=float(round(price*0.08,2))
                finalprice=float(round(tax+price,2))
                print("Tax:$",tax)
                print("Total:$",finalprice)
                choice=str(input("Do you want to continue order? \nplease enter yes or no:"))
                if choice=="no":
                    break
            elif drink=="2":
                price=SS+LM
                print("Smoked Salmon ( $15.99)")
                print("Lemonade($2.99)")
                tax=round(price*0.08,2)
                finalprice=round(tax+price,2)
                print("Tax:$",tax)
                print("Total:$",finalprice)
                choice=str(input("Do you want to continue order? \nplease enter yes or no:"))
                if choice=="no":
                    break
        elif meal=="1" and int(age)>=21:
            drink=str(input("Please enter the drink you want: \n1)Iced tea($1.99) \n2)Lemonade($2.99) \n3)Red wine($4.99) \nPlease enter 1,2or3:"))
            while drink!="1" and drink!="2" and drink!="3"and drink!="quit":
                print("System Error, please try again")
                drink=input("Please enter the drink you want: \n1)Iced tea($1.99) \n2)Lemonade($2.99) \n3)Red wine($4.99) \nPlease enter 1,2or3:")
            if drink=="quit":
                break
            elif drink=="1":
                price=SS+IT
                print("Smoked Salmon ( $15.99)")
                print("Iced tea ($1.99)")
                tax=round(price*0.08,2)
                finalprice=round(tax+price,2)
                print("Tax:$",tax)
                print("Total:$",finalprice)
                choice=input("Do you want to continue order? \nplease enter yes or no:")
                if choice=="no":
                        break
            elif drink=="2":
                price=SS+LM
                print("Smoked Salmon ( $15.99)")
                print("Lemonade($2.99)")
                tax=round(price*0.08,2)
                finalprice=round(tax+price,2)
                print("Tax:$",tax)
                print("Total:$",finalprice)
                choice=input("Do you want to continue order? \nplease enter yes or no:")
                if choice=="no":
                    break
            elif drink=="3":
                price=SS+RW
                print("Smoked Salmon ( $15.99)")
                print("Red wine($4.99)")
                tax=round(price*0.08,2)
                finalprice=round(tax+price,2)
                print("Tax:$",tax)
                print("Total:$",finalprice)
                choice=str(input("Do you want to continue order? \nplease enter yes or no:"))
                if choice=="no":
                    break
        elif meal=="2" and int(age)<21:
            drink=str(input("Please enter the drink you want: \n1)Cranberry juice ($2.50) \n2)Lemonade ($2.99) \nPlease enter 1or2:"))
            while drink!="0" and drink!="1" and drink!="2" and drink!="quit":
                print("System Error, please try again")
                drink=input("Please enter the drink you want: \n1)Cranberry juice ($2.50) \n2)Lemonade ($2.99) \nPlease enter 1or2:")
            if drink=="quit":
                break
            elif drink=="1":
                price=PP+CJ
                print("Pasta Primavera ( $11.50)")
                print("Cranberry juice ($2.50)")
                tax=round(price*0.08,2)
                finalprice=round(tax+price,2)
                print("Tax:$",tax)
                print("Total:$",finalprice)
                choice=str(input("Do you want to continue order? \nplease enter yes or no:"))
                if choice=="no":
                    break
            elif drink=="2":
                price=PP+LM
                print("Pasta Primavera ( $11.50)")
                print("Lemonade ($2.99)")
                tax=round(price*0.08,2)
                finalprice=round(tax+price,2)
                print("Tax:$",tax)
                print("Total:$",finalprice)
                choice=str(input("Do you want to continue order? \nplease enter yes or no:"))
                if choice=="no":
                    break
        elif meal=="2" and int(age)>=21:
            drink=str(input("Please enter the drink you want: \n1)Cranberry juice ($2.50) \n2)Lemonade ($2.99) \n3)Red wine($4.99) \nPlease enter 1,2or3:"))
            while drink!="3" and drink!="1" and drink!="2" and drink!="quit":
                print("System Error, please try again")
                drink=input("Please enter the drink you want: \n1)Cranberry juice ($2.50) \n2)Lemonade ($2.99) \n3)Red wine($4.99) \nPlease enter 1,2or3:")
            if drink=="quit":
                break
            elif drink=="1":
                price=PP+CJ
                print("Pasta Primavera ( $11.50)")
                print("Cranberry juice ($2.50)")
                tax=round(price*0.08,2)
                finalprice=round(tax+price,2)
                print("Tax:$",tax)
                print("Total:$",finalprice)
                choice=str(input("Do you want to continue order? \nplease enter yes or no:"))
                if choice=="no":
                        break
            elif drink=="2":
                price=PP+LM
                print("Pasta Primavera ( $11.50)")
                print("Lemonade ($2.99)")
                tax=round(price*0.08,2)
                finalprice=round(tax+price,2)
                print("Tax:$",tax)
                print("Total:$",finalprice)
                choice=str(input("Do you want to continue order? \nplease enter yes or no:"))
                if choice=="no":
                    break
            elif drink=="3":
                price=PP+RW
                print("Pasta Primavera ( $11.50)")
                print("Red wine($4.99)")
                tax=round(price*0.08,2)
                finalprice=round(tax+price,2)
                print("Tax:$",tax)
                print("Total:$",finalprice)
                choice=str(input("Do you want to continue order? \nplease enter yes or no:"))
                if choice=="no":
                    break
        elif meal=="3" and int(age)<21:
            drink=str(input("Please enter the drink you want: \n1)Iced tea($1.99) \n2)Ginger beer ($3.99) \nPlease enter 1or2:"))
            while drink!="1" and drink!="2" and drink!="quit":
                print("System Error, please try again")
                drink=str(input("Please enter the drink you want: \n1)Iced tea($1.99) \n2)Ginger beer ($3.99) \nPlease enter 1or2:"))
            if drink=="quit":
                break
            elif drink=="1":
                price=MC+IT
                print("Macaroni and Cheese ( $9.99)")
                print("Iced tea ($1.99)")
                tax=round(price*0.08,2)
                finalprice=round(tax+price,2)
                print("Tax:$",tax)
                print("Total:$",finalprice)
                choice=str(input("Do you want to continue order? \nplease enter yes or no:"))
                if choice=="no":
                    break
            elif drink=="2":
                price=MC+GB
                print("Smoked Salmon ( $15.99)")
                print("Ginger beer ($3.99)")
                tax=round(price*0.08,2)
                finalprice=round(tax+price,2)
                print("Tax:$",tax)
                print("Total:$",finalprice)
                choice=str(input("Do you want to continue order? \nplease enter yes or no:"))
                if choice=="no":
                    break
        elif meal=="3" and age>=21:
            drink=str(input("Please enter the drink you want: \n1)Iced tea($1.99) \n2)Ginger beer ($3.99) \n3)Beer ($2.59) \nPlease enter 1,2or3:"))
            while drink!="3" and drink!="1" and drink!="2" and drink!="quit":
                print("System Error, please try again")
                drink=str(input("Please enter the drink you want: \n1)Iced tea($1.99) \n2)Ginger beer ($3.99) \n3)Beer ($2.59) \nPlease enter 1,2or3:"))
            if drink=="quit":
                break
            elif drink=="1":
                price=MC+IT
                print("Macaroni and Cheese ( $9.99)")
                print("Iced tea ($1.99)")
                tax=round(price*0.08,2)
                finalprice=round(tax+price,2)
                print("Tax:$",tax)
                print("Total:$",finalprice)
                choice=str(input("Do you want to continue order? \nplease enter yes or no:"))
                if choice=="no":
                    break
            elif drink=="2":
                price=MC+GB
                print("Smoked Salmon ( $15.99)")
                print("Ginger beer ($3.99)")
                tax=round(price*0.08,2)
                finalprice=round(tax+price,2)
                print("Tax:$",tax)
                print("Total:$",finalprice)
                choice=str(input("Do you want to continue order? \nplease enter yes or no:"))
                if choice=="no":
                    break
            elif drink=="3":
                price=MC+BE
                print("Smoked Salmon ( $15.99)")
                print("Beer ($2.59)")
                tax=round(price*0.08,2)
                finalprice=round(tax+price,2)
                print("Tax:$",tax)
                print("Total:$",finalprice)
                choice=str(input("Do you want to continue order? \nplease enter yes or no:"))
                if choice=="no":
                    break
        else:
            print("System Error, please try again.")
