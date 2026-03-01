#Print command to ask what is the user's guess and give them range
#Check if the guess is a number
#If it is number, say higher or lower or correct
#Loop
#If its correct we want say how many guess it took

target_number = 57
player_guess = ""
number_of_guesses = 0

while True:
    print("Between 1-100, what is your guess:")
    player_guess = input()

    while not player_guess.isnumeric():
        player_guess = input("Please enter a valid number between 1-100: ")
        
    player_guess = int(player_guess)

    if(player_guess > 100 or player_guess < 1):
        print("Please enter a valid number between 1-100: ")
        
    elif(player_guess > target_number):
        print("Your guess is too high!")
        number_of_guesses+=1
        
    elif(player_guess < target_number):
        print("Your guess is too low!")
        number_of_guesses+=1
        
    else:
        print("You have found the number!")
        break