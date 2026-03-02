import random

exitCode = "quit"
menuCode = "menu"

# What each move beats
win_determination = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}
# What each move loses to (inverse of win_determination)
lose_determination = {
    "scissors": "rock",
    "paper": "scissors",
    "rock": "paper"
}

def checkValidInput(question, acceptedAnswers):
    checkValue = ""
    while True:
        checkValue = input(question).lower()
        if checkValue == exitCode:
            goodbye()
        elif checkValue == menuCode:
            menu()
        elif checkValue in acceptedAnswers:
            return checkValue
        else:
            print("Please enter a valid input!\n")

def menu():
    menuOptions = ["1", "2", "3"]
    print("\n\n\n\nWelcome to Rock Paper Scissors, choose from the following options!")
    print("1. Play")
    print("2. Extra Options")
    print("3. Quit")
    chosen = checkValidInput("Please choose one of the above 3 options: ", menuOptions)
    if chosen == "3":
        goodbye()
    elif chosen == "2":
        secretMenu()
    else:
        play(0)

def secretMenu():
    cheatOptions = ["iwannawin", "iwannalose"]
    print("Welcome to the extra options: ")
    print("If you know the secret code enter it below\nElse\nType 'quit' to exit\n'menu' to return:")
    chosen = checkValidInput("", cheatOptions)
    if chosen == cheatOptions[0]:
        print("Starting ~~normal mode: ")
        play(1)
    else:
        print("Starting ~normal mode: ")
        play(2)
        
def goodbye():
    print("Goodbye!")
    raise SystemExit

def play(game_type):
    print("Welcome to the Rock Paper Scissors\nAt any time you may return to the beginning by typing 'menu'\nor exit by typing in 'quit'")
    options = ["rock", "paper", "scissors"]
    max_rounds = getNumberOfRounds()
    # Ceiling of max_rounds / 2 (wins needed to cinch match)
    wins_needed = max_rounds // 2 + 1

    counter = 1
    player_score = 0
    computer_score = 0

    while True:
        print(f"Round: {counter}/{max_rounds}")
        print(f"Player Score: {player_score}")
        print(f"Computer Score: {computer_score}")

        player_input = checkValidInput(f"Please choose one of the following options:\n{options}\n", options)

        if game_type == 0:
            # Normal mode: random computer
            computer_choice = random.choice(options)
            print(f"The computer played {computer_choice}!")

            if player_input == computer_choice:
                print("Draw!")
            elif win_determination[player_input] == computer_choice:
                print("Player wins!")
                counter += 1
                player_score += 1
            else:
                print("Computer wins!")
                counter += 1
                computer_score += 1

        elif game_type == 1:
            # Player always wins: computer picks the move that loses to player
            computer_choice = win_determination[player_input]
            print(f"The computer played {computer_choice}!")
            print("Player wins!")
            counter += 1
            player_score += 1

        else:
            # Player always loses: computer picks the move that beats player
            computer_choice = lose_determination[player_input]
            print(f"The computer played {computer_choice}!")
            print("Computer wins!")
            counter += 1
            computer_score += 1

        if computer_score >= wins_needed:
            print("The computer wins the game!\n\n\n\n")
            playAgain()
        elif player_score >= wins_needed:
            print("The player wins the game!\n\n\n\n")
            playAgain()
        else:
            # Proceed only if match not clinched and rounds remain
            if counter > max_rounds:
                # Safety: If maximum rounds reached without someone clinching (e.g., many draws)
                if player_score > computer_score:
                    print("The player wins the game!\n\n\n\n")
                elif computer_score > player_score:
                    print("The computer wins the game!\n\n\n\n")
                else:
                    print("The game is a draw!\n\n\n\n")
                playAgain()
            else:
                print("Next round starting!\n\n\n\n")
              
def playAgain():
    yesAnswers = ["yes", "y", "yeah"]
    noAnswers = ["no", "n", "nah"]
    answer = checkValidInput("Would you like to play again?: ", yesAnswers + noAnswers)
    if answer in yesAnswers:
        menu()
    else:
        goodbye()         
    
def getNumberOfRounds():
    roundOptions = ["3", "5", "7", "9", exitCode, menuCode]
    rounds = checkValidInput("How many rounds would you like to play?: ", roundOptions)
    # checkValidInput already handles 'quit' and 'menu'
    return int(rounds)

menu()