
def summation(n):
    if(n==0):
        return 0
    else:
        return n%10+summation(n//10)
print(summation(1234))