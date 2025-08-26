math = int(input('Enter the marks for math : '))
physics = int(input('Enter the marks for physics : '))
chemistry = int(input('Enter the marks for chemistry : '))

if math >= 45 and physics >= 45 and chemistry >= 45:
    print('Passed')
else:
    print('Failed')