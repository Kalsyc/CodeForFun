"""
Write a function that takes in an array of integers and returns a sorted version of that array. Use the Bubble Sort algorithm to sort the array.

If you're unfamiliar with Bubble Sort, we recommend watching the Conceptual Overview section of this question's video explanation before starting to code.
"""

def bubbleSort(array):
    for i in range(len(array) - 1):
        check_pass = True
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                check_pass = False
        if check_pass:
            return array
    return array

"""
Time Complexity: O(n^2); Space Complexity: O(1)
The time complexity is O(n^2) where n is the number of elements in the array.
The space complexity is O(1) since we are not using any extra space.

The idea is to iterate through the array multiple times, comparing adjacent elements and swapping them if they are in the wrong order. In each pass, the largest unsorted element will "bubble up" to its correct position.
We keep track of whether any swaps were made in a pass. If no swaps were made, the array is already sorted, and we can return it early.
"""