s = input("enter a value: ")
for i in range(1, len(s)+1):
    print(" ".join(s[:i]))
print()  
for i in range(len(s)):
    print((s[i] + " ") * (i+1))
