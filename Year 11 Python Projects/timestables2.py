def getIntInput(question):
    value = ""
    while True:
        value = input(question)
        try:
            value = int(value)
            break
        except:
            print("Please enter a vaild input!")  
    return value
def printTimestable():
    base = getIntInput("Please enter the timestables you want printed?")
    rows = getIntInput("Please enter the last row you want printed?")
    for i in range(rows+1):
        print(f"{base} x {i} = {base * i}")
def playAgain():
    yesAnswers = ["yes", "y"]
    noAnswers = ["no", "n"]
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
    printTimestable()
    while playAgain():
        printTimestable()   
main()