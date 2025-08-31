n = int(input('Enter a number : '))
m = n
rev = 0

while n > 0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10

if rev == m:
    print('Number is a palindrome')
else:
    print('Number is not a palindrome')