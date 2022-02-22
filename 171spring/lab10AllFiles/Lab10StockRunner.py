from lab10v0 import getCleanDataFromFile, calcDayChangeAndVolatility, totalChangeAndVolatility 
'''
Stock Processing based on files downloaded from NASDAQ
4/26/2018
Authors: Toby Dragon
'''

def processFileAndShowWork(filename):
    '''
    processes an historical stack data file and calculates the change and Volatlity over the whole period
    :param filename: the filename of the stock history file (a string)
    :returns: a list containing the stock name, the total change, and average Volatilty, example:
            ['Test', 1.5, 1.525]
    '''
    cleanData = getCleanDataFromFile(filename)
    print(["date","close","volume","open","high","low"])
    for i in range(len(cleanData)):
        print(cleanData[i])
    print() 

    calcData = calcDayChangeAndVolatility(cleanData)
    print(["date  ","change","Volatility"])
    for i in range(len(calcData)):
        print(calcData[i])
    print()

    finalData = totalChangeAndVolatility(filename, calcData)
    return finalData
    

def main():

    fileName = "AAPL-HistoricalQuotes.csv"
    results = processFileAndShowWork(fileName)
    
    print(["name", "total change", "avg Volatility"])
    print(results)

main()
    
    
