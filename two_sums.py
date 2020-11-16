# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Author: Faisal Ali
# Creation Date: 16-Nov-2020
# Version 1.0

# Brute force approach
class Solution1:
    def twoSum(self, nums, target):
        list1 = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    sum = nums[i] + nums [j]
                    if sum == target:
                        list1 = [i,j]
                        return list1

# Optimal Approach
class Solution2:
    def twoSum(self, nums, target):
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []

a = Solution1()
b = Solution2()
nums = [2,7,11,15]
target = 9
print(a.twoSum(nums, target))
print(b.twoSum(nums, target))
