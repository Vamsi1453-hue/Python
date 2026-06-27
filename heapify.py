import heapq

class MaxHeap:
    def __init__(self):
        self.h=[]
    def push(self,val):
        heapq.heappush(self.h,-val)
    def pop(self):
        return -heapq.heappop(self.h)
    def peek(self):
        return self.h[0]
    
mh=MaxHeap()
for v in [5,2,8,1,9,3]:
    mh.push(v)
    
print("Max (root):",mh.peek())
print("Pop max: ",mh.pop())
print("New max: ",mh.peek())
nums = [3,1,4,1,5,9,2,6,5,3]
heapq.heapify(nums)

print("Heapified List:", nums)
print("Root (min): ",nums[0])

result=[]
while nums:
    result.append(heapq.heappop(nums))
print("Sorted output:",result)