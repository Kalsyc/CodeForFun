"""
It's photo day at the local school, and you're the photographer assigned to take class photos. The class that you'll be photographing has an even number of students, and all these students are wearing red or blue shirts. In fact, exactly half of the class is wearing red shirts, and the other half is wearing blue shirts. You're responsible for arranging the students in two rows before taking the photo. Each row should contain the same number of the students and should adhere to the following guidelines:

All students wearing red shirts must be in the same row.
All students wearing blue shirts must be in the same row.
Each student in the back row must be strictly taller than the student directly in front of them in the front row.
You're given two input arrays: one containing the heights of all the students with red shirts and another one containing the heights of all the students with blue shirts. These arrays will always have the same length, and each height will be a positive integer. Write a function that returns whether or not a class photo that follows the stated guidelines can be taken.

Note: you can assume that each class has at least 2 students.
"""

def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    if redShirtHeights[0] > blueShirtHeights[0]:
        back_row, front_row = redShirtHeights, blueShirtHeights
    elif blueShirtHeights[0] > redShirtHeights[0]:
        back_row, front_row = blueShirtHeights, redShirtHeights
    else:
        return False
    for i in range(len(front_row)):
        if back_row[i] <= front_row[i]:
            return False
    return True

"""
Time Complexity: O(nlogn); Space Complexity: O(1)
The time complexity is O(nlogn) where n is the number of students in each class.
The space complexity is O(1) since we are not using any extra space.

The idea is to sort the two input arrays in ascending order. We then compare the heights of the first students in each class. 
If the height of the first student in the back row is greater than the height of the first student in the front row, we assign the back row to the students with the greater heights. 
Otherwise, we assign the back row to the students with the smaller heights. 
We then iterate through the two rows and check if the height of each student in the back row is strictly greater than the height of the corresponding student in the front row. 
If we find a student in the back row who is not taller than the corresponding student in the front row, we return False. Otherwise, we return True.
"""