count_nums = int(input('Enter the total count of numbers : '))
counter = 0
sum_pos = 0
sum_neg = 0

while counter < count_nums:
    num = int(input('Enter a number : '))

    if num >= 0:
        sum_pos += num
    else:
        sum_neg += num

    counter += 1

print('Positive sum is', sum_pos)
print('Negative sum is', sum_neg)