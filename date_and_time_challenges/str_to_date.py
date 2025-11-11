import datetime

def string_to_date(str_date):
    d, m, y = str_date.split('-')
    return datetime.date(int(y), int(m), int(d))


print(string_to_date('01-01-2001'))
