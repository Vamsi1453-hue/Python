pizza_size = int(input("Enter the size of pizza: "))
Toppings = int(input("Enter the no of toppings: "))
topping1 = input("Enter first topping: ")
topping2 = input("Enter second topping: ")

prize = 0
final_prize = 0

while True:
    print("1.SMALL")
    print("2.MEDIUM")
    print("3.LARGE")
    print("4.Cheese")
    print("5.Pepperoni")
    print("6.Olives")
    print("7.Jalapenos")
    print("8.Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Price is 12$")
        prize += 12

    elif choice == 2:
        print("Price is 15$")
        prize += 15

    elif choice == 3:
        print("Price is 20$")
        prize += 20

    elif choice == 4:
        print("Topping is Cheese with price 2$")
        prize += 2

    elif choice == 5:
        print("Topping is Pepperoni with price 3$")
        prize += 3

    elif choice == 6:
        print("Topping is Olives with price 5$")
        prize += 5

    elif choice == 7:
        print("Topping is Jalapenos with price 5$")
        prize += 5

    elif choice == 8:
        final_prize = prize
        print("Final Price =", final_prize, "$")
        break

    else:
        print("Invalid Choice")