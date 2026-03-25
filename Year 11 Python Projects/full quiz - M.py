# Quiz Program: Merit Level
def get_name():
    # Ask for the player's name until a non-empty value is given.
    while True:
        name = input("What is your name? ").strip()
        if name != "":
            return name
        print("Please enter a name.")

def get_age():
    # Ask for the player's age until a numeric, realistic value is given.
    while True:
        raw = input("How old are you? ").strip()
        if not raw.isdigit():
            print("Please enter your age as a whole number, for example 12.")
            continue

        age = int(raw)

        # Simple sanity range
        if age < 0 or age > 120:
            print("Please enter a realistic age between 0 and 120.")
            continue

        return age

def can_play(age):
    # Only ages 9 to 13 inclusive can play.
    return age >= 9 and age <= 13

def load_questions():
    # Return a list of question dictionaries.
    # Each item has 'q' for question text and 'a' for the correct answer.
    # Answers are stored in lowercase to make comparison easy.
    return [
        {"q": "What is the capital of France?", "a": "paris"},
        {"q": "5 + 7 = ?", "a": "12"},
        {"q": "What planet do humans live on?", "a": "earth"},
        {"q": "What is the opposite of hot?", "a": "cold"},
        {"q": "How many days are in a week?", "a": "7"}
    ]

def ask_round(name, question_bank):
    # Ask each question in order and keep a score for this round.
    score = 0
    total = len(question_bank)

    i = 0
    while i < total:
        print("")
        print("Question " + str(i + 1) + " for " + name + ": " + question_bank[i]["q"])
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = question_bank[i]["a"]

        if user_answer == correct_answer:
            print("Correct.")
            score = score + 1
        else:
            print("Incorrect. The correct answer was: " + correct_answer)

        i = i + 1

    # Round summary
    print("")
    print("Round complete, " + name + ". You scored " + str(score) + " out of " + str(total) + ".")

def play_again():
    # Ask if the player wants another round.
    while True:
        choice = input("Play again? (y/n): ").strip().lower()
        if choice == "y" or choice == "yes":
            return True
        if choice == "n" or choice == "no":
            return False
        print("Please enter y or n.")

def main():
    # Overall flow: greet, collect valid name and age, age gate, run rounds, replay.
    print("Welcome to the Quiz.")
    name = get_name()
    age = get_age()

    if not can_play(age):
        print("Sorry " + name + ", this quiz is for ages 9 to 13.")
        return

    print("Great, " + name + ". You can play the quiz.")

    bank = load_questions()

    while True:
        print("")
        print("Starting a new round of " + str(len(bank)) + " questions.")
        ask_round(name, bank)
        if not play_again():
            print("Thanks for playing, " + name + ". Goodbye.")
            break
        
main()