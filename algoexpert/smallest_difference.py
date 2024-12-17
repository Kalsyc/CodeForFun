"""
Write a function that takes in two non-empty arrays of integers, finds the pair of numbers (one from each array) whose absolute difference is closest to zero, and returns an array containing these two numbers, with the number from the first array in the first position.

Note that the absolute difference of two integers is the distance between them on the real number line. For example, the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.

You can assume that there will only be one pair of numbers with the smallest difference.
"""

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idx_one, idx_two = 0, 0
    min_pair = [arrayOne[idx_one], arrayTwo[idx_two]]
    while idx_one < len(arrayOne) and idx_two < len(arrayTwo):
        if abs(min_pair[0] - min_pair[1]) > abs(arrayOne[idx_one] - arrayTwo[idx_two]):
            min_pair = [arrayOne[idx_one], arrayTwo[idx_two]]
        if arrayOne[idx_one] == arrayTwo[idx_two]:
            break
        elif arrayOne[idx_one] < arrayTwo[idx_two]:
            idx_one += 1
        else:
            idx_two += 1
    return min_pair

"""
Time Complexity: O(nlog(n) + mlog(m)) where n is the number of elements in arrayOne and m is the number of elements in arrayTwo
Space Complexity: O(1)

The time complexity is O(nlog(n) + mlog(m)) because we sort both arrays and then iterate through each element in the arrays. The space complexity is O(1) because we only store the minimum pair of numbers.

The idea is to sort both arrays and iterate through each element in the arrays. We keep track of the minimum pair of numbers and update it if we find a pair with a smaller absolute difference. 
We then move the pointers of the arrays based on the comparison of the elements at the pointers. Finally, we return the minimum pair of numbers.
"""