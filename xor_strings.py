# Given two strings consisting of digits 0 and 1 only, find the XOR of the two strings.
# Input
# 10101
# 00101
# Sample Output
# 10000
# XOR = Output is 1 when both inputs differ

def xor_strings(str1, str2):
    new_str = ""
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            new_str += '0'
        else:
            new_str += '1'
    return new_str

print(xor_strings('10101', '00101'))