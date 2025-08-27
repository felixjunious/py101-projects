amount = int(input('Enter bill amount : '))

if amount <= 1000:
    discount = amount * 0.1
elif amount > 1000 and amount <= 5000:
    discount = amount * 0.2
elif amount > 5000 and amount <= 10000:
    discount = amount * 0.3
else:
    discount = amount * 0.5

discounted_amount = amount - discount

print('Pay ', discounted_amount)