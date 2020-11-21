# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Author: Faisal Ali
# Creation Date: 21-Nov-2020
# Version 1.0

class Solution:

    def longestCommonPrefix(self, strs):
        size = len(strs)

        if (size == 0): # If size is 0, return empty string  
            return "" 
    
        if (size == 1): 
            return strs[0] # If size is 1, return 1st element 
          
        strs.sort() # sort the array of strings
          
        end = min(len(strs[0]), len(strs[size - 1])) # find the minimum length from first and last string
    
        # find the common prefix between the first and last string  
        i = 0
        while (i < end and strs[0][i] == strs[size - 1][i]): 
            i += 1
    
        if i == 0:
            return ""
        else:
            pre = strs[0][0: i] 
            return pre 

obj = Solution()
strs = ["flower","flow","flight"]
print(obj.longestCommonPrefix(strs))