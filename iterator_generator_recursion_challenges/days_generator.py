import random

def days():
    d = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
    i = 0
    while True:
        yield d[i]
        i = (i + 1) % 7

days_generator = days()

days_pass = random.randint(1, 365)

rand_day = None
for n in range(days_pass):
    rand_day = next(days_generator)

print(rand_day)

