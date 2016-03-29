import random as r
import time as t

sleep = 0
 
def displayIntro():
    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2' and cave != '3':
        print('Which cave will you go into? (1, 2, or 3)')
        cave = input()

    return cave

def fight(chosenCave, friendlyCave):
    action = ''
    while action != 'run' and action != 'fight':
        print('Do you want to run away, or stand and fight? (run or fight)')
        action = input()
        
    if action == 'fight':
        if chosenCave == str(friendlyCave):
            print('Gives you his treasure!')
        else:
            print('Gobbles you down in one bite!')
    else:
        print('COWARD!')
    

def checkCave(chosenCave):
    print('You approach the cave...')
    t.sleep(r.randint(0,sleep))
    print('It is dark and spooky...')
    t.sleep(r.randint(0,sleep))
    
    if chosenCave == '3':
        print('You see a merchant.  He has treasures for sale.')
        print('Do you want to buy, or try to steal them? (buy or steal)')
        merchant = input()
        if merchant != 'buy' and merchant != 'steal':
            survivalChance = r.randint(1,50)
            deathChance = r.randint(1,30)
            if deathChance > survivalChance:
                print('Your incomprehensible desires have, in turn, brought you to an incomprehensible death!')
            else:
                print("Invalid selection! You are now being warped to the glitch-zone...")
                t.sleep(2)
                print("Welcome to the glitch-zone! There is no hope of redemption out of here, unfortunately. Do you wish to 'sulk' for the rest of your life or try to 'call' 911?")
                choice = input()
                if 'call' == choice:
                    print("Upon realizing that there is a lack of Verizon towers in the glitch-zone, you find yourself trapped in the zone for the rest of your days.")
                else:
                    print ("You sulk disparingly for the rest of your sorrow filled days, until you reach the pitiful end.")
                    
              
        elif merchant == 'buy':
            cash = r.randint(500,1000)
            treasure = r.randint(500,1000)
            if treasure > cash:
                print('That\'s too expensive!')
            else:
                print('Enjoy your treasures!')
        else:
            health = r.randint(1,10)
            merchantHealth = r.randint(1,10)
            if merchantHealth > health:
                print('You have been defeated by the merchant!')
            else:
                print('You showed him!  Enjoy your ill-gotten gains!')
    else:
        print('A large dragon jumps out in front of you! He opens his jaws and...')
        print()
        t.sleep(r.randint(0,sleep))

        friendlyCave = r.randint(1, 3)

        fight(chosenCave, friendlyCave)
        
        

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    displayIntro()

    caveNumber = chooseCave()

    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()

