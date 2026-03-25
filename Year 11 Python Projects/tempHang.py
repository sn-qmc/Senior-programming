"""
Title: Hangman Game
Author: Tamara Nguyen
Date: 30 April 2025
"""

import random
import time

science_words = [
    "velocity",
    "momentum",
    "force",
    "gravity",
    "mass",
    "trajectory",
    "projectile"]

math_words = [
    "sum",
    "addition",
    "multiplication",
    "division",
    "algebra",
    "exponent",
    "integer"]

technology_words = [
    "control",
    "loop",
    "iteration",
    "data type",
    "input",
    "output",
    "operator"]

all_words = {
    "science": science_words,
    "math": math_words,
    "technology": technology_words}

all_subjects = list(all_words.keys())

score = 0
INITIAL_TRIES = 7
tries_left = INITIAL_TRIES
incorrect_letters_guessed = []
correct_letters_guessed = [" "]
play_hangman = False

# Checks if the input is in the English alphabet
def is_alpha(word):
            is_letter = word.isalpha()
            if is_letter is False:
                return False
            else:
                return True

# Hangman displays
def no_hangman():
    print("------  ")
    print("|       ")
    print("|       ")
    print("|       ")
    print("|       ")
    print("|       ")

def hangman_rope():
    print("------  ")
    print("|    |  ")
    print("|       ")
    print("|       ")
    print("|       ")
    print("|       ")

def hangman_head():
    print("------  ")
    print("|    |  ")
    print("|    O  ")
    print("|       ")
    print("|       ")
    print("|       ")

def hangman_torso():
    print("------  ")
    print("|    |  ")
    print("|    O  ")
    print("|    |  ")
    print("|       ")
    print("|       ")

def hangman_left_arm():
    print("------  ")
    print("|    |  ")
    print("|    O  ")
    print("|   /|  ")
    print("|       ")
    print("|       ")

def hangman_right_arm():
    print("------  ")
    print("|    |  ")
    print("|    O  ")
    print("|   /|\ ")
    print("|       ")
    print("|       ")

def hangman_left_leg():
    print("------  ")
    print("|    |  ")
    print("|    O  ")
    print("|   /|\ ")
    print("|   /   ")
    print("|       ")

def hangman_right_leg():
    print("------  ")
    print("|    |  ")
    print("|    O  ")
    print("|   /|\ ")
    print("|   / \ ")
    print("|       ")

# The dictionary keys are the number of tries left
hangman_display_from_tries = {
    7: no_hangman,
    6: hangman_rope,
    5: hangman_head,
    4: hangman_torso,
    3: hangman_left_arm,
    2: hangman_right_arm,
    1: hangman_left_leg,
    0: hangman_right_leg
}

user_name = input("Welcome to Hangman. Please enter your name: ")

# Check for invalid names
while True:
    if len(user_name.lower().strip()) < 1:
        user_name = input("Sorry, you didn't enter a name. Please enter"
        " a name: ")
    else:
        break

yes_or_no = input("Do you want to play a game of hangman? (yes/no): ")

# User introduction
while True:
    if yes_or_no.lower().strip() == "yes":
        yes_or_no = input("Do you know how to play hangman? (yes/no): ")
        while True:
            if yes_or_no.lower().strip() == "yes":
                play_hangman = True
                break
            elif yes_or_no.lower().strip() == "no":
                print("Here is how to play hangman: ")
                print("I will give you a few seconds to read it.")
                print("First, you will pick a subject category for your"
                " guessing word to be in.")
                print("Then, you may start guessing letters in this wor"
                "d.")
                print("You will have 7 incorrect attempts to guess the "
                "word.")
                print("Each incorrect try will add a limb onto the hang"
                "man display.")
                print("If you run out of tries and the hangman is fully"
                " hung, you lose the game.")
                print("Otherwise, if you manage to guess the word, you "
                "get one point added to your score.")
                print("You may play again as many times as you want to "
                "get the highest score. Good luck!")
                time.sleep(10)
                play_hangman = True
                break
            else:
                yes_or_no = input("That's not a valid input. Please typ"
                "e 'yes' or 'no': ")
        break
    elif yes_or_no.lower().strip() == "no":
        print("That's too bad! Maybe next time then.")
        play_hangman = False
        break
    else:
        yes_or_no = input("That's not a valid input. Please type 'yes' "
        "or 'no': ")

# Main game
while play_hangman is True:
    print("")
    print("Please pick a subject for your word - ", end="")
    for subject in all_subjects:
        if len(all_subjects) - 1 == all_subjects.index(subject):
            print("or", subject, end="")
        else:
            print(subject, end=", ")
    subject_choice = input(": ")

    # Check that the chosen subject is a valid input and has words left
    while True:
        if subject_choice.lower().strip() in all_subjects:
            if len(all_words[subject_choice.lower().strip()]) != 0:
                break
            else:
                subject_choice = input("Sorry, that subject does not ha"
                "ve any more words. Please choose another subject: ")
        else:
            subject_choice = input("That's not a valid input. Please"
            " enter one of the subjects provided above: ")

    # Pick the guessing word from the subject list and remove it.
    guessing_word = random.choice(all_words[subject_choice.lower().strip()])
    all_words[subject_choice.lower().strip()].remove(guessing_word)

    # Guessing game true loop
    while True:
        print("")
        hangman_display_from_tries[tries_left]()
        print("Tries left:", tries_left)
        print("Letters guessed: ", end="")
        print(* incorrect_letters_guessed, sep=", ")
        for letter in guessing_word:
            if letter in correct_letters_guessed:
                print(letter, end="")
            else:
                print("-", end="")
        print("")
        print("")

        guess = input("Please enter your single letter guess: ")

        # Check for any invalid inputs
        while True:
            if guess.lower().strip() in correct_letters_guessed:
                guess = input("That's already in the word. Guess anothe"
                "r letter: ")
            elif guess.lower().strip() in incorrect_letters_guessed:
                guess = input("That's already been guessed. Guess anoth"
                "er letter: ")
            elif len(guess.strip()) > 1:
                guess = input("Too long. Guess a singular letter"
                ": ")
            elif len(guess.strip()) < 1:
                guess = input("Too short. Guess a letter: ")
            elif is_alpha(guess.strip()) is False:
                guess = input("Sorry, that's not a letter in the Englis"
                "h alphabet. Please guess another letter: ")
            else:
                break

        # Checks if the word has been fully guessed
        def word_guessed():
            correctly_guessed = 0
            for letter in guessing_word:
                if letter in correct_letters_guessed:
                    correctly_guessed += 1
            if len(guessing_word) == correctly_guessed:
                return True
            else:
                return False

        # Checks if the letter is in the word
        if guess.lower().strip() in guessing_word:
            correct_letters_guessed.append(guess.lower().strip())

            # Checks if the word is guessed
            if word_guessed() is True:
                score += 1
                hangman_display_from_tries[tries_left]()
                print("Tries left:", tries_left)
                print("Letters guessed: ", end="")
                print(* incorrect_letters_guessed, sep=", ")
                for letter in guessing_word:
                    print(letter, end="")
                print("")
                print("You guessed the word!")

                # Checks if there any guessing words remaining
                finished_subjects = 0
                for subject in all_words:
                    if len(all_words[subject]) == 0:
                        finished_subjects += 1

                if finished_subjects == len(all_subjects):
                    print("Congratulations! You've finished the game, "
                    , user_name, "! There are no more words to be gues"
                    "sed!", sep="")
                    print("Your final score was:", score)
                    play_hangman = False
                    break

                # Asks user if they would like to continue playing
                yes_or_no = input("Would you like to continue playing ("
                "yes/no): ")
                while True:
                    if yes_or_no.lower().strip() == "yes":
                        correct_letters_guessed = [" "]
                        incorrect_letters_guessed = []
                        tries_left = INITIAL_TRIES
                        print("OK!")
                        break
                    elif yes_or_no.lower().strip() == "no":
                        print("OK, thanks for playing", user_name)
                        print("Your final score was", score)
                        break
                    else:
                        yes_or_no = input("Not a valid input. Please en"
                        "ter yes or no: ")
                if yes_or_no.lower().strip() == "yes":
                    # Breaks the guessing game true loop
                    break
                if yes_or_no.lower().strip() == "no":
                    play_hangman = False
                    # Stops main game and guessing game true loop
                    break

        else:
            incorrect_letters_guessed.append(guess.lower())
            tries_left -= 1
            if tries_left == 0:
                print("")
                hangman_display_from_tries[tries_left]()
                yes_or_no = input("Oops! You ran out of tries. Would yo"
                "u like to play again (yes/no): ")
                while True:
                    if yes_or_no.lower().strip() == "yes":
                        correct_letters_guessed = [" "]
                        incorrect_letters_guessed = []
                        tries_left = INITIAL_TRIES
                        science_words = [
                            "velocity",
                            "momentum",
                            "force",
                            "gravity",
                            "mass",
                            "trajectory",
                            "projectile"]
                        math_words = [
                            "sum",
                            "addition",
                            "multiplication",
                            "division",
                            "algebra",
                            "exponent",
                            "integer"]
                        technology_words = [
                            "control",
                            "loop",
                            "iteration",
                            "data type",
                            "input",
                            "output",
                            "operator"]
                        all_words = {
                            "science": science_words,
                            "math": math_words,
                            "technology": technology_words}
                        all_subjects = list(all_words.keys())
                        score = 0
                        print("OK!")
                        break
                    elif yes_or_no.lower().strip() == "no":
                        print("OK, thanks for playing", user_name)
                        print("Your final score was", score)
                        break
                    else:
                        yes_or_no = input("Not a valid input. Please en"
                        "ter yes or no: ")
                if yes_or_no.lower().strip() == "yes":
                    # Breaks the guessing game true loop
                    break
                if yes_or_no.lower().strip() == "no":
                    play_hangman = False
                    # Stops main game and guessing game true loop
                    break
                break
