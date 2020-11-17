# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Input: x = 121
# Output: true

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Author: Faisal Ali
# Creation Date: 16-Nov-2020
# Version 1.1

# Brute Force Approach
class Solution1:
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            rev = 0
            a = x
            while(x > 0):
                rev *= 10
                rev += (x % 10)
                x //= 10
            if rev == a:
                return True
            else:
                return False

# Optimal Approach
class Solution2:
    def isPalindrome(self, x):
        a = str(x)
        rev = ""
        if a[0] == "-":
            return False
        else:
            for elm in reversed(a):
                rev = rev + elm
            b = int(rev)
            if b == x:
                return True
            else:
                return False


obj1 = Solution1()
obj2 = Solution2()
x = 121
print(obj1.isPalindrome(x))
print(obj2.isPalindrome(x))