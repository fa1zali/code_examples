# Implement a stack that has the following methods:

# push(val), which pushes an element onto the stack
# pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, 
# then it should throw an error or return null.
# max(), which returns the maximum value in the stack currently. If there are no elements in the stack, 
# then it should throw an error or return null.
# Each method should run in constant time.

# Author: Faisal Ali
# Creation Date: 21-June-2021
# Version 1.0

class Stack:

    def __init__(self):
        self.stack_list = []

    def push(self, val):
        self.val = val
        self.stack_list.append(self.val)

    def lth(self):
        return len(self.stack_list)

    def pop(self):
        if self.lth() == 0:
            return None
        else:
            self.val = self.stack_list[-1]
            del self.stack_list[-1]
            return f"{self.val} is removed"

    def max(self):
        if self.lth() == 0:
            return None
        else:
            return max(self.stack_list)

obj = Stack()
obj.push(1)
obj.push(10)
obj.push(3)
obj.push(15)
obj.push(29)
print(obj.pop())
print(obj.pop())
print(obj.max())