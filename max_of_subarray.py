# Given an array of integers and a number k, where 1 <= k <= length of the array, 
# compute the maximum values of each subarray of length k.

# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. 
# You can simply print them out as you compute them.

# Author: Faisal Ali
# Creation Date: 06-Feb-2021
# Version 1.0

class Solution:
    def maxsubarray(self, arr, k):
        print(max(arr[:k]))
        if len(arr) > k:
            del arr[0]
            return self.maxsubarray(arr, k)

obj = Solution()
obj.maxsubarray(arr = [10, 5, 2, 7, 8, 7], k = 3)