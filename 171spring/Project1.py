'''
The worse currencies to convert between are US dollars and CD dollars because the racial between the two are very close which makes me get confuse.
'''
user1=int(input("please enter the amount:"))
choice="no"
answer=0
user2=input("1)US \n2)EU \n3)CD \nPlease enter the currency you enter or enter Quit:")
while user2!="1" and user2!="2" and user2!="3" and user2!="Quit":
    print("System error, please try it again.")
    user2=input("1)US \n2)EU \n3)CD \nPlease enter the currency you enter:")
if user2=="Quit":
    choice="Quit"
while choice!="Quit":        
    user3=input("1)US \n2)EU \n3)CD \nPlease enter the currency you want to covert or enter Quit: ")
    if user3=="Quit":
        choice="Quit"
    while user3!="1" and user3!="2" and user3!="3" and user3!="Quit":
        print("System error, please try it again.")
        user3=input("1)US \n2)EU \n3)CD \nPlease enter the currency you want to covert or enter Quit: ")
    while user2==user3:
        print("Sorry, you can covert same currency, please try other.")
        user3=user3=int(input("1)US \n2)EU \n3)CD \nPlease enter the currency you want to covert:"))
    if user2=="1" and user3=="2":
        answer=user1*0.705389
        choice=input("If you want to continue, please press any key \notherwise please enter:Quit.")
    elif user2=="1" and user3=="3":
        answer=user1*1.15584
        choice=input("If you want to continue, please press any key \nOtherwise please enter:Quit.")
    elif user2=="2" and user3=="1":
        answer=user1*1.139096
        choice=input("If you want to continue, please press any key \notherwise please enter:Quit.")
    elif user2=="2" and user3=="3":
        answer=user1*1.40762
        choice=input("If you want to continue, please press any key \notherwise please enter:Quit.")
    elif user2=="3" and user3=="1":
        answer=user1*0.694646
        choice=input("If you want to continue, please press any key \notherwise please enter:Quit.")
    elif user2=="3" and user3=="2":
        answer=round(user1*0.490593)
        choice=input("If you want to continue, please press any key \notherwise please enter:Quit.")
    else:
        print("End.")
if user2=="1" and user3=="2":
    print("_________________________")
    print("EU is:",answer)
elif user2=="1" and user3=="3":
    print("_________________________")
    print("CD is:",answer)
elif user2=="2" and user3=="1":
    print("_________________________")
    print("US is:",answer)
elif user2=="2" and user3=="3":
    print("_________________________")
    print("CD is:",answer)
elif user2=="3" and user3=="1":
    print("_________________________")
    print("US is:",answer)
elif user2=="3" and user3=="2":
    print("_________________________")
    print("Eu is:",answer)
else:
    print("end")
    
