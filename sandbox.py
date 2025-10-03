name = 'Raj'
roll = 10
avg = 78.5
print('{}--{}--{}'.format(name, roll, avg))

item = 'Memory'
size = 32
price = 11.72
print('{0}GB {1} in ${2}'.format(size, item, price))

data  = 100
print('start {0:15} end'.format(data))
print('start {0:<15} end'.format(data))
print('start {0:^15} end'.format(data))

data2 = 100
print('binary {0:b}'.format(data2))
print('octal {0:o}'.format(data2))
print('hexadecimal {0:x}'.format(data2))

large_num = 123456789
print('start {0:,} end'.format(large_num))
print('start {0:_} end'.format(large_num))

item = 'Memory'
size = 32
price = 11.75
print(f'{size}GB {item:*^10} in ${price:.2f}')

num_positive = 100
num_negative = -100
print(f'{num_positive:+d}, {num_negative:+d}')
print(num_positive, num_negative)