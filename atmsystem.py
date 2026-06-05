# create an ATM system that validates a PIN before allowing transactions.
# The system supports deposit, withdrawal, and balance inquiry.

pin = int(input("Enter your pin number: "))
acc_bal = 0

if pin == 1234:
    print("Welcome to the bank")
    while True:
        print("\n1. Deposit")
        print("2. Withdrawal")
        print("3. Balance Inquiry")
        print("4. Exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
            amount = int(input("Enter the amount to deposit: "))
            if amount > 0:
                acc_bal += amount
                print(f"Dear customer, your account xxxxxxxxx1234 is credited with {amount}.")
            else:
                print("Please enter a positive amount.")

        elif choice == 2:
            amount = int(input("Enter the amount to withdraw: "))
            if amount <= 0:
                print("Please enter a positive amount.")
            elif amount <= acc_bal:
                acc_bal -= amount
                print(f"Dear customer, your account xxxxxxxxx1234 is debited with {amount}.")
            else:
                print("Insufficient balance.")

        elif choice == 3:
            print(f"Dear customer, your account xxxxxxxxx1234 has {acc_bal}.")

        elif choice == 4:
            print("Thank you for choosing our bank.")
            break

        else:
            print("Invalid option. Please choose 1-4.")
else:
    print("You entered the wrong PIN.")
    