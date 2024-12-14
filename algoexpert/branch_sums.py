"""
Write a function that takes in a Binary Tree and returns a list of its branch sums ordered from leftmost branch sum to rightmost branch sum.

A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch is a path of nodes in a tree that starts at the root node and ends at any leaf node.

Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.
"""


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    result = []
    def helper_branch(root, curr_value):
        if not root.left and not root.right:
            result.append(curr_value + root.value)
            return
        if root.left:
            helper_branch(root.left, curr_value + root.value)
        if root.right:
            helper_branch(root.right, curr_value + root.value)
    helper_branch(root, 0)
    return result

"""
Time Complexity: O(n); Space Complexity: O(n)
The time complexity is O(n) where n is the number of nodes in the Binary Tree.
The space complexity is O(n) because the recursive calls are stored in the call stack.

The idea is to traverse the Binary Tree using a depth-first search (DFS) approach. We keep track of the current branch sum and update it as we move down the tree. When we reach a leaf node, we add the branch sum to the result list.
We make recursive calls to the left and right children of the current node if they exist so that we can explore all possible branches in the tree.
"""