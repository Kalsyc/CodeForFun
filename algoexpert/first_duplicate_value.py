"""
Given an array of integers between 1 and n, inclusive, where n is the length of the array, write a function that returns the first integer that appears more than once (when the array is read from left to right).

In other words, out of all the integers that might occur more than once in the input array, your function should return the one whose first duplicate value has the minimum index.

If no integer appears more than once, your function should return -1.

Note that you're allowed to mutate the input array.
"""

def firstDuplicateValue(array):
    for idx in range(len(array)):
        if array[abs(array[idx]) - 1] < 0:
            return abs(array[idx])
        array[abs(array[idx]) - 1] *= -1
    return -1

"""
Time Complexity: O(n) where n is the number of elements in the array
Space Complexity: O(1)

The time complexity is O(n) because we iterate through each element in the array. The space complexity is O(1) because we only store the duplicate value in the array itself.
The idea is to iterate through the array and mark each element as negative if we have seen it before. We do this by using the element as an index and negating the value at that index. 
If we encounter a negative value at an index, it means we have seen that element before and we return it as the first duplicate value.
"""