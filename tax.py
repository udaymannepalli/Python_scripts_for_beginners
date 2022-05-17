country = input('What country do you live in? ')

if country.lower() == 'india':
    state = input('What state are you from? ')
    if state in ('andhra' , 'telangana' , 'tamilnadu'):
        tax = 0.25
    elif state == 'kerala':
        tax = 0.50
    else: 
        tax = 0.75
else:
    tax = 0
print(tax)
        