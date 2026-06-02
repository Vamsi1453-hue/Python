#write a python program to find summation of each digit in the number.
num = int(input("Enter an integer: "))
summation = 0
remainder=0
while (num != 0):
    remainder = num % 10
    summation += remainder
    num = num // 10
print(f"The summation of the digits is: {summation}")
