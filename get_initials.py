# # ask for someones name and return the initials

# first_name = input('Enter your first_name: ')
# first_name_initial = first_name[0:1]

# middle_name = input('Enter your middle_name: ')
# middle_name_initial = middle_name[0:1]

# last_name = input('Enter your first_name: ')
# last_name_initial = last_name[0:1]

# print('Your initials are: ' + first_name_initial \
#     + middle_name_initial + last_name_initial)

# now do the same program with the help of function

def get_initial(name):
    initial = name[0:1]
    return initial

first_name = input('Enter your first_name: ')
first_name_initial = get_initial(first_name)

middle_name = input('Enter your middle_name: ')
middle_name_initial = get_initial(middle_name)

last_name = input('Enter your last_name: ')
last_name_initial = get_initial(last_name)

print('Your initials are: ' + first_name_initial \
    + middle_name_initial + last_name_initial)


