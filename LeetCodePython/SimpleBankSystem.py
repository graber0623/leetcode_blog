from collections import defaultdict

class Bank:
    def __init__(self, balance):
        self.bal = {}
        for i, amount in enumerate(balance):
            self.bal[i+1] = amount

    def account_exists(self, account):
        return account in self.bal

    def deposit(self, account, money):
        if self.account_exists(account) and money >= 0:
            self.bal[account] += money
            return True
        else:
            return False

    def withdraw(self, account, money):
        if self.account_exists(account) and 0 <= money <= self.bal[account]:
            self.bal[account] -= money
            return True
        else:
            return False

    def transfer(self, account1, account2, money):
        if self.account_exists(account1) and self.account_exists(account2) and self.withdraw(account1, money):
            return self.deposit(account2, money)
        return False

# Usage
# obj = Bank(balance)
# result = obj.transfer(account1, account2, money)
# result = obj.deposit(account, money)
# result = obj.withdraw(account, money)
