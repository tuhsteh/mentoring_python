import copy
import random as r


def randomWord():
    fileName = '/usr/share/dict/words'
    words = open(fileName, 'r')
    wordsList = words.readlines()

    return wordsList[r.randint(0,len(wordsList))]


def handleGuess(letter, word, guesses):
    import ipdb
    ipdb.set_trace()
    guesses.append(letter)
    if word.index(letter) >= 0:
        showGameWord(word, guesses)
        isSolved(word, guesses)
    return False


def showGameWord(word, guesses):
    # immutable list!!!
    workingCopy = '_'*len(word)
    for i in guesses:
        if word.index(i) >= 0:
            workingCopy[word.index(i)] = i
    print(workingCopy)


def isSolved(word, guesses):
    chars = len(word)
    for i in range(0,chars):
        if guesses.index(word[i]) < 0:
            return False
    return True



if __name__ == '__main__':
    gameWord = randomWord()
    print(gameWord)
    
    guesses = []
    
    solved = False
    while(not solved):
        print('Guess a letter:  ')
        letter = input()
        solved = handleGuess(letter, gameWord, guesses)
    