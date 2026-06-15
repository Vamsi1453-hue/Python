n=int(input("Enter a character:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(i+64),end=" ")
        print(chr(i+96),end=" ")
    print()
print()