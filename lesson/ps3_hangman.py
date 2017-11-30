# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "C:/Users/Ramenga/Documents/Py/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in secretWord:
        if i not in lettersGuessed:
            return False
        
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessed=''
    for i in secretWord:
        if i in lettersGuessed:
            guessed = guessed+i+' '
        else:
            guessed = guessed+'_ '
            
    return guessed



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alphb = string.ascii_lowercase #import alphabet list
    notGuessed=''
    for i in alphb:
        if i not in lettersGuessed:
            notGuessed+=i
        
    return notGuessed

  
secretWord=chooseWord(wordlist)
 

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    
    Wlength=len(secretWord)
    guesses=8
    guess_ip=''
    lettersGuessed=[]
    lettersGuessed2=[]
    print "Welcome to the game, Hangman!"
    print ("I am thinking of a word that is "+str(Wlength)+" letters long.")
    print ("-------------")
    
    while guesses>0 and (not isWordGuessed(secretWord,lettersGuessed)):
        availableLetters = getAvailableLetters(lettersGuessed)
        print ("You have "+str(guesses)+" guesses left.")
        print ("Available letters: "+availableLetters)
        guess = raw_input("Please guess a letter: ")
        lettersGuessed2=lettersGuessed[:]
        guess_ip = guess.lower()
        lettersGuessed+=[guess_ip]
        if (guess_ip in secretWord) and (guess_ip in availableLetters):            
            print ("Good guess: "+getGuessedWord(secretWord,lettersGuessed))
            print ("-------------")
        elif (guess_ip in secretWord) and (guess_ip not in availableLetters):
            print ("Oops! You've already guessed that letter: "+getGuessedWord(secretWord,lettersGuessed))
            print ("-------------")
        elif (guess_ip in lettersGuessed2):
            print ("Oops! You've already guessed that letter: "+getGuessedWord(secretWord,lettersGuessed))
            print ("-------------")
        else:
            print ("Oops! That letter is not in my word: "+getGuessedWord(secretWord,lettersGuessed))
            guesses-=1
            print ("-------------")
            
    if guesses<=0:
        print("Sorry, you ran out of guesses. The word was "+secretWord)
    else:
        print("Congratulations, you won!")
        





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)