 def isCharUpper(charToCheck):
    '''
    checks if a single character is upper case
    :param charToCheck: the 1 character string to check
    :return: True if the string is a single uppercase character, False otherwise
    '''
    if len(charToCheck) <= 0 or len(charToCheck) > 1:
        return False
    elif ord(charToCheck) >= ord("A") and ord(charToCheck) <= ord("Z"):
        return True
    else:
        return False

def charToLower(charToConvert):
    '''
    gives the lowercase version of a single uppercase letter
    :param charToConvert: the 1 character string to make lower
    :return: the matching lowercase character if the string is a single uppercase character,
             otherwise an empty string
    '''


def strToLower(strToConvert):
    '''
    makes an all lowercase version of strToConvert
    :param strToConvert: the 1 character string to make lower
    :return: a matching string but with any uppercase letters replaced with lowercase letters
    '''
    pass


def test():
    rslt = isCharUpper("A")
    print("isCharUpper('A') should be True returns:", rslt)
    rslt = isCharUpper("a")
    print("isCharUpper('a') should be False returns:", rslt)
    rslt = isCharUpper("H")
    print("isCharUpper('H') should be True returns:", rslt)
    rslt = isCharUpper("h")
    print("isCharUpper('h') should be False returns:", rslt)
    rslt = isCharUpper("A")
    print("isCharUpper('A') should be True returns:", rslt)
    rslt = isCharUpper("z")
    print("isCharUpper('z') should be False returns:", rslt)
    rslt = isCharUpper("1")
    print("isCharUpper('1') should be False returns:", rslt)
    rslt = isCharUpper("%")
    print("isCharUpper('%') should be False returns:", rslt)
    rslt = isCharUpper("")
    print("isCharUpper('') should be False returns:", rslt)

def main():
    sentence = input("Enter a string:")
    lowerSentence = strToLower(sentence)
    print ("The lowercase version of that string is:")
    print(lowerSentence)

test()
#main()
    
            
    
