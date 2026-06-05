#seperate even and odd numbers from a given list. display both lists and their counts.
nums=[]
n=int(input("Enter the number of elements in list:"))
for i in range(n):
    x=int(input("Enter element: "))
    nums.append(x)
print("list is the list", nums)
even=[]
odd=[]
for i in nums:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(f"even numbers are {even}")
print(len(even))
print(f"odd numbers are {odd}")
print(len(odd))