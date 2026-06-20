class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        node = Node(data)
        if not self.head: 
            self.head = node
            return
        cur = self.head
        while cur.next: 
            cur = cur.next
        cur.next = node
        
    def insertAtStart(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def insertAtPos(self, data, pos):
        if pos == 0: 
            self.insertAtStart(data)
            return
        node, cur, i = Node(data), self.head, 0
        while cur and i < pos - 1: 
            cur = cur.next
            i += 1
        if cur: 
            node.next = cur.next
            cur.next = node
        
    def delete(self, value):
        if not self.head: 
            return 
        if self.head.data == value:
            self.head = self.head.next
            return 
        cur = self.head
        while cur.next and cur.next.data != value:
            cur = cur.next
        if cur.next: 
            cur.next = cur.next.next
    
    def search(self, key):
        cur = self.head
        while cur:
            if cur.data == key: 
                return True
            cur = cur.next
        return False
    
    def display(self):
        cur, parts = self.head, []
        while cur: 
            parts.append(str(cur.data))
            cur = cur.next
        print(" -> ".join(parts) + " -> None")

ll = SinglyLinkedList()
ll.insertAtEnd(1)
ll.insertAtEnd(2)
ll.insertAtEnd(3)
ll.insertAtStart(0)
ll.insertAtPos(99, 2)
ll.display()