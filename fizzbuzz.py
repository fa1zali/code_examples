# Fizbuzz Problem

# Print numbers from 1 to 100, wherever the no. is divisible by 3 print fizz,
# divisible by 5 print buzz and fizzbuzz wherever it is divisble by both 5 and 3

# Author: Faisal Ali
# Creation Date: 29-Jan-2021
# Version 1.0

#Brute Force Approach
def fizbuzz1():
    for i in range(1,101):
        if (i % 15 == 0):
            print("fizzbuzz")
        elif (i % 5 == 0):
            print("buzz")
        elif (i % 3 == 0):
            print("fizz")
        else:
            print(i)

#Optimal Approach
def fizzbuzz2():
    for i in range(1,101):
        c3 = i % 3
        c5 = i % 5
        if (c3 == 0) and (c5 == 0):
            print("fizzbuzz")
        elif (c5 == 0):
            print("buzz")
        elif (c3 == 0):
            print("fizz")
        else:
            print(i)