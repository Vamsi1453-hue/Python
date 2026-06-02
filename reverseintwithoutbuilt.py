# write a python program to print the reversed integer of user entered number without using builtin functions
num = int(input("Enter an integer: "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10