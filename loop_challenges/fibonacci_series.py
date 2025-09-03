n = int(input('Enter a number : '))
a = 0
b = 1

for i in range(n+1):
    if i == 0:
        print(a)
        continue

    if i == 1:
        print(b)
        continue

    c = a + b
    print(c)

    a = b
    b = c