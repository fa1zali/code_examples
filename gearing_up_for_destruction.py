# Gearing Up for Destruction
# ==========================

# As Commander Lambda's personal assistant, you've been assigned the task of configuring the LAMBCHOP doomsday device's axial orientation gears. 
# It should be pretty simple -- just add gears to create the appropriate rotation ratio. But the problem is, due to the layout of the LAMBCHOP and 
# the complicated system of beams and pipes supporting it, the pegs that will support the gears are fixed in place.

# The LAMBCHOP's engineers have given you lists identifying the placement of groups of pegs along various support beams. You need to place a gear on 
# each peg (otherwise the gears will collide with unoccupied pegs). The engineers have plenty of gears in all different sizes stocked up, so you can 
# choose gears of any size, from a radius of 1 on up. Your goal is to build a system where the last gear rotates at twice the rate (in revolutions per minute, or rpm) 
# of the first gear, no matter the direction. Each gear (except the last) touches and turns the gear on the next peg to the right.

# Given a list of distinct positive integers named pegs representing the location of each peg along the support beam, write a function solution(pegs) which, 
# if there is a solution, returns a list of two positive integers a and b representing the numerator and denominator of the first gear's radius in its simplest 
# form in order to achieve the goal above, such that radius = a/b. The ratio a/b should be greater than or equal to 1. Not all support configurations will 
# necessarily be capable of creating the proper rotation ratio, so if the task is impossible, the function solution(pegs) should return the list [-1, -1].

# For example, if the pegs are placed at [4, 30, 50], then the first gear could have a radius of 12, the second gear could have a radius of 14, and the 
# last one a radius of 6. Thus, the last gear would rotate twice as fast as the first one. In this case, pegs would be [4, 30, 50] and solution(pegs) 
# should return [12, 1].

# The list pegs will be given sorted in ascending order and will contain at least 2 and no more than 20 distinct positive integers, 
# all between 1 and 10000 inclusive.


# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Python cases --
# Input:
# solution.solution([4, 30, 50])
# Output:
#     12,1

# Input:
# solution.solution([4, 17, 50])
# Output:
#     -1,-1

# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

# Python
# ======
# Your code will run inside a Python 2.7.13 sandbox. All tests will be run by calling the solution() function.

# Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.

# Input/output operations are not allowed.

# Your solution must be under 32000 characters in length including new lines and and other non-printing characters.

def answer(pegs):
    lth = len(pegs)
    dist = []
    ans = []
    flag = []

    # calculating the distance b/w the points
    for i in range(lth-1): 
        diff = pegs[i+1]-pegs[i]
        dist.append(diff)
    
    # finding the gear radius
    rd = 0  
    for elm in dist: 
        rd = elm - rd

    # check if first gear radius is positive or negative
    if len(dist) % 2 == 0: # positive condition
        ans =  [rd * -2,1] 
    elif len(dist) % 2 == 1: # negative condition
        if rd * 2 % 3 == 0: # if the numerator is divisible by 3
            ans = [rd * 2/3,1]
        else:
            ans = [rd * 2,3]

    # finding the size of gears
    gear_size = [float(ans[0])/float(ans[1])]
    x = gear_size[0]

    for elm in dist:
        x = elm - x
        gear_size.append(x)

    # checking the size and setting the flag
    for elm in gear_size: 
        if elm <= 1:
             flag.append(True)
        else:
            flag.append(False)
    
    if any(flag):
        return [-1,-1]
    else:
        return ans    

print(answer([4, 17, 50]))