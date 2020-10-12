from dice import Dice
#from pythonPokeher import PokerApp

class TextInterface:
    def __init__(self):
        print("Welcome to my video Poker Game")

    def setMoney(self, amt):
        print("You currently have ${0}.".format(amt))

    def setDice(self, values):
        print("Dice: ", values)

    def wantToPlay(self):
        ans = input("Do you wish to try your luck? ")
        return ans[0] in "yY"

    def close(self):
        print("\nThanks for Playing")

    def showResult(self, msg, score):
        print("{0}. You Win ${1}.".format(msg, score))

    def chooseDice(self):
        return eval(input("Enter list of which to change ([] to stop) "))
