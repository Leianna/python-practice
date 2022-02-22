
def createPresList(filenameStr):
    '''
    reads a file with information about presidents and their terms and creates
    a useful list of that information
    :param filenameStr: a file that should be read
    :returns: ???
    '''
    file=open(filenameStr)
    file.close()

    newfile=[]
    print(file)
            

def createPresListTest():
    #test that it creates everything from short example file correctly
    #test that it can read the long file, that the list has the right number of rows,
    #and that the first and last entries in the long file are correct
    pass

def findPresByYear(presList, year):
    '''
    returns the name of the person who was president during a given year
    :param presList: ???
    :param year: an int representing the year (4 digits)
    :raises: ValueError if there is no president during the given year
    :returns: a string representing the name of the president
    '''
    

def findPresByYearTest():
    #hardcode short examples of the presList, call your function to make sure it works
    pass

def test():
    createPresListTest()
    findPresByYearTest()

def main():
    presidents = createPresList("171-52-PresComplete.txt")
    #year = int(input("Enter a year to see the president:"))
    #pres = findPresByYear(presidents, year)
    #print(pres)

#test()
main()
