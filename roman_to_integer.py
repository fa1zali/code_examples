# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. 
# The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
# Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
# The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.

# Given a roman numeral, convert it to an integer.

# Input: s = "III"
# Output: 3

# Input: s = "IV"
# Output: 4

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Author: Faisal Ali
# Creation Date: 17-Nov-2020
# Version 1.0

# Brute Force Approach
class Solution:
    def romanToInt(self, s):
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000} # Storing roman symbols with their corresponding integer values
        lst = []
        lth = len(s) # Calculating length of string
        for elm in s:
            lst.append(elm) # Creating a list of roman value input
        sum = 0
        for i in range(lth):
            lst[i] = roman[lst[i]] # Fetching corresponding values and replacing them in list
            sum += lst[i] # Calculating the sum
        for i in range(lth-1):  # For correcting the sum due to exceptional cases
            if (lst[i] == 1 and lst[i+1] == 5):
                sum = sum - 6 + 4
            if (lst[i] == 1 and lst[i+1] == 10):
                sum = sum - 11 + 9
            if (lst[i] == 10 and lst[i+1] == 50):
                sum = sum - 60 + 40
            if (lst[i] == 10 and lst[i+1] == 100):
                sum = sum - 110 + 90
            if (lst[i] == 100 and lst[i+1] == 500):
                sum = sum - 600 + 400
            if (lst[i] == 100 and lst[i+1] == 1000):
                sum = sum - 1100 + 900
        return sum
        
obj = Solution()
s = 'MCMXCIV'
print(obj.romanToInt(s))