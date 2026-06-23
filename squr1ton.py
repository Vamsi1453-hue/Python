#print square values from 1 to n using no loops
def squares(n, i=1):
    if i > n:
        return
    print(i * i)
    squares(n, i+1)

squares(5)
