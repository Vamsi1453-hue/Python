import math

def jump_search(arr,target):
    n=len(arr)
    step=int(math.sqrt(n)) # jump block size
    prev=0
    # jump forward until block may contain target
    while arr[min(step, n) - 1] < target:
        prev = step
        step+= int(math.sqrt(n))
        if prev>= n : return -1
    #linear scan in the identified block
    while arr[prev] < target:
        prev+=1
        if prev ==min(step,n): return -1
    if arr[prev]== target: return prev

    return -1