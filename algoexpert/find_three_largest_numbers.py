"""
Write a function that takes in an array of at least three integers and, without sorting the input array, returns a sorted array of the three largest integers in the input array.

The function should return duplicate integers if necessary; for example, it should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12].
"""

def findThreeLargestNumbers(array):
    result = [array[0], array[1], array[2]]
    for i in array[3:]:
        curr_min = min(result)
        if i >= curr_min:
            if curr_min == result[0]:
                result[0] = i
            elif curr_min == result[1]:
                result[1] = i
            else:
                result[2] = i
    result.sort()
    return result

"""
Time Complexity: O(n); Space Complexity: O(1)
The time complexity is O(n) where n is the number of elements in the input array.
The space complexity is O(1) since we are not using any extra space.

The idea is to initialize a list with the first three elements of the input array. We then iterate through the remaining elements of the input array and update the list with the three largest elements while calculating the minimum element in the list. 
After the loop, we sort the list and return it.
"""