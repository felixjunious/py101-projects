u = int(input('Enter initial velocity : '))
v = int(input('Enter final velocity : '))
a = int(input('Enter acceleration : '))

d = (v * v - u * u) / (2 * a)

print('Displacement is', d)