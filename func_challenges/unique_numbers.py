def unique_nums(*args):
    nums = set(args)
    return sorted(list(nums))

numbers = input('Enter numbers seperated by spaces : ')

numbers_list = [int(n) for n in numbers.split()]
unique_numbers = unique_nums(*numbers_list)

print('Unique numbers:', unique_numbers)

