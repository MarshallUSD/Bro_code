import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open("words.txt", 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
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
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    result = ''
    for letter in secret_word:
        if letter in letters_guessed:
            result += letter
        else:
            result += '_ '
    return result


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available = string.ascii_lowercase
    return ''.join([letter for letter in available if letter not in letters_guessed])


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
    guesses_left = 6
    letters_guessed = []
    warnings = 3
    
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings} warnings left.")
    
    while guesses_left > 0:
        print("-" * 13)
        print(f"You have {guesses_left} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        guess = input("Please guess a letter: ").lower()
        
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            warnings -= 1
            if warnings >= 0:
                print(f"Oops! That is not a valid letter. You have {warnings} warnings left.")
            else:
                print("Oops! That is not a valid letter. You've run out of warnings, you lose one guess.")
                guesses_left -= 1
            continue
            
        if guess in letters_guessed:
            warnings -= 1
            if warnings >= 0:
                print(f"Oops! You've already guessed that letter. You have {warnings} warnings left.")
            else:
                print("Oops! You've already guessed that letter. You've run out of warnings, you lose one guess.")
                guesses_left -= 1
            continue
            
        letters_guessed.append(guess)
        
        if guess in secret_word:
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
            guesses_left -= 1
            
        if is_word_guessed(secret_word, letters_guessed):
            print("-" * 13)
            print("Congratulations, you won!")
            print(f"Your total score for this game is: {guesses_left * len(set(secret_word))}")
            return
            
    print("-" * 13)
    print(f"Sorry, you died. The word was {secret_word}.")


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False
        
    guessed_letters = set(my_word) - {'_'}
    
    for i in range(len(my_word)):
        if my_word[i] != '_' and my_word[i] != other_word[i]:
            return False
        if my_word[i] == '_' and other_word[i] in guessed_letters:
            return False
            
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    matches = [word for word in wordlist if match_with_gaps(my_word, word)]
    if matches:
        print("Possible word matches are:")
        print(" ".join(matches))
    else:
        print("No matches found")


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
    guesses_left = 6
    letters_guessed = []
    warnings = 3
    
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print(f"You have {warnings} warnings left.")
    print("You can enter '*' for a hint, which will show possible matching words.")
    
    while guesses_left > 0:
        print("-" * 13)
        print(f"You have {guesses_left} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        guess = input("Please guess a letter: ").lower()
        
        if guess == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue
            
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            warnings -= 1
            if warnings >= 0:
                print(f"Oops! That is not a valid letter. You have {warnings} warnings left.")
            else:
                print("Oops! That is not a valid letter. You've run out of warnings, you lose one guess.")
                guesses_left -= 1
            continue
            
        if guess in letters_guessed:
            warnings -= 1
            if warnings >= 0:
                print(f"Oops! You've already guessed that letter. You have {warnings} warnings left.")
            else:
                print("Oops! You've already guessed that letter. You've run out of warnings, you lose one guess.")
                guesses_left -= 1
            continue
            
        letters_guessed.append(guess)
        
        if guess in secret_word:
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
            guesses_left -= 1
            
        if is_word_guessed(secret_word, letters_guessed):
            print("-" * 13)
            print("Congratulations, you won!")
            print(f"Your total score for this game is: {guesses_left * len(set(secret_word))}")
            return
            
    print("-" * 13)
    print(f"Sorry, you died. The word was {secret_word}.")


if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman(secret_word)
    
    # To test part 3, uncomment the following two lines
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)