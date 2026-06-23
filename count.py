
def summation(n):
    count=0
    if(n==0):
        return 0
    else:
        n=n//10
        count+=1
        return count+summation(n)
print(summation(1234))

#2nd logic
def summation(n):
    if(n==0):
        return 0
    else:
        return 1+summation(n//10)
print(summation(1234))