def findMax(aList):
    '''
    returns the maximum value from the list
    :aList: a list of values (should not be empty)
    :returns: the largest value in the list, or
    '''
    '''
    a=max(alist)
    return a
    '''
    if len(aList) <= 0:
        return aList
    maxValue = aList[0]
    for i in range(len(aList)):
        if aList[i] > maxValue:
            maxValue = aList[i]
    return maxValue

def changeNumbersShift(numList, amtToShift):
    '''
    add a certain amount to each number in the list
    :numList: the list of numbers to add to
    :amtToShift: the amount to add to each number
    :side effect: each number in list is increased
    '''
    for i in range(len(numList)):
        numList[i] = numList[i] + amtToShift


def newNumbersShift(numList, amtToShift):
    '''
    add a certain amount to each number in the list
    :numList: the list of numbers to add to
    :amtToShift: the amount to add to each number
    :returns: a new list with all numbers from the old list increased
    '''
    newList = []
    for i in range(len(numList)):
        newList.append(numList[i] + amtToShift)
    return newList

def shiftGrades(gradesList):
    '''
    if no student got higher than a 90, shift so that the top achieving
    student gets a 95
    '''
    pass

def testMax():
    try:
        val = findMax([1,2,30,40,100]);
        print("max of [1,2,30,40,100] should be 100, get:", val)
        val = findMax([100,2,30,40,100]);
        print("max of [100,2,30,40,100] should be 100, get:", val)
        val = findMax([100,2,30,40,10]);
        print("max of [100,2,30,40,10] should be 100, get:", val)
        val = findMax([-1, -2, -3, -4, -5]);
        print("max of [-1, -2, -3, -4, -5] should be -1, get:", val)
        val = findMax([-5, -2, -3, -4, -1]);
        print("max of [-5, -2, -3, -4, -1] should be -1, get:", val)
        val = findMax([]);
        print("max of [] should be [], get:", val)
    except ValueError as excpt:
        print(excpt)

def testChangeNumbersShift():
    testList = [1,2,30,40,100]
    changeNumbersShift(testList, 5);
    print("Shift [1,2,30,40,100] by 5, get:", testList)

def testnewNumbersShift():
    testList = [1,2,30,40,100]
    newList = newNumbersShift(testList, 5);
    print("Shift [1,2,30,40,100] by 5, old list is:", testList, "New list is:", newList)
    

def test():
    testMax()
    testChangeNumbersShift()
    testnewNumbersShift()
    

def main():
    pass

test()
# main()
    
