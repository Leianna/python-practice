
hour=int(input("Time:"))
while hour>12:
    hour=input("Time:")
apm=input("am or pm:")
if hour>=10 and apm=="pm":
    print("too late")
elif hour<=8 and apm=="am":
    print("too early")
else:
    print("you can call your grandmother.")
