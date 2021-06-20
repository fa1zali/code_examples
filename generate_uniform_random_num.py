# Given an integer n and a list of integers l, write a function 
# that randomly generates a number from 0 to n-1 that isn't in l (uniform).

# Author: Faisal Ali
# Creation Date: 20-June-2021
# Version 1.0

def random_digit(n, l):
    for elm in range(n):
        if elm not in l:
            return elm

print(random_digit(n=10, l=[0,1,2,3,4,5]))
