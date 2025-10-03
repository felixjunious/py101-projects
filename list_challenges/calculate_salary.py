print('Enter Hours separated by spaces')
print('e.g. : 8 9 8 7 6 0 0')

hours = input('Enter Hours : ')
wage = int(input('Enter Hourly Wage: '))

ot_rate = 1.5

hours_list = hours.split()
hours_list = [int(x) for x in hours_list]

total_hours = sum(hours_list)

if total_hours <= 40:
    total_wages = total_hours * wage
else:
    overtime_wages = (total_hours - 40) * wage * ot_rate
    total_wages = (40 * wage) + overtime_wages


print('Total Wages:', total_wages)