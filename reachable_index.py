# Given an integer list where each number represents the number of hops you can make, 
# determine whether you can reach to the last index starting at index 0.

# For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.

# Author: Faisal Ali
# Creation Date: 19-June-2021
# Version 1.0

def reachable(arr):
    length = len(arr)
    req_hop = length - 1
    sum = 0 
    if arr[0] == 0:
        return False
    for i in range(length - 1):
        if ((arr[i] > i+1) or (sum < i + 1)):
            sum += arr[i]
    if req_hop == sum:
        return True
    return False

print(reachable(arr = [2,0,1,0])) #True
print(reachable(arr = [1,1,0,1])) #False
print(reachable(arr = [1,1,1,0])) #True
print(reachable(arr = [0,1,1,1])) #False
print(reachable(arr = [1,0,1,0])) #False