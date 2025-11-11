from datetime import date

def calculate_age(date_of_birth):
    today = date.today()
    years = today.year - date_of_birth.year

    if (today.month, today.day) < (date_of_birth.month, date_of_birth.year):
        years -= 1

    return years

print(calculate_age(date(2007,8,12)))