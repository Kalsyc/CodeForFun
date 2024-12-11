"""
  Given two non-empty arrays of integers, write a function that determines
  whether the second array is a subsequence of the first one.

  A subsequence of an array is a set of numbers that aren't necessarily adjacent
  in the array but that are in the same order as they appear in the array. For
  instance, the numbers 
"""

def isValidSubsequence(array, sequence):
    pointer = 0
    for i in array:
        if i == sequence[pointer]:
            pointer += 1
        if pointer == len(sequence):
            return True
    return False

"""
Time Complexity: O(n); Space Complexity: O(1)
- The time complexity is O(n) because we are iterating through the array once.
- The space complexity is O(1) because we are not using any extra space.

The idea is to iterate through the array and compare the elements of the array with the elements of the sequence. 
If the elements match, then we increment the pointer to the next element in the sequence. 
If the pointer reaches the end of the sequence, then we return True. If we iterate through the entire array and do not find a subsequence, then we return False.
"""
