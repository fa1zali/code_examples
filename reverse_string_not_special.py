# Given a string containing alphabets and special characters.
# Reverse the string such that it does not effects the position of special characters
# You can assume no character will be repeated.

# Input: "a,b$c"
# Output: "c,b$a"
# Input: "Ab,c*de!$"
# Output: "ed,c*bA!$"

# Author: Faisal Ali
# Creation Date: 21-Jan-2021
# Version 1.0

class Solution:
    def reverseString(self, text):
        lstInitial = list(text)
        lstFinal = []
        rvrsInitial = {} 
        rvrsFinal = {}
        rr = ""
        for i in range(len(lstInitial)):
            rvrsInitial[lstInitial[i]] = i
        
        for key,value in rvrsInitial.items():
            if key.isalpha():
                lstFinal.append(key)
            else:
                rvrsFinal[key] = value
        lstFinal.reverse()
        for i in range(len(lstInitial)):
            for key,value in rvrsFinal.items():
                if value == i:
                    lstFinal.insert(value,key)
        return rr.join(lstFinal)


obj = Solution()
print(obj.reverseString("Ab,c*de!$"))