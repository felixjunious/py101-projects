class InsufficientFundsError(Exception):
    def __init__(self, msg='Not Enough Funds'):
        self.msg = msg

    def __str__(self):
        return self.msg

class BankAccount:
    acc_counter = 1

    def __init__(self, name, balance):
        self.__acc = BankAccount.acc_counter
        self.name = name
        self.__balance = balance
        BankAccount.acc_counter += 1

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            raise InsufficientFundsError

    def get_balance(self):
        return self.__balance

    def details(self):
        print(f'Account No\t: {self.__acc}')
        print(f'Name\t\t: {self.name}')
        print(f'Balance\t\t: {self.get_balance()}')

if __name__ == '__main__':
    nino = BankAccount('Nino', 1000)
    nana = BankAccount('Nana', 1800)

    nino.details()
    print()
    nana.details()
