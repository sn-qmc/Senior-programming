#If statement
#----
#first_number = input("Enter your first number: ")
#operator = input("Please enter the operator: ")
#second_number = input("Enter your first number: ")
#----
#first_number = int(first_number)
#second_number = int(second_number)
#----
#In most programming languages a "=" sign means get the result
# A "==" is a comparator it checks if the left equals the right
#sum = 0
#if operator == "+":
#    sum = first_number + second_number
#else if or elif
#elif operator == "-":
#    sum = first_number - second_number
#elif operator == "x":
#    sum = first_number * second_number
#elif operator == "/":
#    sum = first_number / second_number
#else:
#    print("Invalid operation!")
#When you divide two integers it will automatically convert it into a float
#sum = int(sum)
#----
#print(first_number, operator, second_number, "=", sum)

#Indents tell the computer what is inside of conditions and other structures
name = input("What is your name?: ")

if name == "Bob":
    print("Hello friend!")
else:
    name = "Not friend"
print("Hello", name)