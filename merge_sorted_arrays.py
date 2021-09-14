# Given two array's of sorted integers, merge the two arrays to return a new sorted array. 

# For example, given the array [0,3,4,31] and [4,6,30], return [0,3,4,4,6,30,31].

# Author: Faisal Ali
# Creation Date: 14-Sep-2021
# Version 1.0

def merge_sorted_arrays(arr1, arr2):
    
    i = 0
    j = 0
    l1 = len(arr1)
    l2 = len(arr2)
    arr3 = []

    # Checking if any empty array is given as input
    if l1 == 0:
        return arr2
    if l2 == 0:
        return arr1
    
    while ((i < l1) and (j < l2)):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i = i + 1
        else:
            arr3.append(arr2[j])
            j =j + 1
    
    while (i < l1):
        arr3.append(arr1[i])
        i = i + 1   

    while (j < l2):
        arr3.append(arr2[j])
        j = j + 1   
    
    return arr3
    
print(merge_sorted_arrays([0,3,4,31], [4,6,30]))