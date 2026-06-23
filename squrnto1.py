#print square values from n to 1 using no loops 
def squares(n):
    if n < 1:
        return
    print(n * n)
    squares(n-1)

squares(5)
