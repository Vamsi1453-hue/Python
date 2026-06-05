s = int(input("Enter 1.small 2.medium 3.large: "))
print("available toppings 1.cheese 2.pepperoni 3.olives 4.jalapenos")
st = int(input("enter no of toppings you want "))
amt = 0

if s == 1:
    amt = 10
elif s == 2:
    amt = 15
elif s == 3:
    amt = 20
else:
    print("Invalid size")

for i in range(st):
    topping = input("enter topping: ")
    if topping == 'cheese':
        amt = amt + 2
    elif topping == 'pepperoni':
        amt = amt + 3
    elif topping == 'olives':
        amt = amt + 5
    elif topping == 'jalapenos':
        amt = amt + 5
    else:
        print("Unknown topping", topping)

print(amt)