# Given a string, return the first recurring character in it, or null if there is no recurring character.

# For example, given the string "acbbac", return "b". Given the string "abcdef", return null.

# Author: Faisal Ali
# Creation Date: 05-July-2021
# Version 0.1

def first_rec_char(inp):
    storage = []
    for elm in inp:
        if elm not in storage:
            storage.append(elm)
        elif elm in storage:
            return elm
        else:
            return None

print(first_rec_char(inp = "acbbac"))
print(first_rec_char(inp = "abcdef"))