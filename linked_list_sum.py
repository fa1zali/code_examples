# Let's represent an integer in a linked list format by having each node represent a digit in the number. 
# The nodes make up the number in reversed order.

# For example, the following linked list:

# 1 -> 2 -> 3 -> 4 -> 5
# is the number 54321.

# Given two linked lists in this format, return their sum in the same linked list format.

# For example, given

# 9 -> 9
# 5 -> 2
# return 124 (99 + 25) as:

# 4 -> 2 -> 1

class Node:

    def __init__(self, data = None):
        self.data = data
        self.next = None
    
    def __str__(self):
        return self.data

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count += 1
    
    def iter(self):
        current = self.head
        while current:
            val = current.data
            yield val
            current = current.next

def reverse(n):
    rev = 0
    while n != 0:
        rem = n % 10
        rev = rev * 10 + rem
        n //= 10
    return rev

def solution(r1, r2):
    arr1 = []
    arr2 = []
    arr3 = []

    obj1 = LinkedList()
    obj2 = LinkedList()
    obj3 = LinkedList()

    str1 = list(str(r1))
    str2 = list(str(r2))

    for elm in str1:
        obj1.append(elm)

    print("1st number in reversed format in Linked List: ")
    x = 0
    for i in obj1.iter():
        arr1.append(i)
        x += 1
        print(i, end="")
        if x != obj1.count:
            print("->", end="")

    print("\n")

    for elm in str2:
        obj2.append(elm)

    print("2nd number in reversed format in Linked List: ")
    y = 0
    for i in obj2.iter():
        arr2.append(i)
        y += 1
        print(i, end="")
        if y != obj2.count:
            print("->", end="")

    print("\n")

    n1 = int("".join(arr1[::-1]))
    n2 = int("".join(arr2[::-1]))

    sum = n1 + n2
    rev_sum = reverse(sum)
    print(f"Sum of both numbers in reversed format: {rev_sum}")

    
    str3 = list(str(rev_sum))

    for elm in str3:
        obj3.append(elm)

    print("\nRepresentation of numbers in sum through Linked List:")
    c = 0
    for i in obj3.iter():
        arr3.append(i)
        c += 1
        print(i, end="")
        if c != obj3.count:
            print("->", end="")
    print("\n")
    return int("".join(arr3[::-1]))


r1 = reverse(int(input("Enter 1st number: ")))
r2 = reverse(int(input("Enter 2nd number: ")))

print(solution(r1, r2))