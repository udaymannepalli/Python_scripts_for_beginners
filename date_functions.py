# to get the current date time we need to use the datetime library
from datetime import datetime, timedelta 

today = datetime.now()
# The now function returns current date&time as datetime object
print('Today is: ' + str(today))

#Let's use time delta function for substracting or adding days/weeks/years
one_day = timedelta(days=1)
tomorrow = today + one_day
print('Yesterday is: ' + str(tomorrow))

# #last week sample
# one_week = timedelta(weeks=1)
# last_week = today - one_week
# print('Last week is: ' + str(last_week))


