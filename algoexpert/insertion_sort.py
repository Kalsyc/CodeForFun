"""
Write a function that takes in an array of integers and returns a sorted version of that array. Use the Insertion Sort algorithm to sort the array.

If you're unfamiliar with Insertion Sort, we recommend watching the Conceptual Overview section of this question's video explanation before starting to code.
"""

def insertionSort(array):
    for i in range(1, len(array)):
        while i > 0 and array[i] < array[i - 1]:
            array[i - 1], array[i] = array[i], array[i - 1]
            i -= 1
    return array

"""
Time Complexity: O(n^2); Space Complexity: O(1)
The time complexity is O(n^2) where n is the number of elements in the array.
The space complexity is O(1) since we are not using any extra space.

The idea is to iterate through the array and insert each element into its correct position in the sorted part of the array. 
We start with the second element and compare it with the elements to its left, moving elements to the right until we find the correct position for the current element.
After the loop, the array will be sorted, and we return it.
"""