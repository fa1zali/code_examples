# In the Gregorian calendar, three conditions are used to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.

def is_leap(year):
    leap = False

    if ((year % 400 == 0) and (year % 100 != 0)):
        leap = False
    elif year % 4 == 0:
        leap = True   
    return leap

print(is_leap(year = 2000))
print(is_leap(year = 2400))
print(is_leap(year = 2019))