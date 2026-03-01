#In some ways python is easier, than other code.
#in fact for beginners it is the best language to learn.
#Because of how lenient it is and how similar it is to english.

#variables, main types: 
#int - integer, it stores whole numbers (-ve and +ve)
#all integers store numbers between 2^31 and -2^31
# float - float point integer
#The number stored is basically an integer
#With a small storage for where the decimal point
#Hence the name floating point
#str - string
#It store everything as text

#In your own words write down what these two lines of code do!
# ----
#first_name = input("What is your first name?: ")
# ----
#print("Hello", first_name)

#Adding a hashtag to the start of any code is called commenting it out

#In your own words write down what these four lines of code do!
#----
#birth_year = input("What year where you born?: ")
#----
#birth_year = int(birth_year)
#----
#age = 2026 - birth_year
#----
#print("You are/ or will turn", age, "years old!")

#Make a simple adder, as in, it asks for two numbers
#and adds them together and displays the answer
#----
first_number = input("Enter your first number: ")
second_number = input("Enter your first number: ")
#----
first_number = int(first_number)
second_number = int(second_number)
#----
sum = first_number + second_number
#----
print(first_number, "+", second_number, "=", sum)