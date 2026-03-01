def verifyNumberInput(question):
    while True:
        check_number = input(question)
        try:
            check_number = int(check_number)
            break
        except:
            print("Please enter a valid number")
    return check_number
            
def printTable():
    times_table = verifyNumberInput("Please enter the times tables you want printed: ")
    number_of_rows = verifyNumberInput("Please enter the how many rows you want printed: ")
    for i in range(number_of_rows+1):
        print(f'{times_table} x {i} = {times_table*i}')

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
    
    printTable()
    while playAgain():
        printTable()
        
main()