# Implement a bit array.

# A bit array is a space efficient array that holds a value of 1 or 0 at each index.

# init(size): initialize the array with size
# set(i, val): updates index at i with val where val is either 1 or 0.
# get(i): gets the value at index i.
# Index is considered to be starting from 1 for user and in Python list index starts from 0

# Author: Faisal Ali
# Creation Date: 04-June-2021
# Version 1.0

class bitArray():

    def __init__(self):
        """Initialize an empty array"""
        self.bitt_arr = []

    def initialize(self, size):
        """Sets the size of array and fills it with a character"""
        self.size = size
        self.bitt_arr = ['*' for i in range(self.size)]
    
    def set(self, i, val):
        """Takes index value and value to be filled as argument and place in the array if they are valid"""
        self.i = i
        self.val = val
        if self.size == 0 or self.size == None:
            return "Invalid Size"
        else:
            if ((self.val == 0) or (self.val == 1)):
                if ((self.i > 0) and (self.i <= self.size)):
                    self.i -= 1
                    self.bitt_arr[self.i] = self.val
                    return self.bitt_arr
                return "Invalid Index Position"
            return "Invalid value"
    
    def get(self, i):
        "Return the value at index position passed as an argument"
        if ((self.i > 0) and (self.i <= self.size)):
            self.i = i-1
            if self.bitt_arr[self.i] != '*':
                return self.bitt_arr[self.i]
            return "Value not filled"
        return "Invalid Index"

obj = bitArray()
obj.initialize(5)
print(obj.set(2,1))
print(obj.get(2))
print(obj.set(1,0))
print(obj.set(-1,0))
print(obj.set(4,10))
print(obj.set(3,1))
print(obj.set(5,1))
print(obj.set(4,0))
