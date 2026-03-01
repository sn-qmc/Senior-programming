import random
from enum import Enum

EXIT_CODE = "quit"
MENU_CODE = "menu"
OPTIONS = ("rock", "paper", "scissors")

class GameType(Enum):
    NORMAL = 0
    PLAYER_ALWAYS_WINS = 1
    PLAYER_ALWAYS_LOSES = 2

win_determination = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock",
}

lose_determination = {v: k for k, v in win_determination.items()}

def checkValidInput(question, acceptedAnswers):
    while True:
        checkValue = input(question).strip().lower()
        if checkValue == EXIT_CODE or checkValue == MENU_CODE:
            return checkValue
        if checkValue in acceptedAnswers:
            return checkValue
        print("Please enter a valid input!\n")

def print_status(round_no, max_rounds, player_score, computer_score):
    print(f"Round: {round_no}/{max_rounds}")
    print(f"Player Score: {player_score}")
    print(f"Computer Score: {computer_score}")

def get_computer_choice(game_type: GameType, player_input: str) -> str:
    if game_type == GameType.NORMAL:
        return random.choice(OPTIONS)
    elif game_type == GameType.PLAYER_ALWAYS_WINS:
        return win_determination[player_input]
    else:  # GameType.PLAYER_ALWAYS_LOSES
        return lose_determination[player_input]

def determine_winner(player: str, computer: str) -> str:
    if player == computer:
        return "draw"
    if win_determination[player] == computer:
        return "player"
    return "computer"

def menu():
    menuOptions = ["1", "2", "3"]
    print("\n\n\n\nWelcome to Rock Paper Scissors, choose from the following options!")
    print("1. Play")
    print("2. Extra Options")
    print("3. Quit")
    return checkValidInput("Please choose one of the above 3 options: ", menuOptions)

def secretMenu():
    cheatOptions = ["iwannawin", "iwannalose"]
    print("Welcome to the extra options: ")
    print("If you know the secret code enter it below\nElse\nType 'quit' to exit\n'menu' to return:")
    chosen = checkValidInput("", cheatOptions)
    if chosen == EXIT_CODE or chosen == MENU_CODE:
        return chosen
    if chosen == "iwannawin":
        print("Starting winners mode:")
        return GameType.PLAYER_ALWAYS_WINS
    else:  # "iwannalose"
        print("Starting losers mode:")
        return GameType.PLAYER_ALWAYS_LOSES

def getNumberOfRounds():
    roundOptions = ["3", "5", "7", "9"]
    rounds = checkValidInput("How many rounds would you like to play?: ", roundOptions)
    if rounds in (EXIT_CODE, MENU_CODE):
        return rounds
    return int(rounds)

def play(game_type: GameType):
    print("Welcome to Rock Paper Scissors!\n"
          f"At any time you may return to the beginning by typing '{MENU_CODE}'\n"
          f"or exit by typing '{EXIT_CODE}'.")
    max_rounds = getNumberOfRounds()
    if max_rounds == EXIT_CODE:
        return EXIT_CODE
    if max_rounds == MENU_CODE:
        return MENU_CODE

    wins_needed = max_rounds // 2 + 1 

    counter = 1 
    player_score = 0
    computer_score = 0

    while True:
        print_status(counter, max_rounds, player_score, computer_score)
        player_input = checkValidInput(
            f"Please choose one of the following options:\n{list(OPTIONS)}\n",
            list(OPTIONS)
        )

        if player_input == EXIT_CODE:
            return EXIT_CODE
        if player_input == MENU_CODE:
            return MENU_CODE

        computer_choice = get_computer_choice(game_type, player_input)
        print(f"The computer played {computer_choice}!")

        outcome = determine_winner(player_input, computer_choice)
        if outcome == "draw":
            print("Draw!")
        elif outcome == "player":
            print("Player wins!")
            counter += 1
            player_score += 1
        else:
            print("Computer wins!")
            counter += 1
            computer_score += 1

        if computer_score >= wins_needed:
            print("The computer wins the game!\n\n\n\n")
            return "done"
        elif player_score >= wins_needed:
            print("The player wins the game!\n\n\n\n")
            return "done"
        else:
            if counter > max_rounds:
                if player_score > computer_score:
                    print("The player wins the game!\n\n\n\n")
                elif computer_score > player_score:
                    print("The computer wins the game!\n\n\n\n")
                else:
                    print("The game is a draw!\n\n\n\n")
                return "done"
            print("Next round starting!\n\n\n\n")

def playAgain():
    yesAnswers = ["yes", "y", "yeah"]
    noAnswers = ["no", "n", "nah"]
    answer = checkValidInput("Would you like to play again?: ", yesAnswers + noAnswers)
    if answer in (EXIT_CODE, MENU_CODE):
        return answer
    return "yes" if answer in yesAnswers else "no"

def run():
    while True:
        choice = menu()
        if choice == EXIT_CODE or choice == "3":
            print("Goodbye!")
            break
        
        if choice == MENU_CODE:
            continue

        if choice == "2":
            gt = secretMenu()
            if gt == EXIT_CODE:
                print("Goodbye!")
                break
            if gt == MENU_CODE:
                continue
            result = play(gt)
        else:
            result = play(GameType.NORMAL)

        if result == EXIT_CODE:
            print("Goodbye!")
            break
        if result == MENU_CODE:
            continue
        
        again = playAgain()
        if again == EXIT_CODE:
            print("Goodbye!")
            break
        if again == MENU_CODE:
            continue
        if again == "no":
            print("Goodbye!")
            break
      
run()