# Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:

# next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
# has_next(): returns whether or not the iterator still has elements left.
# For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

class iterator:

    count = 0

    def __init__(self, inp):

        self.lst = []    
        for elm in inp:
            for inn_elm in elm:
                self.lst.append(inn_elm)

    def next(self):
        iterator.count += 1
        
        if iterator.count <= len(self.lst): 
            return self.lst[iterator.count-1]
        else:
            return "No element exists"

    def has_next(self):
        
        try:
            a = self.lst[iterator.count]
            return "Element Exists"
        except:
            return "No element exists"


obj = iterator(inp = [[1, 2], [3], [], [4, 5, 6]])
print(obj.lst)
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.has_next())