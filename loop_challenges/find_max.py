count_nums = int(input('Enter the total count of numbers : '))
counter = 0

max = int(input('Enter a number : '))

while counter < count_nums:
    n = int(input('Enter a number : '))

    if n > max:
        max = n

    counter += 1

print('Max number is', max)

