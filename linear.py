arr=[13,43,54,32,45,34,36]
target=43
print("Enter the target: ")
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return [i]
        return -1
print(target)
#example
arr=[12,3,45,34,7,43]
target=45
idx=linear_search(arr,target)
print(f"Found at index {idx}")
