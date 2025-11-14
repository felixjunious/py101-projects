from collections import Counter

prices = {"soap": 50, "toothpaste": 25, "shampoo": 45.50, "toothbrush": 15.99}

def generate_bill(cart):

    total = 0
    for item, qty in cart.items():
        print(item, prices[item], 'x', qty, "=", prices[item] * qty)
        total += prices[item] * qty

    print("Total:", total)

cart = Counter(soap=5, toothpaste=1, shampoo=2, toothbrush=3)
generate_bill(cart)