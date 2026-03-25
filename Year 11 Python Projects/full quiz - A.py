# Quiz Program: Achieved Level
print("Welcome to the Quiz!")

#Ask for the user's name
name = input("What is your name? ")

play_again = "y"

while play_again == "y":

    #Ask for the user's age
    age = int(input("Hi " + name + ", how old are you? "))

    #Only allow ages 9 to 13
    if age < 9 or age > 13:
        print("Sorry " + name + ", you cannot play.")
        break

    print("Great, " + name + "! Let's start the quiz.")

    #Lists of questions and answers
    questions = [
        "What is the capital of France?",
        "What is 5 + 7?",
        "What planet do we live on?",
        "What is the opposite of hot?",
        "How many days are in a week?"
    ]

    answers = [
        "Paris",
        "12",
        "Earth",
        "Cold",
        "7"
    ]

    #Ask the 5 questions
    index = 1
    while index < 6:
        print("")
        print("Question " + index + ": " + questions[index-1])
        user_answer = input("Your answer: ")
        if(user_answer == answers[index-1]):
            print("Correct!")
        else:
            print("Wrong!")
        index = index + 1

    #Ask if they want to play again
    print("")
    play_again = input("Do you want to play again? (y/n): ")

#End
print("Thanks for playing, " + name + "!")