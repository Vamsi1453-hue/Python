n = int(input("Enter a value: "))
k=0
for i in range(1, n+1):        
    for s in range(i-1):
        print("", end=" ")
    for j in range(n-i+1):
        k=k+1
        print(chr(96+k), end=" ")
    print()
