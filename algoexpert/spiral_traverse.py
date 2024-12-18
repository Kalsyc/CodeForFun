"""
Write a function that takes in an n x m two-dimensional array (that can be square-shaped when n == m) and returns a one-dimensional array of all the array's elements in spiral order.

Spiral order starts at the top left corner of the two-dimensional array, goes to the right, and proceeds in a spiral pattern all the way until every element has been visited.

array = [
  [1,   2,  3, 4],
  [12, 13, 14, 5],
  [11, 16, 15, 6],
  [10,  9,  8, 7],
]

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
"""

def spiralTraverse(array):
    result = []
    start_row, end_row = 0, len(array) - 1
    start_col, end_col = 0, len(array[0]) - 1

    while start_row <= end_row and start_col <= end_col:
        for col in range(start_col, end_col + 1):
            result.append(array[start_row][col])
        for row in range(start_row + 1, end_row + 1):
            result.append(array[row][end_col])
        for col in reversed(range(start_col, end_col)):
            if start_row == end_row:
                break
            result.append(array[end_row][col])
        for row in reversed(range(start_row + 1, end_row)):
            if start_col == end_col:
                break
            result.append(array[row][start_col])
        start_row += 1
        end_row -= 1
        start_col += 1
        end_col -= 1
    return result

"""
Time Complexity: O(n) where n is the number of elements in the two-dimensional array
Space Complexity: O(n)

The time complexity is O(n) because we iterate through each element in the two-dimensional array. The space complexity is O(n) because we store the elements in the result array.

The idea is to iterate through the array in a spiral pattern. We keep track of the start and end rows and columns, and we iterate through the array in four steps: right, down, left, and up. 
We update the start and end rows and columns after each step to ensure that we don't revisit elements. 
We also add a check to break out of the loop if the start and end rows or columns are equal, which means we have reached the center of the array.
"""