# Given an array of integers, return a new array such that each element at index i of the new array 
# is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Author: Faisal Ali
# Creation Date: 19-Jan-2021
# Version 1.0

# Brute force approach
class Solution:
    def arrayProduct(self, arr):
        lst = []
        mlt = 1
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j :
                    mlt *= arr[j]
            lst.append(mlt)
            mlt = 1
        return lst

obj = Solution()
arr = [1, 2, 3, 4, 5]
print(obj.arrayProduct(arr))