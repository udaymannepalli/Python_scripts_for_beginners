country = input('what country do you live in? ')

if country.lower() == 'India':
    state = input('what state do you live in? ')
    if state in ('telangana', \
        'andhra', 'tamilnadu'):
        tax = 0.05
    elif state == 'karnataka':
        tax = 0.13
    else:
        tax = 0.15
else: 
    tax = 0
    
print(tax)
    