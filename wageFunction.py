# Author: Tanner Bacon
""" 
Create another file called "wage_functions.py" and 
write a function called calc_pay 
    that receives the hours worked, 
    hourly wage, 
    tax rate, and 
    FICA rate. 
    This function will calculate the weekly take home pay by 
    multiplying the hours worked in the week by the hourly wage and 
    rounding to the nearest 10th of a cent. 
"""

# This function will calculate the take home amount
def calc_wage(fHours, fWage, fTaxRate, fFICARate):
    
    # Find the pretax income and the tax / fica amounts
    fPreMullahBaby = round(fHours * fWage, 2)
    fTax = fPreMullahBaby * round(fTaxRate/100, 3)
    fFICA = fPreMullahBaby * round(fFICARate/100, 4)

    # Deduct tax/fica amounts for take home amount
    fMullahBaby = fPreMullahBaby - fTax - fFICA

    # Return take home amount
    return fMullahBaby