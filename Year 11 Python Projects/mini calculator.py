def main():
    # Simple text calculator: input an equation, split it, compute it, print the answer
    print("Please enter a question, in this format below:")  # Display instructions to the user

    equation = input("number operator number, eg 3 x 3 \n>: ")  # Get the user's equation as a string

    while True:  # Keep looping until valid input is processed
        try:  # Try running the code that could fail (bad input, wrong format, etc.)

            terms = equation.split(" ")  # Split the input into a list using spaces

            first_num = int(terms[0])  # Convert the first item to an integer
            operator = terms[1]  # Store the operator as a string
            second_num = int(terms[2])  # Convert the third item to an integer

            answer = 0  # Create a variable to store the result

            if operator == "+":  # Check if the operator is addition
                answer = first_num + second_num  # Add the two numbers
            elif operator == "-":  # Check if the operator is subtraction
                answer = first_num - second_num  # Subtract the second number from the first
            elif operator == "x":  # Check if the operator is multiplication
                answer = first_num * second_num  # Multiply the two numbers
            elif operator == "/":  # Check if the operator is division
                answer = first_num / second_num  # Divide the first number by the second
            else:  # If the operator is not one of the supported ones
                int("Redo")  # Force an error so the program goes to except

            print(f"{equation} = {answer}")  # Output the full equation and the computed answer

        except:  # If any error happens above (format, conversion, missing parts, etc.)
            equation = input("Please enter a valid equation following the format above \n>: ")  # Ask again
        else:  # If there were no errors in the try block
            break  # Exit the loop because the calculation succeeded
    playAgain()

def playAgain():
    playerInput =  input("Want to play again?")
    if(playerInput == "y" or playerInput == "yes"):
        main()
    else:
        quit()

main()