#odd numbers from 1 to n using no loops
def odds(n, i=1):
    if i > n:
        return
    print(i)
    odds(n, i+2)

odds(10)
