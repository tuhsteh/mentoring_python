import copy
import random as r


def randomWord():
    fileName = '/usr/share/dict/words'
    words = open(fileName, 'r')
    wordsList = words.readlines()

    return wordsList[r.randint(0,len(wordsList))].strip()


def handleGuess(letter, word, guesses):
    guesses.append(letter)
    try:
        if word.index(letter) >= 0:
            showGameWord(word, guesses)
            if isSolved(word, guesses):
                print('You Did It!')
                return True
    except ValueError as ve:
        pass
    return False


def showGameWord(word, guesses):
    workingCopy = list('_'*len(word))
    for i in guesses:
        if word.index(i) >= 0:
            for w in range(0, len(workingCopy)):
                if word[w] == i:
                    workingCopy[w] = i
    print(' '.join(workingCopy))


def isSolved(word, guesses):
    chars = len(word)
    try:
        for i in range(0,chars):
            if guesses.index(word[i]) < 0:
                return False
    except ValueError as ve:
        return False
    return True



if __name__ == '__main__':
    gameWord = randomWord().lower()
#    print(gameWord)
    
    guesses = []
    
    solved = False
    while(not solved):
        print('Guess a letter:  ')
        letter = input()
        solved = handleGuess(letter, gameWord, guesses)
    