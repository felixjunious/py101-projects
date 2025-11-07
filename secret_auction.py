def find_highest_bidder(bids):
    max_bid = 0
    winner = ""

    for bidder in bids:
        if bids[bidder] > max_bid:
            max_bid = bids[bidder]
            winner = bidder

    return winner


print('Welcome to the secret auction program.')

continue_bid = True
bids = {}


while continue_bid:
    name = input("What is your name ? ")
    bid = float(input("What is your bid ? $"))

    bids[name] = bid

    continue_bid = input("Are there any other bidders? Type 'yes' or 'no'.").lower() == 'yes'.lower()

    print("\n" * 20)

highest_bidder = find_highest_bidder(bids)
print(f'The winner is {highest_bidder} with a bid of ${bids[highest_bidder]}')