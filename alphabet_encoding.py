# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.

# Author: Faisal Ali
# Creation Date: 24-Jan-2021
# Version 1.0

class Solution:
    def num_ways(self, data):
        k = len(data)
        return self.helper(data, k)

    def helper(self, data, k):
        lst = list(data)
        if k == 0:
            return 1
        elif lst[0] == '0':
            return 0
        
        result = self.helper(data, k-1)
        a = ''
        for elm in lst[0:2]:
            a = a + elm
        if (k >= 2) and (int(a) <= 26):
            result += self.helper(data, k-2)
        return result
        
obj = Solution()
print(obj.num_ways("1"))
