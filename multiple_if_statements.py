state = input('What state do you live in? ')
tax = 0

if state == 'Telangana':
    tax = 0.05
if state == 'Andhra Pradesh':
    tax = 0.05
if state == 'Tamilnadu':
    tax = 0.13

print(tax)

    
# use elif inside if statement which makes 
# use else: tax = 0.20 so that if we enter 
# the state which is out of the scope so that the tax is .20


# if province == 'Telangana' or province == 'Andhra Pradesh':

# if province in('Telangana', 'Andhra Pradesh', 'Karnataka'):
#the above is an example of list