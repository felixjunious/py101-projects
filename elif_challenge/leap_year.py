year = int(input('Enter year : '))

if year % 100 == 0:
    if year % 400 == 0:
        print('Leap Year')
    else:
        print('Not a leap year')
elif year % 4 == 0:
    print('Leap year')
else:
    print('Not a leap year')