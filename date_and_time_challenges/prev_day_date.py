import datetime as dt

def prev_day(day):

    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    today = dt.date.today()

    t_dw = today.weekday()
    dw = week_days.index(day)
    diff = dw - t_dw

    if diff >= 0:
        diff = -(7-diff)

    new_date = today + dt.timedelta(diff)
    return new_date

print('Today: ', dt.date.today())
print('Prev Sunday: ', prev_day('sunday'))

