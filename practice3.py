# Author: Tanner Bacon
"""
This program prompts the user for a first name, 
last name, street address, city, state, 
and the birth year of the individual. 
It then calculates the age of the individual
and print the concatenated full name all in uppercase, 
with the first and last name separated by a space. 
It them prints the address on a separate line, the city,
and state on another separate line separated by a tab. 
The name and state will be all caps.
The calculated age in years is on another separate line 
concatenated with "In 2020 ZZ was XX years old"—where ZZ 
is the first name and XX is the calculated age in years.

The output looks similar to:
      GEORGE MCFLY
      9303 Lyon Drive
      Hill Valley     CA
      In 2020 George was 82 years old
"""

sFirstName = input("Enter your first name: ")
sLastName = input("Enter your last name: ")
sFirstNameUpper = sFirstName.upper()
sLastNameUpper = sLastName.upper()

sStreetAddress = input("Enter your street address: ")
sCity = input("Enter your city: ")
sState = input("Enter your state: ").upper()

iYear = 2020
iBirthYear = input("Enter your birth year: ")
iAge = iYear - int(iBirthYear)

print(f'{sFirstNameUpper} {sLastNameUpper}\n{sStreetAddress}\n{sCity}\t{sState}')
print(f'In {iYear} {sFirstName} was {str(iAge)} years old')