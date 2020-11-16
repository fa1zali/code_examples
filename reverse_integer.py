# Given a 32-bit signed integer, reverse digits of an integer.

# Input: x = 123
# Output: 321

# Input: x = 120
# Output: 21

# Author: Faisal Ali
# Creation Date: 16-Nov-2020
# Version 1.0

# Brute force approach
class Solution1:
    def reverse(self, x):
        y = abs(x)
        rev = 0
        while (y > 0):
            rev *= 10
            rev += y % 10
            y //= 10
        if x < 0:
            return (rev * -1)
        else:
            return rev

# Optimal approach
class Solution2:
    def reverse(self, x):
        x = str(x)
        if x[0] == '-':
            a = int('-' + x[-1:0:-1])
            if a >= -2147483648 and a<= 2147483647:
                return a
            else:
                return 0
        else:
            a = int(x[::-1])
            if a >= -2147483648 and a<= 2147483647:
                return a
            else:
                return 0

obj1 = Solution1()
obj2 = Solution2()
x = 123
print(obj1.reverse(x))
print(obj2.reverse(x))


