#write a function total(*numbers) that takes a variable number of arguments and returns the sum of all the numbers. You can use the *args syntax to allow for a variable number of arguments in the function definition.
def total(*numbers):
    print(sum(numbers))
total(1, 2, 3, 4, 5)
