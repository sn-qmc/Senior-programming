#Choose a random word
#A player input for an attempt
#know what are the correct letters
#Increase a chance death if wrong
#-------------Variables----------------------------
max_guesses = 11
wrong_guesses = 0
correct_word = "Queen"
player_input = ""
#------------End of Variables---------------------

#-----------Definitions-------------------------

def checkCharacters(wrong_guesses):
    if(correct_word.lower().__contains__(player_input.lower())):
        print("Good Guess!")
    else:
        print("Oh no!")
        wrong_guesses += 1

def checkWord(wrong_guesses):
    if(correct_word.lower() == player_input.lower()):
        print("Good Guess!")
    else:
        print("Oh no!")
        wrong_guesses += 1
        
def loopAsk():
    global player_input
    #Get player input and check if it is alphabet only
    while not player_input.isalpha():
        player_input = input("Please enter a guess (Only Alphabetical): ")

    #If the input is a word or if the input is a character
    if(len(player_input) == 1):
        checkCharacters(wrong_guesses)
    else:
        checkWord(wrong_guesses)
        
def main():
    while(wrong_guesses < max_guesses):
        loopAsk()
        
#-----------End of Definitions-----------------

main()
    
