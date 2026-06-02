#write a python program to print the multiplication table of five with only even multiples and output should end with even number tables with continue keyword.
num = 5
for i in range(1, 11):
    if (num * i) % 2 == 0:
        print(f"{num} x {i} = {num * i}")
    else:
        continue
    