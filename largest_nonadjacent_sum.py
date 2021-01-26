# Given a list of integers, write a function that returns 
# the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
# 
#  [5, 1, 1, 5] should return 10, since we pick 5 and 5.

class Solution:
    def nonadjsum(self, arr):
        incl = 0
        excl = 0
        for elm in arr:
            new_excl = max(incl,excl)
            incl = excl + elm
            excl = new_excl
        return max(incl,excl)

obj = Solution()
print(obj.nonadjsum([5, 5, 10, 40, 50, 35]))