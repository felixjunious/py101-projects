class InsufficientFundsError(Exception):
    def __init__(self, msg=''):
        self.msg = msg

    def __str__(self):
        return self.msg

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError('Not enough funds')

    return balance - amount

balance = 5000
try:
    amount = int(input('Enter Amount: '))
except EOFError:
    print('Input stream closed unexpectedly.')
except ValueError:
    print('Please enter a valid whole number.')
else:
    print('You entered:', amount)


try:
    balance = withdraw(balance,amount)
except InsufficientFundsError as e:
    print(e)
else:
    print('Withdrawal successful')
    print('Remaining balance : ', balance)



