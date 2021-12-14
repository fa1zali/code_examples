# Implementation of Stack using python list

class Stack:
    def __init__(self):
        self.stack_list = []
        self.size = 0

    def push(self, data):
        self.stack_list.append(data)
        self.size += 1

    def pop(self):
        val = self.stack_list[-1]
        del self.stack_list[-1]
        self.size -= 1
        return f"{val} is popped."
    
    def peek(self):
        if len(self.stack_list) != 0:
            return self.stack_list[-1]
        else:
            return "Empty Stack"
    
    def iter(self):
        for i in range((len(self.stack_list)-1), -1, -1):
            print(self.stack_list[i])

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