#write a python program to check whether the user entered a integer is a prime number or not
num=int(input("Enter an integer: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
