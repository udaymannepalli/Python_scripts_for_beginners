# we use and instead of nested if loops
# student makes distincion if their average is >=85
# and their lowest grade is not below 70
# grade point average
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = input('What was your lowest grade? ')
lowest_grade = float(lowest_grade)

if gpa >= .85:
    if lowest_grade >= .70:
        print('You made the distinction')
        
# if gpa >= .85 and lowest_grade >= .70:
#     print('You made the distinction')