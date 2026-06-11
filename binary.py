def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        
        if arr[mid]==target: return mid
        elif arr[mid]< target: left=mid+1
        else:                  right=mid-1
    
    return -1
arr=[2,3,4,14,22,34,56,67]
target=22
if target in arr:
    print(target)
else:
    print('-1')

