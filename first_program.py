# print current date
from datetime import datetime, timedelta
current_date = datetime.now()
print('today is: ' + str(current_date.day))
print('month is: ' + str(current_date.month))
print('year is: ' + str(current_date.year))
# print yesterday (today - 1 day) - timedelta class
# one_day = timedelta(days=1)
# tomorrow = current_date + one_day
# print('tomorrow is: ' + str(tomorrow))





