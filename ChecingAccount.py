class CheckingAccount:

    def __init__(self, name) -> None:
        self.name = name
        self.__balance = 0

    # # add to balance # #
    def credit(self, amount):
        self.__balance +=amount

    # # subract from balance
    def debit(self, amount):
        self.__balance -=amount

    # # show the balance # #
    def get_balance(self):
        print(f'{self.name} has {self.__balance}$ in checking account')

John_Account = CheckingAccount('John')
John_Account.get_balance()
John_Account.credit(100)
John_Account.debit(10)
John_Account.get_balance()

# # no direct access # #
print(John_Account.__balance)

# # no direct reassignment # #
John_Account.__balance = 1000000
print(John_Account.__balance)