"""
Write a function that takes in an array of integers and returns a sorted version of that array. Use the Selection Sort algorithm to sort the array.

If you're unfamiliar with Selection Sort, we recommend watching the Conceptual Overview section of this question's video explanation before starting to code.
"""

def selectionSort(array):
    for i in range(len(array) - 1):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[min_idx], array[i] = array[i], array[min_idx]
    return array

"""
Time Complexity: O(n^2); Space Complexity: O(1)
The time complexity is O(n^2) where n is the number of elements in the array.
The space complexity is O(1) since we are not using any extra space.

The idea is to iterate through the array and select the minimum element in the unsorted part of the array. We then swap this minimum element with the first element of the unsorted part.
After each iteration, the first i elements will be sorted, and the rest will be unsorted. We continue this process until the entire array is sorted.
"""