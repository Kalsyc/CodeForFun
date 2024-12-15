"""
You're given a Linked List with at least one node. Write a function that returns the middle node of the Linked List. If there are two middle nodes (i.e. an even length list), your function should return the second of these nodes.

Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of the list.
"""

"""
Solution 1
"""

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    length_of_list = 0
    current = linkedList
    while current:
        length_of_list += 1
        current = current.next
    traversals_needed = length_of_list // 2
    middle_node = linkedList
    for i in range(traversals_needed):
        middle_node = middle_node.next
    return middle_node

"""
Time Complexity: O(n); Space Complexity: O(1)
The time complexity is O(n) where n is the number of nodes in the Linked List.
The space complexity is O(1) since we are not using any extra space.

The idea is to first traverse the Linked List to find the length of the list. After that, we calculate the number of traversals needed to reach the middle node. We then traverse the Linked List again to reach the middle node and return it.
"""

"""
Solution 2
"""

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    slow_node = linkedList
    fast_node = linkedList
    while fast_node and fast_node.next:
        slow_node = slow_node.next
        fast_node = fast_node.next.next
    return slow_node

"""
Time Complexity: O(n); Space Complexity: O(1)
The time complexity is O(n) where n is the number of nodes in the Linked List.
The space complexity is O(1) since we are not using any extra space.

The idea is to use two pointers, a slow pointer and a fast pointer. The slow pointer moves one node at a time while the fast pointer moves two nodes at a time. 
When the fast pointer reaches the end of the Linked List, the slow pointer will be at the middle node.
"""