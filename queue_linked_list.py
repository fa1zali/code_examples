# Queue using linked list
class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return str(self.data)

class QueueLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def enqueue(self, data):
        node = Node(data)
        if self.tail:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = self.head
        self.size += 1

    def dequeue(self):
        var = self.head
        if self.size == 1:
            self.head = None
            self.tail = None
        elif self.size > 1:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return f"{var} is pooped."

    def iter(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

que = QueueLinkedList()
que.enqueue(8)
que.enqueue(5)
que.enqueue(19)
que.enqueue(1)
print(que.dequeue())
que.iter()