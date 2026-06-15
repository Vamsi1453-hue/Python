class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def isfull(self):
        return (self.rear + 1) % self.size == self.front

    def isempty(self):
        return self.front == -1

    def enqueue(self, value):
        if self.isfull():
            return "Queue Over Flow"
        if self.isempty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value   
        print(f"Enqueued {value} at index {self.rear}")

    def dequeue(self):
        if self.isempty():
            return "Queue Under Flow"
        val = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return val

    def display(self):
        if self.isempty():
            print("Empty")
            return
        i, elms = self.front, []
        while True:
            elms.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print("CQ:", elms)

V = CircularQueue(3)
V.enqueue(10)
V.enqueue(20)
V.dequeue()
V.display()
print(V.enqueue(10))
print(V.enqueue(20))
print(V.isempty())
print(V.isfull())
print(V.dequeue())
print(V.display())
