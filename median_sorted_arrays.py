# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Author: Faisal Ali
# Creation Date: 26-Jan-2021
# Version 1.0

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if (len(nums1) >= 0) and (len(nums1) <= 1000) and (len(nums2) >= 0) and (len(nums2) <= 1000):  
            for elm in nums2:
                nums1.append(elm)
            nums1.sort()
            lth = len(nums1)
            if lth % 2 == 0 :
                a = nums1[(lth//2)-1]
                b = nums1[(lth//2)]
                c = (a + b)/2
                return c
            else:
                return nums1[(lth//2)]
        else:
            return 0
obj = Solution()
print(obj.findMedianSortedArrays([2],[]))
                