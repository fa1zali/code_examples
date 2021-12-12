# You are given a string .
# Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, 
# lowercase and uppercase characters.
# Example
# Input >> qA2
# Output
# True
# True
# True
# True
# True

if __name__ == '__main__':
    s = input()
    flags = ['False', 'False', 'False', 'False', 'False']
    for elm in s:
        if elm.isalnum():
            flags[0] = True
            break
    for elm in s:
        if elm.isalpha():
            flags[1] = True
            break
    for elm in s:
        if elm.isdigit():
            flags[2] = True
            break
    for elm in s:
        if elm.islower():
            flags[3] = True
            break
    for elm in s:
        if elm.isupper():
            flags[4] = True
            break
    
    for elm in flags:
        print(elm)