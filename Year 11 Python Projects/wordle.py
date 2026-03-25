import json
import random

with open(r"Year 11 Python Projects\wordle_list.json", "r") as f:
    word_list = json.load(f)

word_to_guess = ""
word_set = set(word_list)

def load_words():
    global word_to_guess
    word_to_guess = random.choice(word_list)


# Colour codes for optional ANSI output
GREEN = "32"
RED = "31"
YELLOW = "33"
BOLD = "1"

MAX_GUESSES = 6
WORD_LENGTH = 5

# ------------------------------------
# Small helper for optional text colour
# ------------------------------------

def colour(text, code):
    # Wrap the text in ANSI escape codes for colour
    return f"\033[{code}m{text}\033[0m"

def check_letters(to_split):
    guess_letters = to_split
    letter_correct = [] #0 is incorrect, 1 is partial, 2 is correct
    for x in range(WORD_LENGTH):
        if(guess_letters[x] in word_to_guess):
            if(guess_letters[x] == word_to_guess[x]):
                letter_correct.append(2)
            else:
                letter_correct.append(1)
        else:
            letter_correct.append(0)
    return letter_correct

def setup_guesses(guess, guesses):
    letters_color = check_letters(guess)
    output_text = ""
    for x in range(WORD_LENGTH):
        c = 0
        if(letters_color[x] == 0):
            c = RED
        elif(letters_color[x] == 1):
            c = YELLOW
        else:
            c = GREEN
        output_text += colour(guess[x], c)
        
    guesses.append(output_text)
    
    for g in guesses:
        print(g)            

def play_again():
    while True:
        another = input("Would you like to play again (Y, Yes, N, No):").strip().lower()
        if(another == "y" or another == "yes"):
            main()
        elif(another == "n" or another == "no"):
            print("Bye!")
            break
        else:
            print("Please enter a valid input! \n\n")

def main():
    load_words()
    current_num_guess = 0
    guesses = []
    print("Hello, welcome to rip off wordle \n")
    for i in range(MAX_GUESSES):
        current_num_guess += 1
        guess = input(f"Guess {current_num_guess}: Please enter your guess~ ").strip().lower()
        
        while True:
            if(len(guess) == WORD_LENGTH):
                if(guess.isalpha()):
                    if(guess in word_set):
                        break
                    else:
                        print("Please enter a valid word!")
                else:
                    print("Please enter ony letters!")
            print("please enter only 5 letters!")
            guess = input("Please enter your guess: ").strip().lower()
        
        setup_guesses(guess, guesses)
        if(guess == word_to_guess):
            print("You solved the wordle!")
            break
    play_again()
                
main()