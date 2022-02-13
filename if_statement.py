#input - state?
# 3 states; taxes: 0.50(telangana),0.50(andhra),0.25(tamilandu)
# based on input we will print tax

state = input('Enter your state name? ')

# if state.lower() == 'telangana' or 'andhra':
if state.lower() in('telangana', 'andhra', 'kerala'):
    tax = 0.50 
    # print('tel tax is ' + str(tax))
# elif state.lower() == 'andhra':
#     tax = 0.50
elif state.lower() == 'tamilnadu':
    tax = 0.25
else:
    tax = 0.75
    # print(tax)
print(tax)
