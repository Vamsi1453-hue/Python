#print revrsed multipliocation tables of n using recursion no loops
def rev_table(n, i=None, j=None):
    if i is None and j is None:
        i, j = n, n
    if i < 1:
        return
    print(i * j, end=" ")
    if j > 1:
        rev_table(n, i, j-1)
    else:
        print()
        rev_table(n, i-1, n)

rev_table(5)
