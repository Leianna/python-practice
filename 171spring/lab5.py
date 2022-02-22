import math

def convertDistance(convType, length):
    '''
    Converts the length from english to metric or from metric to english
    :param convType: a string representing type of conversion necessary,
                     if the string is 'e2m' or 'E2M', convert feet to meters
                     if the string is 'm2e' or 'M2E', convert meters to feet
                     any other value does no conversion
    :param amt: a float to represent the length in original units (feet or meters)
    :return: a float to represent the length in the new units (feet or meters),
             or original length if convType is not recognized
    '''
    # TODO
    if convType=="e2m" or convType=="E2M":
        length=float(length*0.3048)
    elif convType=="m2e" or convType=="M2E":
        length=float(length*3.28084)
    else:
        length=float(length)
    return length

def computeArea(convType, length, width):
    '''
    Converts the length and width (if necessary) and then calculates the area.
    :param aType: a string representing type of conversion necessary,
                  if the string is 'e2m' or 'E2M', convert feet to meters
                  if the string is 'm2e' or 'M2E', convert meters to feet
                  any other value does no conversion
    :param length: length in the original units
    :param width: width in the original units
    :return: the area calculated in the new units
    '''
    # TODO
    # use convertDistance function to convert all measurements, then compute
    Area=float(length*width)
    if convType=="e2m" or convType=="E2M":
        Area=Area*0.3048
    elif convType=="m2e" or convType=="M2E":
        Area=Area*3.28084
    else:
        Area=Area
    return Area

def computeVolume(convType, length, width, height):
    '''
    Converts the length, width, and height (if necessary) and then calculates the volume.
    :param aType: a string representing type of conversion necessary,
                  if the string is 'e2m' or 'E2M', convert feet to meters
                  if the string is 'm2e' or 'M2E', convert meters to feet
                  any other value does no conversion
    :param length: length in the original units
    :param width: width in the original units
    :return: the area calculated in the new units
    '''
    # TODO
    # use convertDistance function to convert all measurements, then compute
    Volume=float(length*width*height)
    if convType=="e2m" or convType=="E2M":
        Volume=Volume*0.3048
    elif convType=="m2e" or convType=="M2E":
        Volume=Volume*3.28084
    else:
        Volume=Volume
    return Volume

def test():
    #convertLength Tests
    testLength = convertDistance('e2m', 1)
    print("l1: should be 0.3...:", testLength)
    testLength = convertDistance('E2M', 23.5)
    print("l2: should be 7.1...:", testLength)
    testLength = convertDistance('m2e', 1)
    print("l3: should be 3.2...:", testLength)
    testLength = convertDistance('M2E', 16.8)
    print("l4: should be 55.1..:", testLength)
    testLength = convertDistance('', 1)
    print("l5: should be 1     :", testLength)
    testLength = convertDistance('me2', 5)
    print("l6: should be 5     :", testLength)
    print()
    #convertArea Tests
    testArea = computeArea('e2m', 2, 4)
    print("a1: should be 0.7...:", testArea)
    testArea = computeArea('E2M', 6.56168, 1.64042)
    print("a2: should be 1.0...:", testArea)
    testArea = computeArea('m2e', 1, 1)
    print("a3: should be 10.7..:", testArea)
    testArea = computeArea('M2E', 2, 4)
    print("a4: should be 86.1..:", testArea)
    testArea = computeArea('e2e', 1, 1)
    print("a5: should be 1.0   :", testArea)
    testArea = computeArea('', 6, 4)
    print("a6: should be 24.0  :", testArea)

    #convertVolume Tests
    # TODO add your tests for volume here
    testVolume=computeVolume('m2e', 10, 10, 10)
    print("V1:shoule be 3280.84:",testVolume)
    
def main():
    # ask the user what type of conversion they'd like:'e2m' or 'm2e'
    # ask the user what calculation they would like to perform:
    # 1 for area calculation or 2 for volume calculation
    # depending on choice, asks for the other necessary information
    choice="yes"
    while choice!="quit":
        convType=input("What type of conversion you enter?\n if it's meter please enter m \n if it's feet please enter e:")
        if convType=="quit":
            break
        else:
            convType2=input("What type of conversion you want to convert\n if it's meter please enter m \n if it's feet please enter e:")
            if convType2=="quit":
                break
            else:
                convType=convType+"2"+convType2
                calculation=input("1)Area \n2)Volume \nWhat calculation you would like to perform:")
                if calculation=="quit":
                    break
                else:
                    length=float(input("Enter the length:"))
                    width=float(input("enter the width"))
                    if calculation=="1":
                        Area=computeArea(convType, length, width)
                        if (convType=='e2m' or convType=='E2M'):
                            print("The area from feet to meters is:",Area,"meters.")
                        elif convType=="m2e" or convType=="M2E":
                            print("The area from meters to feet is:",Area,"feet.")
                        elif convType=="e2e" or convType=="E2E":
                            print("The area from feet to feet is:",Area,"feet.")
                        elif convType=="m2m" or convType=="M2M":
                            print("The area from Meters to meters is:",Area,"meters.")
                    elif calculation=="2":
                        height=int(input("enter the height"))
                        Volume=computeVolume(convType, length, width, height)
                        if (convType=='e2m' or convType=='E2M'):
                            print("The volume from feet to meters is:",Volume,"meters.")
                        elif convType=="m2e" or convType=="M2E":
                            print("The volume from meters to feet is:",Volume,"feet.")
                        elif convType=="e2e" or convType=="E2E":
                            print("The volume from feet to feet is:",Volume,"feet.")
                        elif convType=="m2m" or convType=="M2M":
                            print("The Volume from Meters to meters is:",Volume,"meters.")

                    choice=input("Do you want to continue convert? \nPlease press any key to ocntinue or enter quit:")
    print("end")
       
    # calls the appropriate function and prints results
    pass

# only one of these should be used, switch by changing comment
#test()    
main()
