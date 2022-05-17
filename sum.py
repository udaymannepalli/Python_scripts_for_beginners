#input - state?
# 3 states; taxes: 0.50(telangana),0.50(andhra),0.25(tamilandu)
# based on input we will print tax

state = input('enter the state name: ')

if state in ('telangana' , 'andhra'):
    tax = 0.5
elif state == 'tamilnadu' or 'bihar':
    tax = 0.25
else:
    tax = 0.99
print(tax)

