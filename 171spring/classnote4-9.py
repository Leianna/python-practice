'''
def addFive(num):
    '''
#    adds 5 to any number
    '''
    pass

def addFiveToEachItem(myList):
    '''
#    adds 5 to every item in a list
    '''
    for x in range(len(mylist)):
        mylist[x]=mylist[x]+5
    return mylist

def main():
    testNum = 10
    testNum2 = addFive(testNum)
    print("Should be 10:", testNum)
    print("Should be ???:", testNum2)

    testList = [2, 4, 6]
    testList2 = addFiveToEachItem(testList)
    print("Should be [2, 4, 6]:", testList)
    print("Should be ???:", testList2)

main()
'''

def findMax(aList):
    '''
    returns the maximum value from the list
    :aList: a list of values (should not be empty)
    :returns: the largest value in the list, or
    '''
    pass

def changeNumbersShift(numList, amtToShift):
    '''
    add a certain amount to each number in the list
    :numList: the list of numbers to add to
    :amtToShift: the amount to add to each number
    :side effect: each number in list is increased
    '''
    pass


def newNumbersShift(numList, amtToShift):
    '''
    add a certain amount to each number in the list
    :numList: the list of numbers to add to
    :amtToShift: the amount to add to each number
    :returns: a new list with all numbers from the old list increased
    '''
    pass

def shiftGrades(gradesList):
    '''
    if no student got higher than a 90, shift so that the top achieving
    student gets a 95
    '''
    pass

def test():
    pass
    

def main():
    pass

test()
# main()
    
