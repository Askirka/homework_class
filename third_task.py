class BankAccount:
    def __init__(self,balance,interest_rate):

        self.balance = balance
        self.interest_rate = interest_rate


    def deposit(self):

        if self.balance == int or float :
            print(f"Your balancee now {self.balance} and your rate {self.interest_rate}")



    def withdraw(self,minus_balance):
        minus_balance = self.balance - minus_balance
        print(f"Your balance now {minus_balance}")

    def add_interest(self,add_sum):
        self.add_sum = add_sum

        new_balance = self.balance + (self.balance/100*add_sum)
        print(new_balance)








man1 = BankAccount(1041,1)

print(man1.deposit())
print(man1.withdraw(500))

print(man1.add_interest(1))




