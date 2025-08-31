count_nums = int(input('Enter the total count of numbers : '))
counter = 0
sum = 0

while counter < count_nums:
    num = int(input('Enter a number : '))
    sum += num
    counter += 1

print('The sum of all of the numbers is ', sum)