"""
You're given a binary expression tree. Write a function to evaluate this tree mathematically and return a single resulting integer.

All leaf nodes in the tree represent operands, which will always be positive integers. All of the other nodes represent operators. There are 4 operators supported, each of which is represented by a negative integer:

-1: Addition operator, adding the left and right subtrees.
-2: Subtraction operator, subtracting the right subtree from the left subtree.
-3: Division operator, dividing the left subtree by the right subtree. If the result is a decimal, it should be rounded towards zero.
-4: Multiplication operator, multiplying the left and right subtrees.

You can assume the tree will always be a valid expression tree. Each operator also works as a grouping symbol, meaning the bottom of the tree is always evaluated first, regardless of the operator.
"""

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def evaluateExpressionTree(tree):
    if tree.value == -1:
        return evaluateExpressionTree(tree.left) + evaluateExpressionTree(tree.right)
    elif tree.value == -2:
        return evaluateExpressionTree(tree.left) - evaluateExpressionTree(tree.right)
    elif tree.value == -3:
        return int(evaluateExpressionTree(tree.left) / evaluateExpressionTree(tree.right))
    elif tree.value == -4:
        return evaluateExpressionTree(tree.left) * evaluateExpressionTree(tree.right)
    else:
        return tree.value

"""
Time Complexity: O(n); Space Complexity: O(h)
The time complexity is O(n) where n is the number of nodes in the Binary Tree.
The space complexity is O(h) where h is the height of the Binary Tree.

The idea is to traverse the Binary Tree using a depth-first search (DFS) approach. We recursively evaluate the left and right subtrees of the current node and apply the corresponding operator to the results. 
We return the result of the operation at the current node.
"""