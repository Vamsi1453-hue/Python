def table(n, i=1, j=1):
    if i > n:
        return
    print(i * j, end=" ")
    if j < n:
        table(n, i, j+1)
    else:
        print()
        table(n, i+1, 1)
table(5)
