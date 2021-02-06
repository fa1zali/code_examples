# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

# In this example, assume nodes with the same value are the exact same node objects.

# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

# Author: Faisal Ali
# Creation Date: 06-Feb-2021
# Version 1.0

class Solution:
    def list_intersection(self, A, B):
        for elm in A:
            if elm in B:
                return elm

obj = Solution()
print(obj.list_intersection(A = [3, 7, 8, 10], B = [99, 1, 8, 10]))