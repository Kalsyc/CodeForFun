"""
  Write a function that takes in a non-empty array of integers that are sorted
  in ascending order and returns a new array of the same length with the squares
  of the original integers also sorted in ascending order.
"""

def sortedSquaredArray(array):
    first_pointer, second_pointer = 0, len(array) - 1
    result = []
    while second_pointer >= first_pointer:
        if abs(array[second_pointer]) > abs(array[first_pointer]):
            result.append(array[second_pointer] ** 2)
            second_pointer -= 1
        else:
            result.append(array[first_pointer] ** 2)
            first_pointer += 1
    result.reverse()
    return result

"""
Time Complexity: O(n); Space Complexity: O(n)
- The time complexity is O(n) because we are iterating through the array once.
- The space complexity is O(n) because we are using extra space to store the result.

The idea is to use two pointers, one at the start of the array and one at the end of the array. We compare the absolute values of the elements at the two pointers. 
If the absolute value of the element at the end of the array is greater than the absolute value of the element at the start of the array, then we square the element at the end of the array and add it to the result array. 
Otherwise, we square the element at the start of the array and add it to the result array. We then move the pointers towards the middle of the array. We repeat this process until the two pointers meet in the middle of the array. 
Finally, we reverse the result array and return it.
"""