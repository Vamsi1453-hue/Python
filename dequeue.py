from collections import deque

class Deque:
    def __init__(self):
        self.dq = deque()
    def addFront(self, value):
        self.dq.appendleft(value)
        print(f"AddFront {value} -> {list(self.dq)}")
    def addRear(self, value):
        self.dq.append(value)
        print(f"AddRear {value} -> {list(self.dq)}")
    def removeFront(self):
        if self.isEmpty():
            return "Empty!"
        val = self.dq.popleft()
        print(f"RemFront {val} -> {list(self.dq)}")
        return val
    def removeRear(self):
        if self.isEmpty():
            return "Empty!"
        val = self.dq.pop()
        print(f"RemRear {val} -> {list(self.dq)}")
        return val
    def peekFront(self):
        return self.dq[0] if not self.isEmpty() else "Empty"
    def peekRear(self):
        return self.dq[-1] if not self.isEmpty() else "Empty"
    def isEmpty(self):
        return len(self.dq) == 0
v = Deque()
v.addFront(23)
v.addFront(26)
v.addFront(32)
v.addRear(21)
v.addRear(24)
v.addRear(20)
v.removeFront()
v.removeRear()
print("Front:", v.peekFront())
print("Rear :", v.peekRear())
print("Empty:", v.isEmpty())