# we use and instead of nested if loops
# student makes distincion if their average is >=85
# and their lowest grade is not below >= 70
# grade point average

gpa = float(input('What was your grade point average? '))
lowest_grade = float(input('What was your lowest grade? '))

if gpa >= 85 and lowest_grade >= 70:
    print('Well done, you are a distincion student! ')