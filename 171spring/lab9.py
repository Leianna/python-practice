# NOTE: You may not use any complex list functions (sum, slice, sort, etc.)
import math

def mean(numList):
    '''
    finds the mean (average) of the list
    :param numList: a list of numbers
    :raises: ValueError if sent an empty list
    :returns: the mean (average) of the list
    '''
    pass

def meanTest():
    print("---- mean Test ----")
    #simple case
    meanTest = mean([2, 4, 6])
    print("should be 4:", meanTest)
    #1 item
    meanTest = mean([2])
    print("should be 2:", meanTest)
    # bunch of numbers
    meanTest = mean([600, 470, 170, 430, 300])
    print("should be 394:", meanTest)
    #order shouldn't matter
    meanTest = mean([ 470, 430, 170, 300, 600])
    print("should be 394:", meanTest)
    #raises error correctly when given empty list
    try:
        mean([])
        print("PROBLEM, this should never print")
    except ValueError as excpt:
        print("Should be 'can't average empty list'") 


def numsBelow(numList, threshold):
    '''
    finds all numbers in the list below a certain threshold
    :param numList: a list of numbers
    :threshold: the cutoff (only numbers below this will be included)
    :returns: a new list of all numbers from numList below the threshold
    '''
    pass

def numsBelowTest():
    print("---- numsBelowTest ----")
    #below numbers spread out, not in order, checks threshold
    testNums = [6, -3, 2, 10, 12, 5]
    belowNums = numsBelow(testNums, 6)
    print("should be [-3, 2, 5]:", belowNums)
    #no side effects
    print("should be [6, -3, 2, 10, 12, 5]:", testNums)
    belowNums = numsBelow(testNums, -4)
    #if no numbers are below
    print("should be []:", belowNums)
    #no side effects
    print("should be [6, -3, 2, 10, 12, 5]:", testNums)
    #single number in list
    belowNums = numsBelow([4], 6)
    print("should be [4]:", belowNums)
    #no numbers in list
    belowNums = numsBelow([], 6)
    print("should be []:", belowNums)


def numsAbove(numsToCheck, threshold, listToAddHighNums):
    '''
    finds all numbers in the list above a certain threshold
    :param numList: a list of numbers
    :threshold: the cutoff (only numbers above this will be included)
    :side effect: all numbers from numsToCheck above the threshold are added
                  to the end of listToAddHighNums 
    '''
    pass

def numsAboveTest():
    print("---- numsAboveTest ----")
    testNums = [6, -3, 2, 10, 12, 5]
    aboveNums = []
    numsAbove(testNums, 5, aboveNums)
    #check side effect on second list
    print("should be [6, 10, 12]:", aboveNums)
    #no side effects on 1st list
    print("should be [6, -3, 2, 10, 12, 5]:", testNums)

    #add more numbers to aboveNums by calling again
    testNums = [-2, 6, 3, 5, 1]
    numsAbove(testNums, 3, aboveNums)
    #check side effect on second list
    print("should be [6, 10, 12, 6, 5]:", aboveNums)
    #no side effects on 1st list
    print("should be [-2, 6, 3, 5, 1]:", testNums)

    #if no numbers are above
    aboveNums = []
    numsAbove([3, 8, 4, 9, 5], 12, aboveNums)
    print("should be []:", aboveNums)
    #no numbers in list
    numsAbove([], 6, aboveNums)
    print("should be []:", aboveNums)
    #single number in list
    numsAbove([8], 6, aboveNums)
    print("should be [8]:", aboveNums)


def variance(numList):
    '''
    calculates the variance of a list, see:
    http://www.mathsisfun.com/data/standard-deviation.html
    for detail of variance
    :param numList: a list of numbers of which to find the variance
    :raises: ValueError if the list is empty
    :returns: the variance of numList
    '''
    #use the mean function
    pass

def varianceTest():
    #TODO - tests must check that the function:
    # calculates correctly in different scenarios
    # does not have side effects
    # raises error correctly when sent empty list
    pass

def stdDev(numList):
    '''
    calculates the standard deviation of a list, see:
    http://www.mathsisfun.com/data/standard-deviation.html
    for detail of standard deviation
    :param numList: a list of numbers of which to find the standard deviation
    :raises: ValueError if the list is empty
    :returns: the standard deviation of numList
    '''
    #use the variance function, and math.sqrt function
    pass

def stdDevTest():
    #TODO - tests must check that the function:
    # calculates correctly in different scenarios
    # does not have side effects
    # raises error correctly when sent empty list
    pass

def test():
    meanTest()
    numsBelowTest()
    numsAboveTest()
    varianceTest()
    stdDevTest()

def main():
    # sample list from stats website
    # myList = [600, 470, 170, 430, 300]
    myList = [88, 86, 77, 92, 100, 84, 79, 32, 68, 98, 44, 66, 77, 77, 78, 82, 84, 79, 12]
    #TODO:
    # use the mean, stdDev, numsAbove, and numsBelow functions to report
    # all the numbers in a list that are more than one standard deviation
    # away from the mean
    # print the original list, the mean, the standard deviation,
    # and the list of "outliers"
    pass
    
#test()
main()
