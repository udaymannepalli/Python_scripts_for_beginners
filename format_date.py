# to get the current date time we need to use the datetime library
from datetime import datetime, timedelta 

today = datetime.now()
# The now function returns current date&time as datetime object
print('Day is: ' + str(today.day))
print('Month is: ' + str(today.month))
print('Year is: ' + str(today.year))
print('minute is: ' + str(today.minute))
print('Second is: ' + str(today.second))