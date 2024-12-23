"""
You're given an unordered list of unique integers nums in the range [1, n], where n represents the length of nums + 2. This means that two numbers in this range are missing from the list.

Write a function that takes in this list and returns a new list with the two missing numbers, sorted numerically.
"""

def missingNumbers(nums):
    nums.extend([float("inf"), float("inf")])
    for idx in range(len(nums) - 2):
        visited_idx = abs(nums[idx]) - 1
        nums[visited_idx] *= - 1
    result = []
    for idx in range(len(nums)):
        if nums[idx] > 0:
            result.append(idx + 1)
    return result

"""
Time Complexity: O(n) where n is the number of elements in the array
Space Complexity: O(1)

The time complexity is O(n) because we iterate through each element in the array. The space complexity is O(1) because we do not use any extra space that grows with the input size.
The idea is to iterate through the array and mark the indices of the elements that we have seen. We do this by negating the element at the index that corresponds to the value of the element.
For example, if we see the element 3, we negate the element at index 3 - 1 = 2. This way, we can keep track of the elements that we have seen.
After marking all the elements that we have seen, we iterate through the array again and check which indices are positive. The indices that are positive correspond to the missing numbers in the array.
"""