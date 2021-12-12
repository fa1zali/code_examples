# A pangram is a string that contains every letter of the alphabet. 
# Given a sentence determine whether it is a pangram in the English alphabet. 
# Ignore case. Return either pangram or not pangram as appropriate.

# Example
# Input: 'The quick brown fox jumps over the lazy dog'
# Output: pangram

def ispangram(string):
    new_string1 = string.split()
    new_string2 = "".join(new_string1)
    updated_string = new_string2.lower()

    dct = {}
    for i in range(97,123,1):
        dct[i] = 0

    for elm in updated_string:
        for key in dct.keys():
            if ord(elm) == key:
                dct[key] += 1

    for value in dct.values():
        if value == 0:
            return 'not pangram'
    return 'pangram'

print(ispangram(string = 'The quick brown fox jumps over the lazy dog'))
print(ispangram(string = 'We promptly judged antique ivory buckles for the prize'))
