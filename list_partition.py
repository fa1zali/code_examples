# Given a pivot x, and a list lst, partition the list into three parts.

# The first part contains all elements in lst that are less than x
# The second part contains all elements in lst that are equal to x
# The third part contains all elements in lst that are larger than x
# Ordering within a part can be arbitrary.

# For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].
# Author: Faisal Ali
# Creation Date: 13-June-2021
# Version 1.0

def partition(x, lst):
    p1 = []
    p2 = []
    p3 = []

    for elm in lst:
        if elm < x:
            p1.append(elm)
        elif elm == x:
            p2.append(elm)
        else:
            p3.append(elm)
    
    return p1 + p2 + p3

print(partition(x = 10, lst = [9, 12, 3, 5, 14, 10, 10]))