import random

def checkForWinner(p1Choice, p2Choice):
    '''
    Checks who won considering the two players' choices
    :param p1Choice: a string representing player1's choice
    :param p2Choice: a string representing player2's choice
    :returns: "player1", "player2", "tie" depending on who won,
              or "invalid" if either choice is not a valid option
    '''
    if p1Choice=="rock" and p2Choice=="paper":
        winner="player2"
    elif p1Choice=="rock" and p2Choice=="scissors":
        winner="player1"
    elif p1Choice=="scissors" and p2Choice=="paper":
        winner="player1"
    elif p1Choice=="scissors" and p2Choice=="rock":
        winner="player2"
    elif p1Choice=="paper" and p2Choice=="scissors":
         winner="player2"
    elif p1Choice=="paper" and p2Choice=="rock":
        winner="player1"
    else:
        winner="equal"
    return winner

def checkForTypo(userchoice):
    '''
    Checks if the given string is a valid game choice
    :param choice: a string representing the choice a player made
    :return: True, if the choice is "rock", "paper", or "scissors", false otherwise
    '''
    # TODO part 2
    if userchoice=="rock" or userchoice=="paper" or userchoice=="scissors":
        return True
    else:
        return False
    

def computerChoice():
    '''
    Makes a choice for the computer
    :return: one of the strings "rock", "paper", or "scissors"
    '''
    # TODO part 2
    # make a random choice
    comchoice=random.randint(0,3)
    if comchoice==1:
        comchoice="scissors"
    elif comchoice==0:
        comchoice="paper"
    else:
        comchoice="rock"
    return comchoice
    
def humanChoice():
    '''
    Continually ask the user to enter a choice of rock, paper or scissors
    until they have entered one of the choices correctly
    :return: the valid choice entered
    '''
    # TODO part 2
    # use the checkForTypo function to accomplish your task
    userchoice=input("Please enter rock,paper,scissors:")
    e=checkForTypo(userchoice)
    while e!=True:
        userchoice=input("Sorry, please enter rock,paper,scissors:")
        e=checkForTypo(userchoice)
    return userchoice
               
    
def rpsRound():
    '''
    Plays 1 round of rock, paper, scissors
    User input will control 1 player, computer will control the other
    :post: prints the winner and the results of the round
    :return: a string representing the winner
    '''
    player1 = humanChoice()
    player2 = computerChoice()
    winner = checkForWinner(player1, player2)
    print (winner, "wins:\t P1:", player1, "\tP2:", player2)
    return winner
    

def rpsGame():
    '''
    Plays rounds of rock, paper scissors until one of the players gets a score of 2,
    (could be many rounds if players tie several times)
    :post: prints the results of each round, and the overall winner in the end
    '''
    # TODO part 3
    # use the rpsRound function and let it print the results of each round
    count=0
    count1=0
    while count!=2 and count1!=2:
        result=rpsRound()
        if result=="player1":
            count+=1
        elif result=="player2":
            count1+=1
        print("Human:",count)
        print("computer:",count1)
    if count==2:
        print("The winner is player 1.")
    elif count1==2:
        print("The winner is player 2.")

'''def test():
    # TODO part 1: tests for checkForTypo

    # TODO part 1: tests for computerChoice, why will this be different than other tests

    # Why can't we write automated tests for humanChoice, rpsRound, or rpsGame?

    # tests for checkForWinner
    testWin = checkForWinner("rock", "rock")
    print("should be tie:", testWin)
    testWin = checkForWinner("paper", "paper")
    print("should be tie:", testWin)
    testWin = checkForWinner("scissors", "scissors")
    print("should be tie:", testWin)

    testWin = checkForWinner("rock", "scissors")
    print("should be player1:", testWin)
    testWin = checkForWinner("paper", "rock")
    print("should be player1:", testWin)
    testWin = checkForWinner("scissors", "paper")
    print("should be player1:", testWin)

    testWin = checkForWinner("rock", "paper")
    print("should be player2:", testWin)
    testWin = checkForWinner("paper", "scissors")
    print("should be player2:", testWin)
    testWin = checkForWinner("scissors", "rock")
    print("should be player2:", testWin)

    testWin = checkForWinner("rock", "")
    print("should be invalid:", testWin)
    testWin = checkForWinner("paper", "sscissors")
    print("should be invalid:", testWin)
    testWin = checkForWinner("scissors", "ROCK")
    print("should be invalid:", testWin)
    testWin = checkForWinner("BLOCK", "paper")
    print("should be invalid:", testWin)
    testWin = checkForWinner("paperrr", "scissors")
    print("should be invalid:", testWin)
    testWin = checkForWinner("scisors", "rock")
    print("should be invalid:", testWin)
 '''   

def main():
    # TODO part 3
    # allow the user to play more games until they choose to quit
    rpsGame()
    w=input("Do you want to play another round? \nPlease press any key to start or press quit:")
    while w!="quit":
        rpsGame()
main()
