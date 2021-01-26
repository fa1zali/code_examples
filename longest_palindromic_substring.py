# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"

# Author: Faisal Ali
# Creation Date: 26-Jan-2021
# Version 1.0

class Solution():
    sub = []
    def longestPalinsub(self, s):
        seen = []
        initialList = list(s)
        for elm in initialList:
            if elm in seen:
                seen.append(elm)
                break
            else:
                seen.append(elm)
        a = "".join(seen)
        Solution.sub.append(a)
        if len(initialList) > 0:
            del initialList[0]
            b = "".join(initialList)
            return self.longestPalinsub(b)
        
        new = ''
        for elm in Solution.sub:
            for letter in reversed(elm):
                new = new + letter
            if elm == new:
                Solution.sub = []
                return new
            else:
                new = ''

obj = Solution()
print(obj.longestPalinsub("babad"))