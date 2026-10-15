class Bank:
    def __init__(self, opening_balance=0):
        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative.")
        self.__balance = opening_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"Deposited ₹{amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Withdrawal refused: insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount:.2f}")

    def get_balance(self):
        return self.__balance


if __name__ == "__main__":
    account = Bank(1000)
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(5000)
    print(f"Balance: ₹{account.get_balance():.2f}")
