age=int(input("what is your age? "))
if(age>=18):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#ternary operator
res="Eligible to vote" if age>=18 else "Not eligible to vote"
print(res)

#read two integer numbers and find the largest number using ternary operator
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
largest=num1 if num1>num2 else num2
print(f"The largest number is: {largest}")
