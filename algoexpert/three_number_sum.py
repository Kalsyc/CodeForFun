"""
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.

If no three numbers sum up to the target sum, the function should return an empty array.
"""

def threeNumberSum(array, targetSum):
    array.sort()
    result = []
    for curr_idx in range(len(array) - 1):
        left, right = curr_idx + 1, len(array) - 1
        while left < right:
            current_sum = array[curr_idx] + array[left] + array[right]
            if current_sum  == targetSum:
                result.append([array[curr_idx], array[left], array[right]])
                right -= 1
                left += 1
            elif current_sum > targetSum:
                right -= 1
            else:
                left += 1
    return result

"""
Time Complexity: O(n^2) where n is the number of elements in the array
Space Complexity: O(n)

The time complexity is O(n^2) because we iterate through each element in the array and for each element, we iterate through the remaining elements in the array. The space complexity is O(n) because we store the triplets in a list.

The idea is to sort the array and iterate through each element in the array. For each element, we set two pointers, left and right, to the next element and the last element in the array respectively. 
We then calculate the current sum of the three elements and check if it is equal to the target sum. If it is, we append the three elements to the result list. If the current sum is greater than the target sum, we move the right pointer to the left. 
If the current sum is less than the target sum, we move the left pointer to the right.
Finally, we return the result list.
"""