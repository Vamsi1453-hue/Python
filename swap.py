# Swap first and last digit of a 3-digit number
num = int(input("Enter a three-digit number: "))
first = num // 100
middle = (num // 10) % 10
last = num % 10
swapped = last * 100 + middle * 10 + first
print("Swapped number:", swapped)
