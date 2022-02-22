temp=int(input("Enter the temperture:"))
windy=int(input("windy or not?\n1)yes \n2)no \nPlease enter:"))
if temp>=80:
    print("Always nice")

if 50<=temp and temp<80 and windy==2:
    print("Nice")

if 50<=temp and temp<80 and windy==1:
    print("Chilly")

if 32<=temp and temp<50 and windy==2:
    print("Chilly")

if 32<=temp<50 and windy==1:
    print("Freezing")

if temp<32:
    print("Freezing")
