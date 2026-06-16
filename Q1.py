class BankAccount:
    def __init__(self):
        self.__balance = 10000   # private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}, New Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient!")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}, New Balance: {self.__balance}")

    def get_balance(self):
        print(f"Current Balance: {self.__balance}")



acc1 = BankAccount()
acc2 = BankAccount()


print("Account 1:")
acc1.deposit(2000)
acc1.withdraw(5000)
acc1.get_balance()

print("\nAccount 2:")

acc2.deposit(500)
acc2.withdraw(11000)
acc2.get_balance()