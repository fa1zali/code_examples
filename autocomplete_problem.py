# Implement an autocomplete system. That is, given a query string s 
# and a set of all possible query strings, return all strings in the set that have s as a prefix.

# For example, given the query string de and 
# the set of strings [dog, deer, deal], return [deer, deal].

# Author: Faisal Ali
# Creation Date: 28-Jan-2021
# Version 1.0

class Solution:
    def autocomplete(self, query, arr):
        query_list = list(query)
        querylength = len(query_list)
        auto_list = []
        for elm in arr:
            elm_list = list(elm)
            new_elm_list = elm_list[:querylength]
            new_elm = "".join(new_elm_list)
            if query == new_elm:
                auto_list.append(elm)
        return auto_list

obj = Solution()
print(obj.autocomplete("de", ["dog", "deer", "deal"]))