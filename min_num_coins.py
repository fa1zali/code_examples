# Find the minimum number of coins required to make n cents.

# You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

# For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.

# Author: Faisal Ali
# Creation Date: 10-June-2021
# Version 1.0

def number_of_coins(amt):
    c1 = c2 = c3 = c4 = 0
    while amt >= 25:
        c1 += 1
        amt -= 25

    while amt >= 10:
        c2 += 1
        amt -= 10

    while amt >= 5:
        c3 += 1
        amt -= 5
    
    while amt >= 1:
        c4 += 1
        amt -= 1
    
    return c1+c2+c3+c4

print(number_of_coins(16))