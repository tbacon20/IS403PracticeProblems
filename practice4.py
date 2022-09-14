# Author: Tanner Bacon
"""
Write a program that prompts the user to enter in the full name, 
birth year, sum of all test scores, and number of tests that made 
up that sum (i.e., 500 is the sum and there were 5 tests) for two 
different individuals in four separate prompts for each individual 
(one for the first full name, one for the first birth year, etc.).         
"""

# Gather inputs for person 1
sFullName1 = input("Enter the full name: ")
iBirthYear1 = int( input("Enter the birth year: "))
iSumTests1 = int( input("Enter the sum of the test scores: "))
iNumTests1 = int( input("Enter the number of tests: "))

# Gather inputs for person 2
sFullName2 = input("Enter the full name: ")
iBirthYear2 = int( input("Enter the birth year: "))
iSumTests2 = int( input("Enter the sum of the test scores: "))
iNumTests2 = int( input("Enter the number of tests: "))

# Do the math
fAverage1 = round(iSumTests1 / iNumTests1, 1)
fAverage2 = round(iSumTests2 / iNumTests2, 1)
bHighScore = fAverage1 > fAverage2

# Print with format: JOHN DOE born in 1990 scored 452 points on 6 tests for an average of 75.3 %
print(sFullName1.upper() + " born in " + str(iBirthYear1) + " scored " + str(iSumTests1) + \
    " points on " + str(iNumTests1) + " tests for an average of " + str(fAverage1) + " %")
print(sFullName2.upper() + " born in " + str(iBirthYear2) + " scored " + str(iSumTests2) + \
    " points on " + str(iNumTests2) + " tests for an average of " + str(fAverage2) + " %")

# Print with format: Did JOHN DOE score higher than JANE EYRE?
print("Did " + sFullName1.upper() + " score higher than " + sFullName2.upper() + "?")
print(bHighScore)