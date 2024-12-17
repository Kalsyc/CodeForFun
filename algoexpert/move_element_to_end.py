"""
You're given an array of integers and an integer. Write a function that moves all instances of that integer in the array to the end of the array and returns the array.

The function should perform this in place (i.e., it should mutate the input array) and doesn't need to maintain the order of the other integers.
"""

def moveElementToEnd(array, toMove):
    left, right = 0, len(array) - 1
    while left < right:
        if array[left] == toMove and array[right] != toMove:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
        elif array[left] != toMove:
            left += 1
        else:
            right -= 1
    return array

"""
Time Complexity: O(n) where n is the number of elements in the array
Space Complexity: O(1)
The time complexity is O(n) because we iterate through each element in the array. The space complexity is O(1) because we only store the left and right pointers.

The idea is to set two pointers, left and right, to the start and end of the array respectively. We then iterate through the array and check if the element at the left pointer is equal to the element to move and the element at the right pointer is not equal to the element to move. 
If this is the case, we swap the elements at the left and right pointers and move the pointers accordingly. 
If the element at the left pointer is not equal to the element to move, we move the left pointer to the right. If the element at the right pointer is equal to the element to move, we move the right pointer to the left. 
We continue this process until the left pointer is greater than the right pointer. Finally, we return the array.
"""