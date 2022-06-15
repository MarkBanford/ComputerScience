'''Define a BankAccount class that takes a single instance attribute: initial_balance'''


class BankAccount:
    initial_balance = 0

    def __init__(self, initial_balance):
        self.initial_balance = initial_balance

    def deposit(self, amt_to_deposit: int):
        if amt_to_deposit <= 0:
            pass
        else:
            return amt_to_deposit

    def withdraw(self, amt_to_withdraw: int):
        if amt_to_withdraw <= 0:
            pass
        else:
            return amt_to_withdraw


class Savings(BankAccount):
    pass

