 '''for i in range(55,22,-3):
    print(i)'''
def p(s):
    x= len(s)
    for i in range(x):
        print(s[i])

def r(s):
    x = len(s) - 1
    while x >= 0:
        print (s[x])
        x = x-1

def main():
    p("hey")
    print("\n,now\n")
    r("eyb")

main()
