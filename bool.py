# true or false
# based on user inputs we will make sure that the student is 
# a distinction student or not and print the value using boolean

gpa = float(input('What was your grade point average? '))
lowest_grade = float(input('What was your lowest grade? '))

if gpa >= 85 and lowest_grade >= 70:
    distinction = True
else:
    distinction = False

if distinction:
    print('You are a distinction student!!')