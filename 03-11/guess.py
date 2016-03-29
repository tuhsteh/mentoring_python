import random as r

target = r.randint(0,10)


tries = 0

while (tries < 5):
    guess = -1
    try:
       guess = int(raw_input("Pick a number. "))
    except ValueError as e:
       print "Bad guess, numbers only!"
       continue
    tries = tries + 1
    if (guess == target):
        print "Proud of you!  You guessed it in %d tries." % (tries)
        break
    elif (guess < target):
        print "How could you! Too Low!"
    elif (guess > target):
        print "How could you! Too High!"

