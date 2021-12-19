# Implementation of a queue using Python's list

class ListQueue:
    def __init__(self):
        self.item = []
        self.size = 0
    
    def enqueue(self, data):
        self.item.append(data)
        self.size += 1
    
    def dequeue(self):
        if self.size > 0:
            var = self.item[0]
            del self.item[0]
            self.size -= 1
            return f"{var} popped out."
        else:
            return "Empty Queue"
    
    def iter(self):
        for elm in self.item:
            yield elm

queue = ListQueue()
queue.enqueue(8)
queue.enqueue(1)
print(f"The size is: {queue.size}")
queue.enqueue(5)
queue.enqueue(19)
print(f"The size is: {queue.size}")
queue.dequeue()
print(f"The size is: {queue.size}")
for items in queue.iter():
    print(items)