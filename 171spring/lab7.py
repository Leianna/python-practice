# NOTE: You may not use any complex string functions (find, count, slice, split, etc.)

def find(strToSearch, strToFind):
    '''
    finds the first occurrence of strToFind inside of strToSearch
    :param strToSearch: the string to look through
    :param strToFind: the string to look for (single character)
    :return: the index of the first appearance of strToFind, or -1 if either
             it is not present or strToFind is not a single character
    '''
    for x in range(len(strToSearch)):
        if strToSearch[x]==strToFind:
            return x
    if (strToFind not in strToSearch) or (len(strToFind)>=2):
        return -1
    

def count(strToSearch, strToCount):
    '''
    counts the number of times strToCount appears inside of strToSearch
    :param strToSearch: the string to look through
    :param strToCount: the string to look for (single character)
    :return: the count of the number of appearances of strToFind,
             or 0 if either it is not present or -1 if strToFind is not
             a single character
    '''
    count=0
    if len(strToCount)==1:
        for y in range(len(strToSearch)):
            if strToSearch[y]==strToCount:
                count+=1
        return count
    elif len(strToCount)>=2:
        return -1
    else:
        return 0
            

def strSlice(strToSlice, startIndex, stopIndex):
    '''
    builds the slice of strToFind from startIndex to stopIndex
    :param strToSlice: the string from which a piece will be taken
    :param startIndex: the index of the first character to include (not negative)
    :param stopIndex: the index of the first character that is not included (not negative)
    :return: the string of all characters from startIndex to one less than stopIndex,
             or empty string if the indices are invalid in any way
    '''
    if startIndex>=0 and stopIndex>startIndex and stopIndex<=len(strToSlice):
        Slice=strToSlice[startIndex:stopIndex]
    else:
        Slice=""
    return Slice

def firstWord(strToSplit):
    '''
    gives the first word from a string.  A word is a sequence of letters followed
    by white space (space, tab or newline characters)
    :param strToSlice: the string from which the first word will be taken
    :return: the first word of the string (up to 1st space),
             or the entire string if no space is present
    '''
    for i in range(len(strToSplit)):
        if strToSplit[i]==" ":
            return strToSplit[0:i]
    if " " not in strToSplit:
        return strToSplit

def testFind():
    print("-----Testing find:")
    #one at the beginning
    testIndex = find("hello", "h")
    print("should be 0:", testIndex)
    #one in the middle
    testIndex = find("hello", "e")
    print("should be 1:", testIndex)
    #one at the end
    testIndex = find("hello", "o")
    print("should be 4:", testIndex)
    #when there is more than 1 of the same
    testIndex = find("hello", "l")
    print("should be 2:", testIndex)
    #only thing present
    testIndex = find("t", "t")
    print("should be 0:", testIndex)
    #not present
    testIndex = find("hello", "t")
    print("should be -1:", testIndex)
    #empty string
    testIndex = find("", "t")
    print("should be -1:", testIndex)
    #sent more than single character
    testIndex = find("hello", "ll")
    print("should be -1:", testIndex)
    print("-----Done Testing find\n")
    
def testCount():
    print("-----Testing count:")
    #TODO
    #count
    Count=count("happy", "h")
    print("shoule be 1:",Count)
    #more repeat letter
    Count=count("mississippi", "s")
    print("shoule be 4:",Count)
    #sentence
    Count=count("wish you have a beautiful day", "a")
    print("shoule be 3:",Count)
    print("COMPLETE")
    print("-----Done Testing count\n")

def testStrSlice():
    print("-----Testing Slice:")
    #slice from middle
    testIndex = strSlice("hello", 2, 4)
    print("should be ll:", testIndex)
    #slice from start
    testIndex = strSlice("hello", 0, 3)
    print("should be hel:", testIndex)
    #slice to end
    testIndex = strSlice("hello", 2, 5)
    print("should be llo:", testIndex)
    #entire slice
    testIndex = strSlice("hello", 0, 5)
    print("should be hello:", testIndex)
    #slice of 1
    testIndex = strSlice("hello", 1, 2)
    print("should be e:", testIndex)
    #slice of nothing
    testIndex = strSlice("hello", 2, 2)
    print("should be empty, no space, dashes touching:-"+ testIndex+"-")
    #end before start
    testIndex = strSlice("hello", 2, 1)
    print("should be empty, no space, dashes touching:-"+ testIndex+"-")
    #start negative
    testIndex = strSlice("hello", -1, 3)
    print("should be empty, no space, dashes touching:-"+ testIndex+"-")
    #end negative
    testIndex = strSlice("hello", 0, -2)
    print("should be empty, no space, dashes touching:-"+ testIndex+"-")
    #end too large
    testIndex = strSlice("hello", 2, 8)
    print("should be empty, no space, dashes touching:-"+ testIndex+"-")
    print("-----Done Testing slice\n")

def testFirstWord():
    print("-----Testing firstWord:")
    #TODO
    #full snetence
    FirstWord=firstWord("Wish you have a great day.")
    print("The first word shoule be Wish:",FirstWord)
    #One string
    FirstWord=firstWord("Understand")
    print("The first word shoule be Understand:",FirstWord)
    #one letter
    FirstWord=firstWord("A book cost $10.")
    print("The first word shoule be A:",FirstWord)
    print("COMPLETE")
    print("-----Done Testing count\n")

def test():
    testFind()
    testCount()
    testStrSlice()
    testFirstWord()
    pass

def main():
    # ask user to enter a sentence
    # Use functions above to split the sentence into words
    # and print each word on a separate line
    user=input("Please enter a sentence:")
    first=firstWord(user)
    print(first)
    strSlice(strToSlice, startIndex, stopIndex)
    
        
#test()
main()
