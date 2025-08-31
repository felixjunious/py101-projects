n = int(input('Enter a number : '))
total_digits = 0
while n > 0:
    n = n // 10
    total_digits += 1

print('Number of digits are', total_digits)