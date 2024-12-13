"""
Write a function that takes in a Binary Search Tree (BST) and a target integer value and returns the closest value to that target value contained in the BST.

You can assume that there will only be one closest value.

Each BST node has an integer value, a left child node, and a right child node. 

A node is said to be a valid BST node if and only if it satisfies the BST property: 
its value is strictly greater than the values of every node to its left; 
its value is less than or equal to the values of every node to its right; 
and its children nodes are either valid BST nodes themselves or None / null.
"""

def findClosestValueInBst(tree, target):
    last_closest = tree.value
    current_diff = abs(target - tree.value)
    while tree:
        if tree.value > target:
            if abs(target - tree.value) < current_diff:
                last_closest = tree.value
                current_diff = abs(target - tree.value)
            tree = tree.left
        else:
            if abs(target - tree.value) < current_diff:
                last_closest = tree.value
                current_diff = abs(target - tree.value)
            tree = tree.right
    return last_closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

"""
Time Complexity: O(log(n)); Space Complexity: O(1)
Space complexity is O(1) because we are using a constant amount of space.
The time complexity is O(log(n)) where n is the number of nodes in the BST.

The idea is to traverse the BST starting from the root node and update the closest value as we move down the tree.
"""