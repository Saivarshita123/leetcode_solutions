class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.n = len(balance)

    def is_valid(self, account):
        # Check if account number is valid (1 to n)
        return 1 <= account <= self.n

    def transfer(self, account1, account2, money):

        if not self.is_valid(account1) or not self.is_valid(account2):
            return False
        if self.balance[account1 - 1] < money:
            return False

        # Perform transfer
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account, money):
        # Validate account
        if not self.is_valid(account):
            return False

        # Perform deposit
        self.balance[account - 1] += money
        return True

    def withdraw(self, account, money):
        # Validate account and sufficient balance
        if not self.is_valid(account):
            return False
        if self.balance[account - 1] < money:
            return False

        # Perform withdrawal
        self.balance[account - 1] -= money
        return True
