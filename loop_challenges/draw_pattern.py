print('Pattern 1 :')

for i in range(5):
    for j in range(5):
        print('*', end='')
    print('')

print()
print('Pattern 2 :')

for i in range(5):
    for j in range(5):
        if i >= j:
            print('*', end='')
    print('')

print()
print('Pattern 3 :')

for i in range(5):
    for j in range(5):
        if i <= j:
            print('*', end='')
    print('')
