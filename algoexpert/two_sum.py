"""
  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. If any two numbers in the input array sum
  up to the target sum, the function should return them in an array, in any
  order. If no two numbers sum up to the target sum, the function should return
  an empty array.

  Note that the target sum has to be obtained by summing two different integers
  in the array; you can't add a single integer to itself in order to obtain the
  target sum.

  You can assume that there will be at most one pair of numbers summing up to
  the target sum.
"""

def twoNumberSum(array, targetSum):
    map_dict = {}
    for i in array:
        if i in map_dict:
            return [i, map_dict[i]]
        map_dict[targetSum - i] = i
    return []

"""
Time Complexity: O(n); Space Complexity: O(n)
- The time complexity is O(n) because we are iterating through the array once.
- The space complexity is O(n) because we are storing the values in a dictionary.

The idea is to iterate through the array and store the difference between the target sum and the current element in a dictionary. 
If the current element is in the dictionary, then we have found the pair of numbers that sum up to the target sum. 
If we iterate through the entire array and do not find a pair of numbers that sum up to the target sum, then we return an empty array.
"""