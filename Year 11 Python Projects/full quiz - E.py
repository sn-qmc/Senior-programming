# ============================================================
# Quiz Program — Excellence Level
# ============================================================

import json       # For saving and loading high scores as a JSON file
import os         # For checking if the high score file exists
import random     # For shuffling questions and (optionally) choice order
import time       # For measuring time taken per question and per round
from datetime import datetime  # For timestamping high score entries

# ----------------------------
# Settings and global constants
# ----------------------------

USE_COLOUR = True           # Set to True to enable ANSI colour output
NUM_QUESTIONS = 5            # Number of questions asked per round
HIGHSCORE_FILE = "highscores.json"  # File path for storing high scores
AGE_MIN = 9                  # Minimum age for playing
AGE_MAX = 13                 # Maximum age for playing

# Colour codes for optional ANSI output
GREEN = "32"
RED = "31"
CYAN = "36"
YELLOW = "33"
BOLD = "1"

# ------------------------------------
# Small helper for optional text colour
# ------------------------------------

def colour(text, code):
    # If colour is turned off, just return the plain text
    if not USE_COLOUR:
        return text
    # Wrap the text in ANSI escape codes for colour
    return f"\033[{code}m{text}\033[0m"

# ---------------------------
# Input functions and checks
# ---------------------------

def getName():
    # Ask repeatedly until a non-empty name is provided
    while True:
        name = input("What is your name? ").strip()
        if name != "":
            return name
        print("Please enter a name.")

def getAge():
    # Ask repeatedly until a whole number within a sensible range is given
    while True:
        raw = input("How old are you? ").strip()
        # Age must be digits only
        if not raw.isdigit():
            print("Please enter your age as a whole number, for example 12.")
            continue
        age = int(raw)
        # Filter out unrealistic values
        if age < 0 or age > 120:
            print("Please enter a realistic age between 0 and 120.")
            continue
        return age

def canPlay(age):
    # Enforce the 9 to 13 age gate
    return AGE_MIN <= age <= AGE_MAX

# -------------------------------------
# Question bank and category management
# -------------------------------------

def loadQBank():
    # Return a dictionary of categories.
    # Each category maps to a list of question dictionaries.
    # Each question dictionary has:
    #   - 'q': the question text
    #   - 'choices': a list of 4 options (strings)
    #   - 'correct_index': an integer 0..3 pointing to the correct choice
    return {
        "General Knowledge": [
            {"q": "What is the capital of France?",
             "choices": ["Paris", "Rome", "Berlin", "Madrid"], "correct_index": 0},
            {"q": "How many days are in a week?",
             "choices": ["5", "6", "7", "8"], "correct_index": 2},
            {"q": "Which ocean is the largest?",
             "choices": ["Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean"], "correct_index": 1},
            {"q": "Plants mainly take in which gas?",
             "choices": ["Oxygen", "Nitrogen", "Carbon dioxide", "Helium"], "correct_index": 2},
            {"q": "What do bees collect from flowers?",
             "choices": ["Sand", "Pollen", "Clay", "Iron"], "correct_index": 1},
            {"q": "What is H2O commonly called?",
             "choices": ["Salt", "Water", "Sugar", "Air"], "correct_index": 1},
        ],
        "Maths": [
            {"q": "What is 7 × 8?",
             "choices": ["54", "56", "58", "60"], "correct_index": 1},
            {"q": "What is 100 ÷ 4?",
             "choices": ["20", "25", "30", "40"], "correct_index": 1},
            {"q": "What is the square root of 81?",
             "choices": ["7", "8", "9", "10"], "correct_index": 2},
            {"q": "What is 12 + 15?",
             "choices": ["25", "26", "27", "28"], "correct_index": 2},
            {"q": "What is 2 to the power of 5?",
             "choices": ["16", "32", "64", "128"], "correct_index": 1},
        ],
        "Digital Tech": [
            {"q": "In Python, what keyword defines a function?",
             "choices": ["func", "def", "function", "define"], "correct_index": 1},
            {"q": "What does CPU stand for?",
             "choices": ["Central Processing Unit", "Computer Personal Unit", "Core Program Utility", "Central Power Unit"], "correct_index": 0},
            {"q": "Binary is base what number?",
             "choices": ["2", "8", "10", "16"], "correct_index": 0},
            {"q": "What symbol starts a comment in Python?",
             "choices": ["//", "#", "/*", "<!--"], "correct_index": 1},
            {"q": "What does RAM stand for?",
             "choices": ["Read Access Memory", "Random Access Memory", "Rapid Access Module", "Ready Access Memory"], "correct_index": 1},
        ],
    }

def listCategories(bank):
    # Print available categories with numbers for selection
    print("")
    print(colour("Choose a category:", BOLD))
    categories = list(bank.keys())
    i = 0
    while i < len(categories):
        print(str(i + 1) + ". " + categories[i])
        i = i + 1
    # Return the list so the caller can map numbers to names
    return categories

def pickCategory(bank):
    # Show categories and ask the user to enter a valid number
    categories = listCategories(bank)
    while True:
        choice = input("Enter a number: ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(categories):
                return categories[idx]
        print("Please enter a valid number from the list.")

def selectQuestions(bank, category, num_questions):
    # Create a copy of the category question list and shuffle it
    # This keeps the original bank unmodified
    pool = bank[category][:]         # Shallow copy of the list
    random.shuffle(pool)             # Random order each round
    # Return the first N questions
    return pool[:num_questions]

# --------------------------------
# Multiple choice question routine
# --------------------------------

def letterFor(index):
    # Convert a 0..3 index to a letter A..D
    return chr(ord('A') + index)

def indexForLetter(letter):
    # Convert a letter like 'A', 'B', 'C', 'D' to 0..3
    # Return None if invalid
    table = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
    key = letter.strip().lower()
    return table.get(key, None)

def askMcQuestion(name, q_dict, number, shuffle_choices=True):
    # Ask a single multiple choice question and return:
    #   (is_correct, time_taken_seconds)
    print("")
    print("Question " + str(number) + " for " + name + ": " + q_dict["q"])

    # Copy choices so we can shuffle them without changing the bank
    choices = q_dict["choices"][:]
    correct_index = q_dict["correct_index"]

    # Build a list of tuples (choice_text, is_correct)
    labelled = []
    i = 0
    while i < len(choices):
        labelled.append((choices[i], i == correct_index))
        i = i + 1

    # Randomise choice order if requested
    if shuffle_choices:
        random.shuffle(labelled)

    # Display choices as A, B, C, D
    j = 0
    while j < len(labelled):
        print("  " + letterFor(j) + ") " + labelled[j][0])
        j = j + 1

    # Start timing after showing the choices
    start = time.time()

    # Ask for A, B, C, or D (also accept 1, 2, 3, 4)
    while True:
        raw = input("Your choice (A, B, C, or D): ").strip()
        # Accept 1..4 as an alternative to letters
        if raw.isdigit():
            num = int(raw)
            if 1 <= num <= 4:
                chosen_index = num - 1
                break
        # Accept letters A..D in any case
        maybe = indexForLetter(raw)
        if maybe is not None:
            chosen_index = maybe
            break
        print("Please enter A, B, C, D, or 1, 2, 3, 4.")

    end = time.time()
    time_taken = end - start

    # Determine whether the selected option is correct
    is_correct = labelled[chosen_index][1]

    # Provide feedback
    if is_correct:
        print(colour("Correct.", GREEN))
    else:
        # Find which choice in the displayed list is the correct one
        k = 0
        correct_text = ""
        while k < len(labelled):
            if labelled[k][1]:
                correct_text = labelled[k][0]
                break
            k = k + 1
        print(colour("Incorrect. The correct answer was: " + correct_text, RED))

    return is_correct, time_taken

# -------------------
# High score handling
# -------------------

def loadHighscores():
    # Load high scores from JSON file if it exists
    if not os.path.exists(HIGHSCORE_FILE):
        return {}
    try:
        with open(HIGHSCORE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            return data
        # If the file content is not a dict, start fresh
        return {}
    except Exception:
        # If the file is corrupt or unreadable, start fresh
        return {}

def saveHighscores(data):
    # Save the highscores dictionary to the JSON file
    try:
        with open(HIGHSCORE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception:
        # If saving fails, continue without crashing
        pass

def recordScore(highscores, category, name, score, total, total_time_s):
    # Create a score entry with summary data
    percent = round((score / float(total)) * 100)
    entry = {
        "name": name,
        "score": score,
        "total": total,
        "percent": percent,
        "time_s": round(total_time_s, 2),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    # Ensure the category key exists
    if category not in highscores:
        highscores[category] = []
    # Add the new score
    highscores[category].append(entry)
    # Sort by highest score and then by fastest time
    highscores[category].sort(key=lambda e: (-e["score"], e["time_s"]))
    # Keep only the top 5 entries
    highscores[category] = highscores[category][:5]
    # Save changes to disk
    saveHighscores(highscores)

def printLeaderboard(highscores, category):
    # Print a simple leaderboard for the chosen category
    if category not in highscores or len(highscores[category]) == 0:
        print("No high scores for " + category + " yet.")
        return

    print("")
    print(colour("Top scores for " + category + ":", BOLD))
    i = 0
    while i < len(highscores[category]):
        e = highscores[category][i]
        line = (
            str(i + 1) + ". " + e["name"] +
            " - " + str(e["score"]) + "/" + str(e["total"]) +
            " (" + str(e["percent"]) + "%) in " + str(e["time_s"]) + "s" +
            " on " + e["date"]
        )
        print(line)
        i = i + 1

# ----------------------
# Round and game control
# ----------------------

def playRound(name, bank, category):
    # Select a set of questions for this round and play through them
    questions = selectQuestions(bank, category, NUM_QUESTIONS)

    # Round counters for score and time
    score = 0
    round_start = time.time()

    # Loop through each selected question and ask it
    i = 0
    while i < len(questions):
        correct, elapsed = askMcQuestion(name, questions[i], i + 1, shuffle_choices=True)
        if correct:
            score = score + 1
        # elapsed is available if you want to report per-question time
        i = i + 1

    # Compute total time and percentage
    round_end = time.time()
    total_time = round_end - round_start
    percent = round((score / float(len(questions))) * 100)

    # Round summary output
    print("")
    print(colour("Round complete, " + name + ".", CYAN))
    print("You scored " + str(score) + " out of " + str(len(questions)) + " (" + str(percent) + "%).")
    print("Total time: " + str(round(total_time, 2)) + " seconds.")

    # Return values that the caller needs for high score recording
    return score, len(questions), total_time

def askPlayAgain():
    # Ask the player if they want to play another round
    while True:
        choice = input("Play again? (y/n): ").strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("Please enter y or n.")

def main():
    # Welcome message
    print(colour("Welcome to the Quiz.", BOLD))

    # Get and validate player details
    name = getName()
    age = getAge()

    # Enforce the age gate
    if not canPlay(age):
        print("Sorry " + name + ", this quiz is for ages " + str(AGE_MIN) + " to " + str(AGE_MAX) + ".")
        return

    print("Great, " + name + ". You can play the quiz.")

    # Prepare the question bank and high score storage
    bank = loadQBank()
    highscores = loadHighscores()

    # Main game loop (runs rounds until the player chooses to stop)
    while True:
        # Category selection
        category = pickCategory(bank)
        print("")
        print("You chose: " + category)

        # Show leaderboard for this category before the round starts
        printLeaderboard(highscores, category)

        # Run one round and collect results
        print("")
        print("Starting a new round of " + str(NUM_QUESTIONS) + " questions.")
        score, total, total_time = playRound(name, bank, category)

        # Record the score and update the leaderboard
        recordScore(highscores, category, name, score, total, total_time)

        # Ask whether to play again
        if not askPlayAgain():
            print("Thanks for playing, " + name + ". Goodbye.")
            break

main()