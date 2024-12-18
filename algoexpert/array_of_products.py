"""
Write a function that takes in a non-empty array of integers and returns an array of the same length, where each element in the output array is equal to the product of every other number in the input array.

In other words, the value at output[i] is equal to the product of every number in the input array other than input[i].

Note that you're expected to solve this problem without using division.
"""

def arrayOfProducts(array):
    left_arr, right_arr = [1], [1]
    for idx in range(len(array) - 1):
        left_arr.append(left_arr[idx] * array[idx])
        right_arr.append(right_arr[idx] * array[len(array) - 1 - idx])
    right_arr = right_arr[::-1]
    result = [left_arr[idx] * right_arr[idx] for idx in range(len(array))]
    return result

"""
Time Complexity: O(n) where n is the number of elements in the array
Space Complexity: O(n)

The time complexity is O(n) because we iterate through the array twice to calculate the left and right products. The space complexity is O(n) because we store the left and right products in separate arrays.
The idea is to calculate the left and right products of each element in the array. We initialize two arrays, left_arr and right_arr, with the first element as 1. We then iterate through the array to calculate the left and right products for each element.
This works because the left product of an element is the product of all elements to the left of it, and the right product of an element is the product of all elements to the right of it.
"""