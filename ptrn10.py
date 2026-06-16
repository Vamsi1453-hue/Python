n = int(input("Enter the value: "))
count = 5
ch = ord('a')
for i in range(1, n+1):
    if i % 2 != 0:
        print((chr(ch) + " ") * count)
        ch += 2
    else:
        print("* " * count)
    count += 1
