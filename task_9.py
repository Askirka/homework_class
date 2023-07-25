class BankAccount:
    def __init__(self, balance=0, interest_rate=0.01):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

    def is_negative(self):
        return self.balance < 0


account1 = BankAccount(balance=1000, interest_rate=0.05)
account2 = BankAccount(balance=500, interest_rate=0.03)

print(f"Начальный баланс аккаунта 1: {account1.balance}")
account1.deposit(500)
account1.withdraw(200)
account1.add_interest()
print(f"Баланс аккаунта 1 после всех операций: {account1.balance}")
print(f"Баланс аккаунта 1 отрицательный: {account1.is_negative()}")

print(f"Начальный баланс аккаунта 2: {account2.balance}")
account2.add_interest()
print(f"Баланс аккаунта 2 после начисления процентов: {account2.balance}")
print(f"Баланс аккаунта 2 отрицательный: {account2.is_negative()}")
