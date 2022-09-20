# Author: Tanner Bacon
"""
Write a program that prompts the user to enter the 
maximum number used in generating a random number. 
Then generate the random number. Start the timer as 
the user tries to guess the number. Display whether 
the guess is "Too High" or "Too Low". Once the number 
is guessed, display how many seconds it took to guess 
the number.
"""
# Import date and random
import random
from datetime import datetime
from this import d

# Collect random number
iMax = int( input("Enter the maximum number: "))

# Set the range, initialize the guess outside of the range, start the timer
iRand = random.randrange(1, iMax)
iGuess = iRand + 1
dStartTime = datetime.now()

# Collect the user guess and make them continue guessing until they get the number
while (iGuess != iRand):
    iGuess = int( input("Guess the random number between 1 and " + str(iMax) + ": "))
    if iGuess != iRand:
        print("Wrong, try again!")

# Calculate the time it took to guess the answer and congratulate the user
dTimeElapsed = datetime.now() - dStartTime
print("Good job, you guessed the number in " + str(dTimeElapsed.seconds) + " seconds.")
print("The number was " + str(iRand) + ".")