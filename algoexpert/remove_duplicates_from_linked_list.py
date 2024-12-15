"""
You're given the head of a Singly Linked List whose nodes are in sorted order with respect to their values. Write a function that returns a modified version of the Linked List that doesn't contain any nodes with duplicate values. The Linked List should be modified in place (i.e., you shouldn't create a brand new list), and the modified Linked List should still have its nodes sorted with respect to their values.

Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of the list.
"""


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    current = linkedList.next
    prev_node = linkedList
    while current:
        if current.value == prev_node.value:
            current = current.next
            continue
        else:
            prev_node.next = current
            prev_node = current
            current = current.next
    prev_node.next = None
    return linkedList

"""
Time Complexity: O(n); Space Complexity: O(1)
The time complexity is O(n) where n is the number of nodes in the Linked List.
The space complexity is O(1) since we are not using any extra space.

The idea is to traverse the Linked List and remove any duplicate nodes. We keep track of the previous node and the current node. 
If the current node's value is equal to the previous node's value, we skip the current node.
Otherwise, we update the previous node's next pointer to point to the current node and move the previous node and current node pointers forward.
Finally, we set the next pointer of the last node to None to indicate the end of the modified Linked List.
"""