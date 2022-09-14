# Author: Tanner Bacon
"""
Write a program that accepts a student’s full name and their 
final grade average (i.e., 95). Then using an IF ELIF ELSE 
statement, display the letter grade using the following legend:   
"""
# Collect inputs
sFullName = input("Enter full name: ")
iGrade = int( input("Enter the grade average: "))
sGrade = "F"
sAnA = "a "

# Determine grade and "a" / "an"
if iGrade > 94:
    sGrade = "A"
    sAnA = "an "
elif iGrade > 90:
    sGrade = "A-"
    sAnA = "an "
elif iGrade > 87:
    sGrade = "B+"
elif iGrade > 83:
    sGrade = "B"
elif iGrade > 80:
    sGrade = "B-"
else: 
    sGrade = "C"

# Print final average and grade 
# Format: JANE EYRE had a final average of 95 which resulted in an A for the course.
print(sFullName.upper() + " had a final average of " + str(iGrade) + \
    " which resulted in " + sAnA + sGrade + " for the course.")