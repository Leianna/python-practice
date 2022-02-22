num1=float(input("height:"))
num2=float(input("length:"))
num3=float(input("width:"))
wall1=float(num1)*float(num2)
wall2=float(num1)*float(num2)
wall3=float(num1)*float(num3)
wall4=float(num1)*float(num3)
door=7*3
ceiling=float(num2)*float(num3)
area=float(wall1)+float(wall2)+float(wall4)+float(wall4)+float(ceiling)-float(door)
print("Total square footage to be covered is:",area)
paint=float(area)/400
if paint>round(paint):
    paint=round(paint)+1
print("total paint needed: ",paint)
