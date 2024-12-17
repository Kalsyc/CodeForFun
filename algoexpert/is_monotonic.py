"""
Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.

An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.

Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase. Similarly, non-decreasing elements aren't necessarily exclusively increasing; they simply don't decrease.

Note that empty arrays and arrays of one element are monotonic.
"""

def isMonotonic(array):
    if len(array) <= 1:
        return True
    is_increasing, is_decreasing = False, False
    for i in range(len(array) - 1):
        curr_number = array[i]
        next_number = array[i + 1]
        if next_number < curr_number:
            is_decreasing = True
        elif next_number > curr_number:
            is_increasing = True
    return not (is_decreasing and is_increasing)

"""
Time Complexity: O(n) where n is the number of elements in the array
Space Complexity: O(1)

The time complexity is O(n) because we iterate through each element in the array. The space complexity is O(1) because we only store the flags for increasing and decreasing.

The idea is to iterate through each element in the array and check if the next element is less than the current element. 
If it is, we set the flag for decreasing to True. If the next element is greater than the current element, we set the flag for increasing to True.
Finally, we return the negation of the logical AND of the flags for increasing and decreasing. This works because if both flags are True, the array is not monotonic as it is both increasing and decreasing.
"""