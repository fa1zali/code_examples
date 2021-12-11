# Given an array of integers, where all elements but one occur twice, find the unique element.
# Example
# a = [1,2,3,4,3,2,1]
# The unique element is 4.

def lonelyinteger(a):
    dct = {}
    for elm in a:
        if elm not in dct:
            dct[elm]=1
        else:
            dct[elm] += 1
    for key, value in dct.items():
        if value == 1:
            print(key)

lonelyinteger([1,2,3,4,3,2,1])