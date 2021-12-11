# In this challenge, the user enters a string and a substring. You have to print the number of times that the 
# substring occurs in the given string. String traversal will take place from left to right, not from right to left.
# NOTE: String letters are case-sensitive.
# Input Format
# The first line of input contains the original string. The next line contains the substring.
# Sample Input
# ABCDCDC
# CDC
# Sample Output
# 2

substrings = []

def create_substrings(string):
    while len(string) != 0:
        lst = []
        char = ''
        for elm in string:
            char += elm
            substrings.append(char)
            lst.append(elm)
        del lst[0]
        new_string = "".join(lst)
        return create_substrings(new_string)

def count_substring(string, sub_string):
    create_substrings(string)
    print(substrings)
    count = 0
    for elm in substrings:
        if elm == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)