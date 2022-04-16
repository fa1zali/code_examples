# You're given a string consisting solely of (, ), and *. * can represent either a (, ), or an empty string. 
# Determine whether the parentheses are balanced.

# For example, (()* and (*) are balanced. )*( is not balanced.

def balanced(s:str):
    while s != "":
        if '(*)' in s:
            s = s.replace("(*)", "")
        elif '()' in s:
            s = s.replace("()", "")
        elif '(*' in s:
            s = s.replace("(*", "")
        elif '*)' in s:
            s = s.replace("*)", "")

        s_arr = list(s)
        count = 0
        for i in range(len(s)):
            if s_arr[i] == '*':
                count += 1
        if count == len(s_arr):
            return True
        else:
            return False

    return True

print(balanced("(*)"))