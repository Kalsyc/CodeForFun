"""
The distance between a node in a Binary Tree and the tree's root is called the node's depth.

Write a function that takes in a Binary Tree and returns the sum of its nodes' depths.

Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.
"""


"""
1st approach
"""
def nodeDepths(root):
    def helper_depths(root, curr_depth):
        if not root:
            return 0
        return curr_depth + helper_depths(root.left, curr_depth + 1) + helper_depths(root.right, curr_depth + 1)
    return helper_depths(root, 0)
    
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

"""
Time Complexity: O(n); Space Complexity: O(h)
The time complexity is O(n) where n is the number of nodes in the Binary Tree.
The space complexity is O(h) where h is the height of the Binary Tree.

The idea is to traverse the Binary Tree using a depth-first search (DFS) approach. We keep track of the current depth and update it as we move down the tree. 
We make recursive calls to the left and right children of the current node if they exist so that we can explore all possible paths in the tree.
"""



"""
2nd approach
"""
def nodeDepths(root):
    def helper_depths(root, curr_depth):
        sum_left, sum_right = 0, 0
        if not root:
            return 0
        if root.left:
            sum_left = curr_depth + helper_depths(root.left, curr_depth + 1)        
        if root.right:
            sum_right = curr_depth + helper_depths(root.right, curr_depth + 1)
        return sum_left + sum_right
    return helper_depths(root, 1)
    
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

"""
Time Complexity: O(n); Space Complexity: O(h)
The time complexity is O(n) where n is the number of nodes in the Binary Tree.
The space complexity is O(h) where h is the height of the Binary Tree.

The idea is to traverse the Binary Tree using a depth-first search (DFS) approach. We keep track of the current depth and update it as we move down the tree. 
We make recursive calls to the left and right children of the current node if they exist so that we can explore all possible paths in the tree.
"""