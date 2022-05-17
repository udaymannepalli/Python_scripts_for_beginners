
x = int(input('How many candies you want? '))
i = 1
while i <= x:
    print('candy')
    i+=1

stock = 5
x = int(input('How many candies you want? '))

i = 1 # initializaion
while i <= x: # condition
    if i > stock: # Inner loop where we are comparing the stock with the user input
        print('out of stock') # print statement
        break # we are telling the program to jump out of the loop/get out from here :P
    print('candy') 
    i+=1 # increment value

print('bye')

# here we want to skip the numbers divisible by 3 and continue the loop

for i in range(1,101): #mentioned the range
    if i %3 == 0: # provided the condition that if a number is divisible by 3
        continue # we are saying continue which means skip the numbers, WONT jump out of the loop
    print(i) # print the i value
print('Bye')

for i in range(1,20): # starting with 1 till 20
    if i %2 == 0: # condition where the reminder is equal to zero which means it is an even number
        pass # just ignore the if statement and proceed with else
    else:
        print(i) # print the i value
print("bye")



