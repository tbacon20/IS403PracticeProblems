# Author: Tanner Bacon
"""
Write a program that will continue to generate two random 
numbers until they are not equal. Then display the two numbers.
"""
# Import random library
import random

# Initialize maximum and random numbers
iMax = int( input("Enter the maximum number: "))
iRand1 = 0
iRand2 = 0

# Continues guessing until numbers are not equal
while iRand1 == iRand2:
    iRand1 = random.randrange(0, iMax)
    iRand2 = random.randrange(0, iMax)

    # Let the user know when it's guessing again
    if iRand1 == iRand2:
        print("Both numbers are: " + str(iRand1) + ", guessing again")

# Print the final nonequal numbers
print("Nonequal numbers are " + str(iRand1) + " and " + str(iRand2))