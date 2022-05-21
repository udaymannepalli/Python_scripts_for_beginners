# nested if - multiple conditions inside 
# country name ? - if country is india then we will ask for state name
# 3 states - taxes # other state in india - assign tax
# close with if they are not from india tax = 0 
country = input('What is your country name? ')
# first we will verify the country and make sure it is india
# then only we will ask for state 
if country.lower() == 'india':
    state = input('What is your state name? ')
    if state.lower() in ('telangana' , 'andhra' , 'tamilnadu'):
        tax = 0.05
    elif state == 'kerala':
        tax = 0.25
    else:
        tax = 0.5020
else: 
    tax = 0
print('Tax is ' + str(tax))
    
