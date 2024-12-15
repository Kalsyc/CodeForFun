"""
Write a function that takes in a sorted array of integers as well as a target integer. The function should use the Binary Search algorithm to determine if the target integer is contained in the array and should return its index if it is, otherwise -1.

If you're unfamiliar with Binary Search, we recommend watching the Conceptual Overview section of this question's video explanation before starting to code.
"""

def binarySearch(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

"""
Time Complexity: O(log(n)); Space Complexity: O(1)
The time complexity is O(log(n)) where n is the number of elements in the array.
The space complexity is O(1) since we are not using any extra space.

The idea is to use the Binary Search algorithm to find the target integer in the sorted array. We keep track of the left and right pointers and calculate the mid index in each iteration. 
If the mid element is equal to the target, we return the mid index. If the mid element is greater than the target, we update the right pointer to mid - 1. 
If the mid element is less than the target, we update the left pointer to mid + 1. We continue this process until the left pointer is less than or equal to the right pointer. 
If the target is not found, we return -1.
"""