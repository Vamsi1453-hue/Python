n = int(input("Enter a number: "))
for i in range(n):
    ch = chr(65+i)
    print(f"{ch} --> {ord(ch)}")
