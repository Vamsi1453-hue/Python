def num(n,i):
    if (i<=n):
        print(i)
        return num(n,i+1)
num(5,1)