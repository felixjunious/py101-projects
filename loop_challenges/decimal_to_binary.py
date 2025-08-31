n = int(input('Enter a number : '))
bin_rev = 0

while n > 0:
    r = n % 2
    n = n // 2
    bin_rev = bin_rev * 10 + r

bin = 0
while bin_rev > 0:
    r = bin_rev % 10
    bin_rev = bin_rev // 10
    bin = bin * 10 + r

print(bin)