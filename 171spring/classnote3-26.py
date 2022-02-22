def main():
    mystr="House"
    print(mystr)
    x=len(mystr)
    print("the length",mystr,"is",x)
    anotherstr="my"
    mystr+=anotherstr
    for i in range(0,len(mystr),2):
        print(mystr[i])
    for z in range(len(mystr),0,-2):
        print(mystr[z])
main()
