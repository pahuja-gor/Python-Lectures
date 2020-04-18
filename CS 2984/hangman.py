# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 16:15:59 2020

A hangman word game

@author: John
"""

# data
# list of guesses
# target word
# current guess state of target string
# guess count


# functions
# pick a word -- DONE
# load a list of words -- DONE
# user input (letter) -- DONE
# user input (solve) -- DONE
# determine user input type -- DONE
# game loop
# respond to guess (letter) -- DONE
# respond to guess (solve) -- DONE
# print game state -- DONE
# initialize user guess string -- DONE

import random


def loadWords():
    '''
    This function opens the words_alpha.txt file, reads it
    line-by-line, and adds each word into a list.  It returns
    the list containing all words in the file.
    '''
    with open('words_alpha.txt') as wordFile:
        wordList = []

        for line in wordFile:
            wordList.append(line.rstrip('\n'))

    return wordList


def randomWord(wordList):
    '''
    This function selects a random word from the list passed in
    via the parameter
    '''
    location = random.randint(0, len(wordList))
    return wordList[location]


def userGuessLetter(guesses):
    '''
    This function waits for user input, looping endlessly until
    the user enters a character
    '''
    guess = ""
    while not guess.isalpha() or guess in guesses or len(guess) != 1:
        guess = input("Guess a letter: ")
    guess = guess.lower()
    return guess


def userGuessSolution():
    '''
    This function waits for user input when the user wants to
    solve the puzzle
    '''
    return input("OK, make your guess: ")


def determineInputType():
    '''
    This function lets the user decide whether their next input
    will be a single letter or to solve the puzzle
    '''
    print("What do you want to do?")
    print("1.  Guess a letter")
    print("2.  Solve the puzzle")
    response = ""
    while response not in ["1", "2"]:
        response = input("Your choice: ")
    return int(response)


def isCorrectSolution(userGuess, targetWord):
    '''
    This function checks to see if the user's puzzle solution
    guess is correct
    '''
    return userGuess.lower() == targetWord


def isCorrectLetter(userGuess, targetWord, guesses, guessCount, currentGuessState):
    newGuessState = ""
    currentIndex = 0
    guesses.append(userGuess)

    if userGuess not in targetWord:
        print("Incorrect guess")
        guessCount -= 1
    else:
        # user guess is e
        # targetWord is computer
        # currentGuessState is _o___t__
        # after this branch runs, _o___te_
        for ch in targetWord:
            if ch == userGuess:
                newGuessState += ch
            else:
                newGuessState += currentGuessState[currentIndex]
            currentIndex += 1
        currentGuessState = newGuessState

    # things updated:  number of guess, currentState, guesses list
    return (guessCount, currentGuessState, guesses)


def printGameState(currentGuessState, guessCount, guesses):
    '''
    This function prints the current state of the game at the
    beginning of each round
    '''
    # Example:  currentGuessState = "_e__s_a"
    print("Current state is: ", end="")
    for char in currentGuessState:
        print(char, end="")
        print(" ", end="")
    print("")
    print("Guesses remaining: ", guessCount)
    print("Letters already guessed: ", guesses)


def initializeGuessState(targetWord):
    '''
    This function sets up the blank puzzle at the game initialization
    '''
    guessString = ""
    for char in targetWord:
        guessString += "_"
    return guessString


def isUserFinished(currentGuessState):
    return "_" not in currentGuessState


def gameLoop():
    '''
    This function controls the main game loop, including setup
    '''
    guesses = []
    targetWord = randomWord(loadWords())
    currentGuessState = initializeGuessState(targetWord)
    guessCount = 10
    hasWon = False

    while not hasWon and guessCount > 0:
        printGameState(currentGuessState, guessCount, guesses)

        userInputType = determineInputType()

        if userInputType == 1:
            # user guesses a letter
            userGuess = userGuessLetter(guesses)
            (guessCount, currentGuessState, guesses) = isCorrectLetter(userGuess, targetWord, guesses, guessCount,
                                                                       currentGuessState)
            hasWon = isUserFinished(currentGuessState)

        else:
            # user guesses solution
            userGuess = userGuessSolution()
            if isCorrectSolution(userGuess, targetWord):
                print("Hooray!  You won!")
                hasWon = True
            else:
                print("You guesed wrong and lost")
                print("The correct answer was", targetWord)
                guessCount = 0

        if guessCount == 0:
            print("The correct answer was", targetWord)


gameLoop()