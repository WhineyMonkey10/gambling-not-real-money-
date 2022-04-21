import random
import math
balance = 100000
def logBal():
    ("Your current balance is {balance}, you have made {balance - 100000}$ so far. You need {1000000000 - balance} more dollars to win.")
def resetBalance():
    balance = 100000
def getBal():
    return balance
def setbalance(amount):
    balance = amount
def getgamePlay():
   gametoplay = input(f"What game would you like to play (roulette, slots)? {logBal} ").lower()
   return gametoplay

gametoplay = getgamePlay()


if gametoplay == ("roulette"):
    balance = logBal
    print("You walk up to a free roulette table. \nA worker tells you to take a seat and to place your bets \n")
    betforroulette = int(input(f"What is your bet, your current balance is: {balance}: "))
    if betforroulette > getBal():
        print(f"Thats to much.\nYou need {betforroulette - balance} more")
    print(f"You bet {betforroulette}.\n")
    rouletteplacenum = int(input("What number do you want to place your bets on? (1 - 31)\n"))
    if rouletteplacenum > 31:
         print("That's not a valid number. The roulette worker tells you to leave if you're going to be trolling. You get kicked out.")
         exit()
    else:
        print(f"You place your {betforroulette}$ bet on number {rouletteplacenum}")
        roulettenumland = random.randint(1, 31)
        print("The worker spins the wheel...\n")
        if rouletteplacenum == roulettenumland:
            print(f"It lands on {roulettenumland} and you win! Since you bet {betforroulette} your bet gets doubled, meaning you won {betforroulette * 2}$ Your balance is now {balance + betforroulette * 2}")
            balance = int((betforroulette * 2))
            setbalance(balance)
            getgamePlay()
        else:
            print(f"It lands on {roulettenumland} and you loose! Since you bet {betforroulette} your bet gets taken by the house, meaning you lost {betforroulette}$ Your balance is now {balance - betforroulette}")
            balance = int((balance - betforroulette))
            setbalance(balance)
            getgamePlay()
if gametoplay == ("slots"):
    print("You walk up to the slots machine. \nYou see the machine and it askes you what you want to bet")
    betforslots = int(input(f"What is your bet, your current balance is: {balance}: "))
    bet = slotsplay(betforslots)
   
    if bet == False :
        print(f"You dont have enough money. You need {betforslots - balance}")
       
    elif bet == 'loss':
        print(f"You lost {betforslots}$")
        getgamePlay()
    else:
        print(f"You won {bet}")
        getgamePlay()

def slotsplay(bet):
    slot1 = random.randint(1, 5)
    slot2 = random.randint(1, 5)
    slot3 = random.randint(1, 5)
    if balance >= bet:
        balance -= bet
    else:
        return False
    if slot1 == slot2 and slot2 == slot3:
        return math.floor(bet * ((slot1 + 1) / 1.5))
    else:
        return "loss"

getBal(1)

print("Welcome to Mr.Fries casino!\nWe have 3 games to play:\nRoulette\nSlot Machines\nRandom Number ")
getgamePlay()

