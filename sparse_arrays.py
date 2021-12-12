# There is a collection of input strings and a collection of query strings. 
# For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

# strings = ['ab', 'ab', 'abc']
# queries = ['ab', 'abc', 'bc']

# There are 2 instances of 'ab', 1 of 'abc' and 0 of 'bc'. For each query, add an element to the return array, [2,1,0].

# First Approach
def matchingStrings(strings, queries):
    dct = {}
    lst = []
    for elm in queries:
        dct[elm] = 0
    
    for key in dct.keys():
        for elm in strings:
            if key == elm:
                dct[key] += 1
    
    for key, value in dct.items():
        lst.append(value)
    
    return lst

# Second Approach
def matchingStrings2(strings, queries):
    lst = []
    for i in range(len(queries)):
        lst.append(0)

    for i in range(len(queries)):
        for elm2 in strings:
            if queries[i] == elm2:
                lst[i] += 1
    return lst


print(matchingStrings(strings = ['ab', 'ab', 'abc'], queries =['ab', 'abc', 'bc']))
print(matchingStrings2(strings = ['ab', 'ab', 'abc'], queries =['ab', 'abc', 'bc']))