import random

# ----------------- INITIALISATION -------------------
# Create flag to show whether the game is over or not
# and how many attempts are allowed before it's game over.
game_over = False
ATTEMPT_LIMIT = 10

# Create array of words and pick a word from the array
# then put the chosen word into an array/list of chars
WORD_ARRAY = ["Test", "Coding", "Scratchpad", "Tired", "Hungry"]
chosen_word = random.choice(WORD_ARRAY).upper() # Make the word UPPER CASE for consistency
char_chosen_word = list(chosen_word)

# Create a constant string that can be added to replace any missing letters
MISSING_LETTER = "_ "

# Initialise a char array that will hold the letters of each correct guess
guess = []
for char in char_chosen_word:
    guess.append(MISSING_LETTER)

# Initialise a char array of the letters already guessed
guessed_letters = []

print("Chosen word: " + chosen_word) # Testing purposes (delete after game is finished)
#-----------------------------------------------------
#-------------------- FUNCTIONS ----------------------
def ShowWordProgress():
    print("\nHere is the word so far:")
    print(guess)
    
def ShowGuessedLetters():
    # Print the user's guessed letters for their convenience
    print("\nHere are the letters you've already picked:")
    print(guessed_letters)

def GetUserInput():  
    # Get the user's input, then append it to the guessed letters array IF the letter is not already in the array
    input_guess = input("\nWhat letter?\n> ").upper() # Make the word UPPER CASE for consistency
    if (input_guess in guessed_letters):
        print("You've already picked this letter!")
        GetUserInput()
    else:
        guessed_letters.append(input_guess)
        
    return input_guess

def CheckInput(letter_guess):
    # Get the letter guess and check it against the char array of the chosen word
    if (letter_guess in char_chosen_word):
        print("Correct!")
        for i in range(len(char_chosen_word)):
            if (letter_guess in char_chosen_word[i]):
                guess[i] = letter_guess
    else:
        print("Nope!")

#-----------------------------------------------------
#-------------------- MAIN CODE ----------------------
print("~~~~~~~~~~ Welcome to Hangman! ~~~~~~~~~")
print("I've chosen a word. Guess it by picking letters and seeing where it goes!")
while (game_over == False):
    ShowWordProgress()
    ShowGuessedLetters()
    CheckInput(GetUserInput())
    
print("~~~~~~ GAME OVER ~~~~~~")