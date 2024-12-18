"""
Write a function that takes in an array of integers and returns the length of the longest peak in the array.

A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip (the highest value in the peak), at which point they become strictly decreasing. At least three integers are required to form a peak.

For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10 don't and neither do the integers 1, 2, 2, 0. Similarly, the integers 1, 2, 3 don't form a peak because there aren't any strictly decreasing integers after the 3.
"""

def longestPeak(array):
    curr_longest = 0
    curr_value = 0
    is_increasing = False
    is_decreasing = False
    for i in range(len(array) - 1):   
        if (array[i+1] > array[i] or array[i+1] == array[i]) and is_increasing and is_decreasing:
            curr_longest = max(curr_value + 1, curr_longest)
            
        if array[i+1] > array[i] and is_decreasing:
            is_decreasing = False
            curr_value = 1
        elif array[i+1] > array[i] and not is_decreasing:
            is_increasing = True
            curr_value += 1
        elif array[i+1] < array[i] and is_increasing:
            is_decreasing = True
            curr_value += 1
        else:
            curr_value = 0
            is_decreasing, is_increasing = False, False
    if is_increasing and is_decreasing:
        curr_longest = max(curr_value + 1, curr_longest)
    return curr_longest

"""
Time Complexity: O(n) where n is the number of elements in the array
Space Complexity: O(1)

The time complexity is O(n) because we iterate through each element in the array. The space complexity is O(1) because we only store the current longest peak length and the current peak length.

The idea is to iterate through the array and keep track of the current peak length. We also keep track of whether we are currently increasing or decreasing.
"""