a = 5
b = 2
try:
    print("resource opened")
    print(a/b)
    k = int(input("enter the number: "))
    print(k)
except ValueError as e:
    print('Invalid input or do not enter alphabets', e)
except ZeroDivisionError as e:
    print('a number cannot be divided by zero', e)
except Exception as e:
    print('Something went wrong')
finally:    
    print("resource closed")
print("Bye")