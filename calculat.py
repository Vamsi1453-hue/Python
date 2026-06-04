def add(a,b):
    print(f"Addition of {a} and {b} is: {a + b}")
    print('='*30)
def subtract(a,b):
    print(f"Subtraction of {a} and {b} is: {a - b}")
    print('='*30)
def multiply(a,b):
    print(f"Multiplication of {a} and {b} is: {a * b}")
    print('='*30)
def divide(a,b):
        print(f"Division of {a} and {b} is: {a / b}")
        print('='*30)
def remainder(a,b):
        print(f"Remainder of {a} and {b} is: {a % b}")
        print('='*30)

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Remainder")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 6:
        break
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    if choice == 1:
        add(a,b)
    elif choice == 2:
        subtract(a,b)
    elif choice == 3:
        multiply(a,b)
    elif choice == 4:
         divide(a,b)
    elif choice == 5:
        remainder(a,b)
