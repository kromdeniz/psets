# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    progress = ''
    for char in secret_word:
            if char not in letters_guessed:
                progress += '_ '
            else:
                progress += char
    return progress



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    abc = string.ascii_lowercase 
    letters_rest = ''
    if letters_guessed == []:
        return abc
    for char in abc:
        if char not in letters_guessed:
            letters_rest += char
    return letters_rest 



def warning_msg(user_guess,letters_guessed,warning):
    if warning == 0:
         if user_guess.isalpha() != True:
            return f'Oops! that is not a valid letter and you dont have any warning left so you lose a guess! '
         elif user_guess in letters_guessed:
            return f'Oops you already guessed that letter and you dont have any warning left so you lose a guess!'    
    elif warning != 0:
        if user_guess.isalpha() != True:
            return f'Oops! that is not a valid letter you have {warning-1} warning(s) left! '
        elif user_guess in letters_guessed:
            return f'Oops you already guessed that letter you have {warning-1} warning(s) left!'
   
def game_intro(warning):
    return f'''Welcome to a mighty game of hangman by Krom abi!
I am thinking of a word with {len(secret_word)} letters.
You have {warning} warnings left.'''

def game_msg(guess, letters_guessed):
    return(f'''-------------
You have {guess} guess(es) left
Available letters: {get_available_letters(letters_guessed)}''')
        
def win_msg(guess):    
    secret_set = set(secret_word)
    total_score = len(secret_set) * guess
    return f'''Congrats! you won!
your score is: {total_score}'''

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    
    guess = 6
    warning = 3
    letters_guessed =[]
    user_guess = ''
    vowels =['a','e','i','o']
    print(game_intro(warning))
    while guess != 0 or is_word_guessed(secret_word,letters_guessed) != True:
        
        print(game_msg(guess, letters_guessed))
        user_guess = str.lower(input('Please guess a letter:'))   
        
        if user_guess.isalpha()!= True or user_guess in letters_guessed:            
            if warning == 0: guess += -1 ; print(warning_msg(user_guess, letters_guessed, warning))
            elif warning != 0:print(warning_msg(user_guess, letters_guessed, warning)); warning += -1
                           
        elif user_guess in secret_word:
            letters_guessed.append(user_guess)
            print('Good guess!', get_guessed_word(secret_word,letters_guessed))
        
        elif user_guess not in secret_word and user_guess in vowels:      
            print('Oops! that letter is not in my word', get_guessed_word(secret_word, letters_guessed))
            guess += -2
        elif user_guess not in secret_word: print('Oops! that letter is not in my word', get_guessed_word(secret_word, letters_guessed)); guess += -1
        letters_guessed.append(user_guess)
        if guess == 0 or is_word_guessed(secret_word,letters_guessed):break
    if is_word_guessed(secret_word, letters_guessed):print(win_msg(guess))        
    elif guess == 0 :print('Sorry, you ran out of guesses. The word was else.')    
        
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
