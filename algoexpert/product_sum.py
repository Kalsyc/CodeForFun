"""
Write a function that takes in a "special" array and returns its product sum.

A "special" array is a non-empty array that contains either integers or other "special" arrays. The product sum of a "special" array is the sum of its elements, where "special" arrays inside it are summed themselves and then multiplied by their level of depth.

The depth of a "special" array is how far nested it is. For instance, the depth of [] is 1; the depth of the inner array in [[]] is 2; the depth of the innermost array in [[[]]] is 3.

Therefore, the product sum of [x, y] is x + y; the product sum of [x, [y, z]] is x + 2 * (y + z); the product sum of [x, [y, [z]]] is x + 2 * (y + 3z).
"""

def productSum(array):
    def helper(array, depth):
        if not array:
            return 0
        next_ele = array[0]
        if type(next_ele) == list:
            return (depth + 1) * helper(next_ele, depth + 1) + helper(array[1:], depth)
        return next_ele + helper(array[1:], depth)
    return helper(array, 1)

"""
Time Complexity: O(n); Space Complexity: O(d)
The time complexity is O(n) where n is the number of elements in the "special" array.
The space complexity is O(d) where d is the depth of the "special" array.
The idea is to recursively traverse the "special" array and calculate the product sum. We keep track of the depth of the array and multiply the sum of the inner array by the depth. We continue this process until we reach the end of the array.
"""