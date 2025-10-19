import calendar as cal

def next_month():
    i = 1
    while True:
        yield cal.month_abbr[i]
        i = i % 12 + 1

if __name__ == '__main__':

    month_generator = next_month()

    for i in range(24):
        print(next(month_generator))