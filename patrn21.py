n = int(input("Enter the value: "))
num = 2
for i in range(1, n+1):
    for j in range(1, n+1):
        k = (j * 2) * (j * 2)   
        print(f"{k}", end=" ")
    print()
