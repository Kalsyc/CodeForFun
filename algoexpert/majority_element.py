"""
Write a function that takes in a non-empty, unordered array of positive integers and returns the array's majority element without sorting the array and without using more than constant space.

An array's majority element is an element of the array that appears in over half of its indices. Note that the most common element of an array (the element that appears the most times in the array) isn't necessarily the array's majority element; for example, the arrays [3, 2, 2, 1] and [3, 4, 2, 2, 1] both have 2 as their most common element, yet neither of these arrays have a majority element, because neither 2 nor any other element appears in over half of the respective arrays' indices.

You can assume that the input array will always have a majority element.
"""

def majorityElement(array):
    count = 0
    maj_ele = -1
    for num in array:
        if count == 0:
            maj_ele = num
        if num == maj_ele:
            count += 1
        else:
            count -= 1
    return maj_ele

"""
Time Complexity: O(n) where n is the number of elements in the array
Space Complexity: O(1)

The time complexity is O(n) because we iterate through each element in the array. The space complexity is O(1) because we do not use any extra space that grows with the input size.
The idea is to keep track of the majority element in the array. We iterate through the array and update the majority element if the count becomes zero. 
We increment the count if the current element is the same as the majority element, and decrement the count otherwise.

This works because the majority element appears more than n/2 times in the array. If we cancel out all the other elements with the majority element, the majority element will be left in the end.
"""