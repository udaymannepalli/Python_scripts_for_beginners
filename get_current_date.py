# to get the current date time we need to use the datetime library
from datetime import datetime
current_date = datetime.now()
# print(current_date)
# The now function returns current date&time as datetime object
# print(current_date)
# we must convert the datetime object to a string
# before you can concatenate to another string
print('Today is: ' + str(current_date))