
def palindorme(word):
    '''
    Check if it's palindorme by comparing the word to it's backward.
    '''
    word=lower(word)
    backward=""
    for x in range(len(word)-1,-1,-1):
        backward+=word[x]
    if backward==word:
        return True
    else:
        return False

def anagram(word,word1):
    '''
    Check if it's anagram by makesure all the character in word are also in words.
    '''
    word=lower(word)
    word1=lower(word1)
    count=0
    if len(word)==len(word1):
        for x in range(len(word)):
            if word[x] in word1:
                count+=1
        if count==len(word):
            return True
        else:
            return False
    else:
        return False
        

def lower(word):
    '''
    all lowercase to make it easy to check.
    '''
    word=word.lower()
    return word

def testpalindorme():
    #uncorrect answer
    word="yes"
    num=palindorme(word)
    print("False:",num)

    #correct anwer
    word="level"
    num=palindorme(word)
    print("True:",num)


def testanagram():
    #two word have different length
    word="yes"
    word1="no"
    num=anagram(word,word1)
    print("False:",num)

    #two word have same length, and correct answer
    word="dog"
    word1="god"
    num=anagram(word,word1)
    print("True:",num)

    #two word have same length, but contains different letter
    word="first"
    word1="texts"
    num=anagram(word,word1)
    print("False:",num)


def testlower():
    #all capitalize
    word="YES"
    num=lower(word)
    print("yes:",num)

    #most capitalize
    word="HAPpY"
    num=lower(word)
    print("happy:",num)

    #all lowercase
    word="yes"
    num=lower(word)
    print("yes:",num)
    
def test():
    testlower()
    testanagram()
    testpalindorme()
pass

    

def main():
    """
    enter the choice and word, and then print the answer.
    """
    choice="1"
    while choice!="quit":
        choice=input("What you want to check \nPlease enter anagram, palindorm or quit:")
        word=input("enter a word:")
        if choice=="anagram":
            word1=input("enter the anagram of the word:")
            while word1==word:
                word1=input("Sorry you can't enter same word, please enter again:")
            answer=anagram(word,word1)
            if answer==True:
                print("It is anagram!")
                choice=input("Do you want to continue?\nPlease enter any key to continue or enter quit:")
            else:
                print("No it is not anagram.")
                choice=input("Do you want to continue?\nPlease enter any key to continue or enter quit:")

        else:
            answer=palindorme(word)
            if answer==True:
                print("It is palindrome!")
                choice=input("Do you want to continue?\nPlease enter any key to continue or enter quit:")

            else:
                print("No it isn't palindrome.")
                choice=input("Do you want to continue?\nPlease enter any key to continue or enter quit:")
#test()
main()
