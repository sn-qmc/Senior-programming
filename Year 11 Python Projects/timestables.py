#Ask for player's input on which timestable the want
#Ask how many rows would you like
#Print all of the times tables up to that row
#Check if they want to try again

def getInput():
    timestableRow = ""
    timestableColumn = ""
    
    while True:
        timestableColumn = input("Which timestable would you like printed?: ")
        try:
            timestableColumn = int(timestableColumn)
            break
        except:
            print("Please enter a valid number")
    
    while True:
        timestableRow = input("How many rows would you like printed?: ")
        try:
            timestableRow = int(timestableRow)
            break
        except:
            print("Please enter a valid number!")
            
    return [timestableColumn, timestableRow]

def printTable(tableRange):
    numColumn = tableRange[0]
    numRow = tableRange[1]
    
    for i in range(numRow+1):
        print(f'{numColumn} x {i} = {numColumn*i}')
        
def playAgain():
    yesAnswers = ["yes", "y","yeah","ye"]
    noAnswers = ["no", "n", "nah", "noew"]
    anotherRound = ""
    
    while True:
        anotherRound = input(f"Would you like to try again?: \n{yesAnswers}\n{noAnswers}\n").lower()
        if anotherRound in yesAnswers:
            return True
        elif anotherRound in noAnswers:
            return False
        else:
            print(f"Please enter a valid answer!\n")

def main():
    
    printTable(getInput())
    while playAgain():
        printTable(getInput())
        
main()