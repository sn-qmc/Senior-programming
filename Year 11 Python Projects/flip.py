#Get an input from the user
#Flip the input
#output the flipped value

to_be_flipped = input("Enter value: ")
#This create a variable called flipped,
#and starts it with it as empty text
#It is safer to initialise variables like this
flipped = ""

#A function or def that takes two variables
def checkPalindrome(orignal, flip):
    #it then compares the two and returns
    #a true or false value
    return orignal == flip

#When you create a loop that needs to run for a specific amount,
#you need a variable to keep track of the number of times it has looped
# 'i' is tradition for the name of that variable
#len(to_be_flipped) gets the total number of characters/letters
#inside of to_be_flipped
#We subtract 1 because computers count from 0
#So even if there are 9 letters, it is in the 8th position
i = len(to_be_flipped)-1
while i >= 0:
    flipped += to_be_flipped[i]
    i -= 1
print(flipped)
#Using the true or false returned we check
if checkPalindrome(to_be_flipped, flipped):
    print("Its a palindrome!")
else:
    print("Its not a palindrome!")