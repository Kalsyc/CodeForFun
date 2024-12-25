"""
Write a BST class for a Binary Search Tree. The class should support:

Inserting values with the insert method.
Removing values with the remove method; this method should only remove the first instance of a given value.
Searching for values with the contains method.
Note that you can't remove values from a single-node tree. In other words, calling the remove method on a single-node tree should simply not do anything.

Each BST node has an integer value, a left child node, and a right child node. 

A node is said to be a valid BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; 
and its children nodes are either valid BST nodes themselves or None / null.
"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        curr_node = self
        while True:
            if value < curr_node.value:
                if curr_node.left is None:
                    curr_node.left = BST(value)
                    break
                else:
                    curr_node = curr_node.left
            else:
                if curr_node.right is None:
                    curr_node.right = BST(value)
                    break
                else:
                    curr_node = curr_node.right
        return self

    def contains(self, value):
        curr_node = self
        while curr_node is not None:
            if value < curr_node.value:
                curr_node = curr_node.left
            elif value > curr_node.value:
                curr_node = curr_node.right
            else:
                return True
        return False

    def remove(self, value, parent_node=None):
        curr_node = self
        while curr_node is not None:
            if value < curr_node.value:
                parent_node = curr_node
                curr_node = curr_node.left
            elif value > curr_node.value:
                parent_node = curr_node
                curr_node = curr_node.right
            else:
                if curr_node.left is not None and curr_node.right is not None:
                    curr_node.value = curr_node.right.get_min_value()
                    curr_node.right.remove(curr_node.value, curr_node)
                elif parent_node is None:
                    if curr_node.left is not None:
                        curr_node.value = curr_node.left.value
                        curr_node.right = curr_node.left.right
                        curr_node.left = curr_node.left.left
                    elif curr_node.right is not None:
                        curr_node.value = curr_node.right.value
                        curr_node.left = curr_node.right.left
                        curr_node.right = curr_node.right.right
                    else:
                        pass
                elif parent_node.left == curr_node:
                    parent_node.left = curr_node.left if curr_node.left is not None else curr_node.right
                elif parent_node.right == curr_node:
                    parent_node.right = curr_node.left if curr_node.left is not None else curr_node.right
                break
        return self
    def get_min_value(self):
        curr_node = self
        while curr_node.left is not None:
            curr_node = curr_node.left
        return curr_node.value

"""
Average (all 3 methods): O(log(n)) time | O(1) space - where n is the number of nodes in the BST Worst (all 3 methods): O(n) time | O(1) space - where n is the number of nodes in the BST
"""