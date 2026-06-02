x=10
y=3
print(f"Addition of x & y is {x+y}")
print(f"Subtraction of x & y is {x-y}")
print(f"Multiplication of x & y is {x*y}")  
print(f"Division of x & y is {x/y}")
print(f"Positive Floor division of x & y is {x//y}")
print(f"Negative Floor division of x & y is {-x//y}")
print(f"Modulus of x & y is {x%y}")
print(f"Exponentiation of x & y is {x**y}")
#relational operators
print(10>15)
print(10<15)
print(10>=10)
print(10<=10)
print(10==10)
print(10!=15)
#assignment operators
num=10
print(f"num = {num}")
num+=2
print(f"num = {num}")
num-=2
print(f"num = {num}")
num*=2
print(f"num = {num}")
num/=2
print(f"num = {num}")
num//=2
print(f"num = {num}")
num%=2
print(f"num = {num}")
num**=2
print(f"num = {num}")

#logical operators
num=10
print(num>5 and num<15)
print(num>5 or num<5)
print(not(num<15))
#bitwise operators
a=10
b=15
print(a&b)
print(a|b)
print('~a=',~a)
print('a&b=',a&b)
print('a|b=',a|b)
print('a^b=',a^b)
print('a>>1=',a>>1)
print('a<<1=',a<<1)
#membership operators
List=[10,35,25,40,15,20]
print(10 in List)
print(50 in List)
print(10 not in List)
print(50 not in List)
print("Python" in "I am working on Python")
print("Python" in "I am working on Python")
#identity operators
num1=10
print(num1)
print(id(num1))
num2=10
print(num2)
print(id(num2))
print(num1 is num2)
num3=20
print(num3)
print(id(num3))
print(num1 is num3)