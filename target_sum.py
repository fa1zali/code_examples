# Given an array of integers and a target integer value.
# Find whether any 2 elements when added is equal to the target integer value. 

# For example, given the array [1,2,4,4] and target is 8, return True as 4 + 4 is 8.
# given the array [1,2,3,4] and target is 8, return False as sum of any 2 elements is not equal to 8.

# Author: Faisal Ali
# Creation Date: 14-Sep-2021
# Version 1.0

# Brute Force Approach

def target_sum(arr, target):
    
    l1 = len(arr)
    for i in range(l1):
        for j in range(l1):
            if i != j:
                if arr[i] + arr[j] == target:
                    return True
    return False

print(target_sum(arr = [1,3,2,4], target = 8))
print(target_sum(arr = [1,3,4,4], target = 8))

# Optimal Approach

def target_sum2(arr, target):

    seen = []
    for elm in arr:
        rem = target - elm
        if rem in seen:
            if ((rem * 2) == target):
                return True
        else:
            seen.append(rem)
    return False

print(target_sum2(arr = [1,3,3,4], target = 8))
print(target_sum2(arr = [1,3,4,4], target = 8))