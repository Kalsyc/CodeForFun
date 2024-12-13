"""
You're given a 2D array of integers matrix. Write a function that returns the transpose of the matrix.

The transpose of a matrix is a flipped version of the original matrix across its main diagonal (which runs from top-left to bottom-right); it switches the row and column indices of the original matrix.

You can assume the input matrix always has at least 1 value; however its width and height are not necessarily the same.
"""

def transposeMatrix(matrix):
    result = []
    number_of_rows = len(matrix[0])
    number_of_columns = len(matrix)
    for i in range(number_of_rows):
        sub_array = []
        for j in range(number_of_columns):
            sub_array.append(matrix[j][i])
        result.append(sub_array)
    return result


"""
Time Complexity: O(n*m); Space Complexity: O(n*m)
- The time complexity is O(n*m) where n is the number of rows and m is the number of columns in the input matrix.
- The space complexity is O(n*m) because we are creating a new matrix to store the transposed matrix.

The idea is to iterate through the input matrix and create a new matrix where the rows and columns are switched. 
We iterate through the columns of the input matrix and create a new row in the transposed matrix by taking the elements from the corresponding column in the input matrix.
"""