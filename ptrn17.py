n = int(input("Enter a number: "))
count, num = 0, 2
while count < n:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
        count += 1
    num += 1
