item_count = int(input('How many items to add on the menu : '))

items = []
prices = []
total_dots = []

for i in range(0, item_count):
    items.append(input('Enter the item  : '))
    prices.append(input('Enter the price : '))
    total_dots.append(26 - len(items[i]) - len(prices[i]))

print('\n')
print('MENU'.center(27, '='))

for i in range(0, item_count):
    dots = '.' * total_dots[i]
    print(items[i] + dots + '$' + prices[i])

print('='*27)

