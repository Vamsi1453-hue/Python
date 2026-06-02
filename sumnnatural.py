#write a python program to calculate sum of n natural numbers 
num=int(input("Enter a number: "))
sum=0
for i in range(1,num+1):
    sum+=i
print("The sum of first",num,"natural numbers is:",sum)
