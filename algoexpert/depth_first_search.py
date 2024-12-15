"""
You're given a Node class that has a name and an array of optional children nodes. When put together, nodes form an acyclic tree-like structure.

Implement the depthFirstSearch method on the Node class, which takes in an empty array, traverses the tree using the Depth-first Search approach (specifically navigating the tree from left to right), stores all of the nodes' names in the input array, and returns it.

If you're unfamiliar with Depth-first Search, we recommend watching the Conceptual Overview section of this question's video explanation before starting to code.
"""

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
    
"""
Time Complexity: O(n); Space Complexity: O(n)
The time complexity is O(n) where n is the number of nodes in the tree.
The space complexity is O(n) where n is the number of nodes in the tree.

The idea is to traverse the tree using a depth-first search (DFS) approach. We start by adding the current node's name to the input array. Then, we recursively call the depthFirstSearch method on each of the current node's children.
"""