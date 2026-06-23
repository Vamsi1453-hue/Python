def fact(n):
    if(n==1):
        return 1
    return fact(n-1)*n
print(fact(5))

#2nd logic
def x(n):
    if(n==1):
        return 1
    return x(n-1)*n
print(x(5))