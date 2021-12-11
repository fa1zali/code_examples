# Given the names and grades for each student in a class of N students, stored in a nested list. Print the name(s) of 
# any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and 
# print each name on a new line.

# Example
# records = [['chi', 20], ['alpha', 50], ['beta', 50], ['theta', 30], ['gamma', 30]]
# Output:
# gamma
# theta

def second_lowest(arr):
    scores = []
    dct = {}
    names = []

    for elm in arr:
        if elm[1] not in scores:
            scores.append(elm[1])
        dct[elm[0]] = elm[1]

    scores.sort()
    sec_lowest = scores[1]
    for key, value in dct.items():
        if value == sec_lowest:
            names.append(key)
    names.sort()
    for name in names:
        print(name)

second_lowest(arr = [['chi', 20], ['alpha', 50], ['beta', 50], ['theta', 30], ['gamma', 30]]) 
