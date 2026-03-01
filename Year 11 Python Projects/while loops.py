#While loops are permanent repetitions in code till a condtion is met

#number = input("What number am I thinking off?: ")
#correct_number = "4"
#!= or a 'not' inverse comparison, the opposite of a ==, check if they are not equal
#while number != correct_number:
#while not (number == correct_number):
    #print("Wrong!")
    #number = input("What number am I thinking off?: ")

#print("Good job!")

#to check if something is a number, we use .isnumeric()
#to check if something is a letter or string we use .isalpha()

#I want a program that gets the name of someone
#Then checks if it is valid
#Otherwise it will make them loop till it is
#Explain what these lines of code mean
#----
name = input("What is your name?: ")
#----
while not name.isalpha():
    #----
    print("Please enter a valid name with only letters!")
    #----
    name = input("What is your name?: ")
#----
print("Hello", name)
        