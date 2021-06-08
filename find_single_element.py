# Given an array of integers in which two elements appear exactly once and 
# all other elements appear exactly twice, find the two elements that appear only once.

# For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.

# Author: Faisal Ali
# Creation Date: 09-June-2021
# Version 1.0

def findSingleElement(arr):
    # defining a dictionary to store the count of occurence of elements and a list to store elements with single occurrence
    count_map = {}
    single_elm = []
    for elm in arr:
        if elm not in count_map:
            count_map.update({elm:1}) # if element does not exist, add the element with its count in dictionary
        else:
            val = count_map[elm] + 1 
            count_map.update({elm:val}) # If element exist then update the occurence value and increment by 1
    
    for key,value in count_map.items(): # Extract the key, value pair
        if value == 1: 
            single_elm.append(key) # Check if occurence count is 1 then add them in the list
    return single_elm

print(findSingleElement([2, 4, 6, 8, 10, 2, 6, 10]))