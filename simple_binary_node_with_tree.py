# A very simple implementation of a binary tree node and creating a tree

class TreeNode:
    def __init__(self, data = None):
        self.data = data
        self.right_child = None
        self.left_child = None
    
    def __repr__(self):
        return str(self.data)

n1 = TreeNode("Root Node")
n2 = TreeNode("Left Child")
n3 = TreeNode("Right Child")
n4 = TreeNode("Grand Left Child")

n1.left_child = n2 
n1.right_child = n3
n2.left_child = n4

current = n1
while current:
    print(current.data)
    current = current.left_child # Only traversing the left child