import heapq

h=[]

heapq.heappush(h,5)
heapq.heappush(h,2)
heapq.heappush(h,8)
heapq.heappush(h,1)
heapq.heappush(h,6)
heapq.heappush(h,4)

print("Heap array: ",h)
print("Min element: ",h[0])

minimum = heapq.heappop(h)
print("Popped min: ",minimum)
print("After pop: ",h)
print("New min: ",h[0])