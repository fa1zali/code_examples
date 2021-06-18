# Given a string of words delimited by spaces, reverse the words in string. 
# For example, given "hello world here", return "here world hello"

# Author: Faisal Ali
# Creation Date: 18-June-2021
# Version 1.0

def reverse(str):
    new_list = str.split(" ")
    rvs_list = new_list[::-1]
    print(rvs_list)
    for elm in rvs_list:
        print(elm, sep=" ", end=" ") 

reverse("hello world here")