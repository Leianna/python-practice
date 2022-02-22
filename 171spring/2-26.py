
numberCount = 3
origNumberCount = numberCount
minval=int(input("Enter a number:"))
maxval=minval
total = minval
while numberCount-1 > 0:
    #do input and sum
    num=int(input("Enter a number:")) 
    total = num + total
    if num<minval:
        minval=total
    else:
        maxval=total
    #print new Sum
    print("Total so far:", total)
    #change numberCount
    numberCount = numberCount -1
#find the average
avg = total/origNumberCount
print(avg)
print(minval)
print(maxval)
