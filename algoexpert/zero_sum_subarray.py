"""
You're given a list of integers nums. Write a function that returns a boolean representing whether there exists a zero-sum subarray of nums.

A zero-sum subarray is any subarray where all of the values add up to zero. A subarray is any contiguous section of the array. For the purposes of this problem, a subarray can be as small as one element and as long as the original array.
"""

def zeroSumSubarray(nums):
    sums = set([0])
    curr_sum = 0
    for num in nums:
        curr_sum += num
        if curr_sum in sums:
            return True
        sums.add(curr_sum)
    return False

"""
Time Complexity: O(n) where n is the number of elements in the array
Space Complexity: O(n)

The time complexity is O(n) because we iterate through each element in the array. The space complexity is O(n) because we store the prefix sums in a set.

The idea is to keep track of the prefix sums of the array. We iterate through the array and calculate the prefix sum at each index. 
If we encounter a prefix sum that we have seen before, it means that there is a subarray with a sum of zero. We return True in this case. If we reach the end of the array without finding a subarray with a sum of zero, we return False.
"""