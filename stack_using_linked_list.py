# Implementation of Stack using linked list

class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = None
        self.prev = None
    
    def __repr__(self):
        return str(self.data)

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.tail:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = self.head
        self.size += 1

    def pop(self):
        top = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1
        return f"{top.data} is popped."

    def iter(self):
        current = self.tail
        while current:
            print(current.data)
            current = current.prev
    
    def peek(self):
        current = self.tail
        return current.data

a = Stack()
print("Adding elemnets")
a.push(1)
a.push(5)
a.push(4)
a.push(8)
print(f"Length of stack: {a.size}")
print(f"Top element is: {a.peek()}")
a.iter()
print(a.pop())
print(f"Length of stack: {a.size}")
print(f"Top element is: {a.peek()}")
a.iter()