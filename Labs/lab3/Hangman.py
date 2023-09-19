'''
Hangman.py

Nicolas Van der Werf. Worked alone on this lab.

'''

import sys
import random

class Hangman:
    '''
    Initializes the words list
    '''
    def __init__(self):
        file = open('words.txt','r')
        self.words = []
        self.wordguess = []
        for line in file:
            self.words.append(line.rstrip())

    '''
    Outputs the current status of the guesses
    '''
    def printword(self):
        for c in self.wordguess:
            print(c,end="")
        print()

    '''
    Chat GPT created the art in characters for this method. It was not used anywhere else.
    '''
    def print_hangman(self, turns):
        stages = [
            """
             ------
             |    |
             |    
             |   
             |    
             |   
             |
            ---
            """,
            """
             ------
             |    |
             |    O
             |   
             |    
             |   
             |
            ---
            """,
            """
             ------
             |    |
             |    O
             |    |
             |    
             |   
             |
            ---
            """,
            """
             ------
             |    |
             |    O
             |   \|
             |    
             |   
             |
            ---
            """,
            """
             ------
             |    |
             |    O
             |   \|/
             |    
             |   
             |
            ---
            """,
            """
             ------
             |    |
             |    O
             |   \|/
             |    |
             |   
             |
            ---
            """,
            """
             ------
             |    |
             |    O
             |   \|/
             |    |
             |   / 
             |
            ---
            """,
            """
             ------
             |    |
             |    O
             |   \|/
             |    |
             |   / \\
             |
            ---
            """,
            """
             ------
             |    |
             |   .O
             |   \|/
             |    |
             |   / \\
             |
            ---
            """,
            """
             ------
             |    |
             |   .O.
             |   \|/
             |    |
             |   / \\
             |
            ---
            """,
            """
             ------
             |    |
             |   .O.
             |   \|/
             |    |
             |   / \\
             |
            ---  DEAD
            """
        ]

        print(stages[turns])

    def playgame(self):
        # generate random word
        word = self.words[random.randint(0,len(self.words)-1)]
        #print(word)
        listguesses = []
        guesses = 0
        correct = True
        while guesses < 10:
            validguess = False
            ch = ''
            while not validguess:
                ch = input('Enter a guess: ').lower()
                if not ch.isalpha():    print("Guess must be a single letter\n")
                elif len(ch) != 1:      print("Guess must only be one letter\n")
                elif ch in listguesses: print('The letter ' + ch + ' has already been guessed\n')
                else: validguess = True

            guesses = guesses + 1
            listguesses.append(ch)

            correct = True
            lista = list(map(lambda x: x if x in listguesses else'_', word))
            if '_' in lista: correct = False
            if correct:
                print(*lista, sep='', end='\n')
                print("Correct!!")
                break
            if ch not in word:
                print('\n'+ ch + ' does not occur.')
            print('Guesses Remaining: ' + str(10 - guesses))
            print(*lista, sep='')
            self.print_hangman(guesses)
        if not correct:
            print('Sorry dude, the word is:  ' + word)


            ### Your code goes here:###

if __name__ == "__main__":

    game = Hangman()

    game.playgame()
