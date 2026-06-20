import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.counter = 0

    def insert(self, item, priority):
        heapq.heappush(self.heap, (priority, self.counter, item))
        self.counter += 1
        print(f"Inserted '{item}' with priority {priority}")

    def extractMin(self):
        if not self.isEmpty():
            priority, _, item = heapq.heappop(self.heap)
            print(f"Extracted '{item}' (priority {priority})")
            return item
        return "Empty"

    def peek(self):
        return self.heap[0][2] if not self.isEmpty() else "Empty"

    def isEmpty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)


pq = PriorityQueue()

pq.insert("low task", 3)
pq.insert("high task", 1)
pq.insert("med task", 2)

print("Peek:", pq.peek())

pq.extractMin()
pq.extractMin()

print("Size:", pq.size())