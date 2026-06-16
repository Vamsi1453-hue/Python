n = 5  
letters = ["A", "C", "E"]  
for idx, ch in enumerate(letters):
    print((ch + " ") * n)
    if idx != len(letters) - 1:
        print("* " * n)
