# Given a list of numbers L, implement a method sum(i, j) 
# which returns the sum from the sublist L[i:j] (including i, excluding j).

# For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.

# Author: Faisal Ali
# Creation Date: 18-June-2021
# Version 1.0

class SumOfSublist:
    def __init__(self, L):
        self.L = L

    def sum(self, i, j):
        if (i < 0) :
            raise ValueError("Invalid range entered")
        self.i = i
        self.j = j
        self.new_list = self.L[self.i:self.j]
        total = 0
        for elm in self.new_list:
            total += elm
        return total

obj = SumOfSublist(L = [1, 2, 3, 4, 5])
print(obj.sum(i = 1, j = 3))