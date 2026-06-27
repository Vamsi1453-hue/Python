import heapq

class MaxHeap:
    def __init__(self):
        self.h = []
    def push(self, val):
        heapq.heappush(self.h, -val)
    def pop(self):
        return -heapq.heappop(self.h)
    def peek(self):
        return -self.h[0]   # fixed here

mh = MaxHeap()
for v in [5, 2, 8, 1, 9, 3]:
    mh.push(v)

print("Max (root):", mh.peek())
print("Pop max:", mh.pop())
print("New max:", mh.peek())

def top_k_scores(scores, k):
    heap = []
    for score in scores:
        heapq.heappush(heap, score)
        if len(heap) > k:
            heapq.heappop(heap)
    return sorted(heap, reverse=True)

scores = [84, 92, 78, 95, 88, 73, 99, 61, 70, 85]
print("All scores:", scores)
print("Top 3:", top_k_scores(scores, 3))
print("Top 5:", top_k_scores(scores, 5))

print("\nLargest(3):", heapq.nlargest(3, scores))
print("Smallest(3):", heapq.nsmallest(3, scores))
