#even numbers from 1 to n using no loops
def evens(n, i=2):
    if i > n:
        return
    print(i)
    evens(n, i+2)

evens(10)
