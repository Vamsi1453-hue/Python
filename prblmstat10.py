class User:
    def __init__(self, user_name):
        self.user_name = user_name


class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def transfer_money(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def show_balance(self):
        return self.balance


class Transaction:
    def generate_receipt(self, user, wallet, transfer_amount, opening_balance):
        print("=" * 50)
        print("          TRANSACTION RECEIPT")
        print("=" * 50)

        print(f"\nUser Name       : {user.user_name}")
        print(f"\nOpening Balance : ₹{opening_balance}")
        print(f"\nTransfer Amount : ₹{transfer_amount}")
        print(f"\nCurrent Balance : ₹{wallet.show_balance()}")

        print("\nStatus          : SUCCESSFUL")

        print("\n" + "=" * 50)


user = User("Noah")

wallet = Wallet(10000)
opening_balance = wallet.balance

wallet.transfer_money(2500)

transaction = Transaction()
transaction.generate_receipt(
    user,
    wallet,
    2500,
    opening_balance
)