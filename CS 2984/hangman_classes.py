# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 11:28:01 2020

@author: gorpa
"""

import random

class Game:
    def __init__(self):
        self.__listOfGuesses = []
        self.__player = Player()
        self.__word = Word()

    def loadWords(self):
        '''
        This method opens the words_alpha.txt file, reads it
        line-by-line, and adds each word into a list.  It returns
        the list containing all words in the file.
        '''
        with open('words_alpha.txt') as wordFile:
            wordList = []

            for line in wordFile:
                wordList.append(line.rstrip('\n'))

        return wordList

    def randomWord(self, wordList):
        '''
        This method selects a random word from the list passed in
        via the parameter
        '''
        location = random.randint(0, len(wordList))
        return wordList[location]

    def printGameState(self):
        '''
        This method prints the current state of the game at the
        beginning of each round
        '''
        # Example:  currentGuessState = "_e__s_a"
        print("Current state is: ", end="")
        for char in self.__word.getGuessString():
            print(char, end="")
            print(" ", end="")
        print("")
        print("Guesses remaining: ", self.__player.getGuessCount())
        print("Letters already guessed: ", self.__listOfGuesses)

    def isUserFinished(self):
        return "_" not in self.__word.getGuessString()

    def gameLoop(self):
        '''
        This method controls the main game loop, including setup
        '''
        targetWord = self.randomWord(self.loadWords())
        self.__word.setTargetWord(targetWord)
        self.__word.initializeGuessState()
        hasWon = False

        while not hasWon and self.__player.getGuessCount() > 0:
            self.printGameState()

            userInputType = self.__player.determineInputType()

            if userInputType == 1:
                # user guesses a letter
                userGuess = self.__player.userGuessLetter(self.__listOfGuesses)
                (guessCount, self.__listOfGuesses) = self.__word.isCorrectLetter(userGuess, self.__listOfGuesses, self.__player.getGuessCount())
                self.__player.setGuessCount(guessCount)
                hasWon = self.isUserFinished()

            else:
                # user guesses solution
                userGuess = self.player.userGuessSolution()
                if self.__word.isCorrectSolution(userGuess):
                    print("Hooray!  You won!")
                    hasWon = True
                else:
                    print("You guesed wrong and lost")
                    self.__player.setGuessCount(0)

            if self.__player.getGuessCount() == 0:
                print("The correct answer was", targetWord)


class Player:
    def __init__(self):
        self.__guessCount = 10
    
    def getGuessCount(self):
        return self.__guessCount
    
    def setGuessCount(self, updateCount):
        self.__guessCount = updateCount

    def userGuessLetter(self, guesses):
        '''
        This method waits for user input, looping endlessly until
        the user enters a character
        '''
        guess = ""
        while not guess.isalpha() or guess in guesses or len(guess) != 1:
            guess = input("Guess a letter: ")
        guess = guess.lower()
        return guess

    def userGuessSolution(self):
        '''
        This method waits for user input when the user wants to
        solve the puzzle
        '''
        return input("OK, make your guess: ")

    def determineInputType(self):
        '''
        This method lets the user decide whether their next input
        will be a single letter or to solve the puzzle
        '''
        print("What do you want to do?")
        print("1.  Guess a letter")
        print("2.  Solve the puzzle")
        response = ""
        while response not in ["1", "2"]:
            response = input("Your choice: ")
        return int(response)
        

class Word:
    def __init__(self):
        self.__targetWord = ''
        self.__guessString = ''
    
    def getTargetWord(self):
        return self.__targetWord

    def getGuessString(self):
        return self.__guessString

    def setTargetWord(self, newWord):
        self.__targetWord = newWord

    def setGuessString(self, newString):
        self.__guessString = newString

    def isCorrectSolution(self, userGuess):
        '''
        This method checks to see if the user's puzzle solution
        guess is correct
        '''
        return userGuess.lower() == self.__targetWord

    def isCorrectLetter(self, userGuess, guesses, guessCount):
        newGuessState = ""
        currentIndex = 0
        guesses.append(userGuess)

        if userGuess not in self.__targetWord:
            print("Incorrect guess")
            guessCount -= 1
        else:
            # user guess is e
            # targetWord is computer
            # currentGuessState is _o___t__
            # after this branch runs, _o___te_
            for ch in self.__targetWord:
                if ch == userGuess:
                    newGuessState += ch
                else:
                    newGuessState += self.__guessString[currentIndex]
                currentIndex += 1
            self.__guessString = newGuessState

        # things updated:  number of guess, currentState, guesses list
        return (guessCount, guesses)

    def initializeGuessState(self):
        '''
        This method sets up the blank puzzle at the game initialization
        '''
        guessStringBuilder = ""
        for char in self.__targetWord:
            guessStringBuilder += "_"
        self.__guessString = guessStringBuilder



def main():
    game = Game()
    game.gameLoop()

main()