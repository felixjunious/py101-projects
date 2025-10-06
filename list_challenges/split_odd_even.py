nums = [4, 8, 3, 5, 10, 7, 2, 9, 13, 6]

odd = [num for num in nums if (num % 2) != 0]

even = [num for num in nums if (num % 2) == 0]

print('Odd :', odd)
print('Even :', even)