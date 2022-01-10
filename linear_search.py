# Linear Search

# Unordered Linear Search

def unl_search(unordered_list, term):
    unordered_list_size = len(unordered_list)
    for i in range(unordered_list_size):
        if term == unordered_list[i]:
            return True
    return False

print(unl_search(unordered_list=[60,1,88,10,11,100], term=11))
print(unl_search(unordered_list=[60,1,88,10,11,100], term=2))

# Ordered Linear Search

def ol_search(ordered_list, term):
    ordered_list_size = len(ordered_list)
    for i in range(ordered_list_size):
        if term == ordered_list[i]:
            return True
        elif ordered_list[i] > term:
            return False
    return False

print(ol_search(ordered_list=[1,10,11,60,88,100], term=11))
print(ol_search(ordered_list=[1,10,11,60,88,100], term=2))