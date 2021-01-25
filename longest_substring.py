# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Author: Faisal Ali
# Creation Date: 25-Jan-2021
# Version 1.0

class Solution:
    subs = []
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        if s != "":
            for elm in s:
                if elm in seen:
                    break
                else:
                    seen.append(elm)
            Solution.subs.append(len(seen))
            initialList = list(s)
            del initialList[0]
            r = ''
            newString = r.join(initialList)
            self.lengthOfLongestSubstring(newString)
            return max(Solution.subs)
        else:
            return 0
        
obj = Solution()
print(obj.lengthOfLongestSubstring("pwwkew"))