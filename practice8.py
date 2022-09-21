# Author: Tanner Bacon
"""
Create a file called "wages.py"
prompts the user to enter an employee's name, 
    the total number of hours worked for the week, 
    the hourly wage, 
    the tax rate (i.e., 3.2% includes federal, state, and local taxes), 
    and FICA (i.e., 7.65%). 
 """
#Import the wage function
from practice8a import calc_wage

# Initialize variables
sName = input("Enter the employee's name: ")
fHours = float( input("Enter the number of hours worked for the week: "))
fWage = float( input("Enter the hourly wage: "))
fTaxRate = float( input("Enter the tax rate: "))
fFICA = float( input("Enter FICA: "))

# Calculate take home pay
fMullahBaby = calc_wage(fHours, fWage, fTaxRate, fFICA)

# Print final statementl
print(sName + " worked " + "{:.2f}".format(fHours) + \
    " hours in the week at " + "${:,.2f}".format(fWage) + \
    " an hour and took home " + "${:,.2f}".format(fMullahBaby))