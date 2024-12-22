"""
You walk into a theatre you're about to see a show in. The usher within the theatre walks you to your row and mentions you're allowed to sit anywhere within the given row. Naturally you'd like to sit in the seat that gives you the most space. You also would prefer this space to be evenly distributed on either side of you (e.g. if there are three empty seats in a row, you would prefer to sit in the middle of those three seats).

Given the theatre row represented as an integer array, return the seat index of where you should sit. Ones represent occupied seats and zeroes represent empty seats.

You may assume that someone is always sitting in the first and last seat of the row. Whenever there are two equally good seats, you should sit in the seat with the lower index. If there is no seat to sit in, return -1. The given array will always have a length of at least one and contain only ones and zeroes.
"""

def bestSeat(seats):
    max_longest, curr_longest = 0, 0
    was_longest = False
    for seat in seats:
        if seat == 1 and was_longest:
            was_longest = False
            max_longest = max(curr_longest, max_longest)
            curr_longest = 0
        elif seat == 0 and not was_longest:
            was_longest = True
            curr_longest = 1
        else:
            curr_longest += 1
    curr_longest = 0
    idx = 0
    for idx in range(len(seats)):
        if seats[idx] == 0 and curr_longest + 1 == max_longest:
            return idx - (max_longest // 2)
        elif seats[idx] == 0:
            curr_longest += 1
        else:
            curr_longest = 0       
    return -1

"""
Time Complexity: O(n) where n is the number of seats in the row
Space Complexity: O(1)

The time complexity is O(n) because we iterate through the seats array twice. The space complexity is O(1) because we only store a few variables.

The idea is to iterate through the seats array and find the longest sequence of empty seats. We then iterate through the seats array again to find the seat index that is in the middle of the longest sequence of empty seats. 
If there are multiple seats that are in the middle of the longest sequence of empty seats, we return the one with the lower index.
"""