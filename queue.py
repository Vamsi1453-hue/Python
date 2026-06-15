class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def display(self):
        return self.queue
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Removed:", self.queue.pop(0))
    def peekfront(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Front:", self.queue[0])
    def peekrear(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Rear:", self.queue[-1])
    def isempty(self):
        print(len(self.queue) == 0)
    def clear(self):
        self.queue.clear()
        print("Queue cleared")
queue = Queue()
queue.enqueue(12)
queue.enqueue(25)
queue.display()
queue.peekfront()
queue.peekrear()
queue.dequeue()
queue.isempty()
queue.clear()