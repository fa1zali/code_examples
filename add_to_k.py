# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Author: Faisal Ali
# Creation Date: 19-Jan-2021
# Version 1.0

# Brute force approach
class Solution1:
    def addtok(self,arr,k):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j:
                    if arr[i] + arr[j] == k:
                        return True
        return False

# Optimal Approach
class Solution2:
    def addtok(self,arr,k):
        seen = []
        for i in range(len(arr)):
            diff = k - arr[i]
            if diff in arr:
                seen.append(diff)
        if len(seen) == 2:
            return True
        else:
            return False


arr = [10, 15, 3, 7]
k = 25
obj1 = Solution1()
obj2 = Solution2()
print(obj1.addtok(arr, k))
print(obj2.addtok(arr, k))