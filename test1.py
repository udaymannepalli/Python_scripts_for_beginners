
try:
    numerator = int(input('enter the numerator: '))
    denominator = int(input('enter the denominator: '))
    result = numerator / denominator
    print(result)
except ZeroDivisionError:
    print('Denominator cannot be 0, please enter a valid number')

print('Program ends')

