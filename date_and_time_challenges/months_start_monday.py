from datetime import *
import calendar

def total_months_starting_monday(year):
    months = []
    total = 0

    for month in range(1,13):
        if date(year,month,1).weekday() == 0:
            months.append(calendar.month_name[month])
            total += 1

    return months, total

print(total_months_starting_monday(2021))