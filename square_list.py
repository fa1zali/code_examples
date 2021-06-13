# Given a sorted list of integers, square the elements and give the output in sorted order.

# For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].

# Author: Faisal Ali
# Creation Date: 13-June-2021
# Version 1.0

def square_list(lst):
    new_list = []
    for elm in lst:
        new_list.append(elm*elm)
    new_list.sort()
    return new_list
print(square_list([-9, -2, 0, 2, 3]))