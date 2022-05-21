# I check to see if the requirements for distinction roll are met
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = input('What was your lowest grade? ')
lowest_grade = float(lowest_grade)

if gpa >= .85 and lowest_grade >= .70:
    distincion_roll = True
else:
    distincion_roll = False

#somewhere later in your code if you need to check if students 
# is on distincion roll, all I need to do is check the boolean 
# variable I set earlier in my code

if distincion_roll:
    print('You made the distincion!!')