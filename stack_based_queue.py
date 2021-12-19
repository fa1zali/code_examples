# Stack based queue (Using 2 stacks)

class StackQueue:

    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []
    
    def enqueue(self, data):
        self.inbound_stack.append(data)
    
    def dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        return self.outbound_stack.pop()

que = StackQueue()
que.enqueue(8)
que.enqueue(5)
que.enqueue(19)
que.enqueue(1)
print(que.inbound_stack)
que.dequeue()
que.dequeue()
print(que.outbound_stack)