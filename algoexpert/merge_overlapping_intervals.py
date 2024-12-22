"""
Write a function that takes in a non-empty array of arbitrary intervals, merges any overlapping intervals, and returns the new intervals in no particular order.

Each interval interval is an array of two integers, with interval[0] as the start of the interval and interval[1] as the end of the interval.

Note that back-to-back intervals aren't considered to be overlapping. For example, [1, 5] and [6, 7] aren't overlapping; however, [1, 6] and [6, 7] are indeed overlapping.

Also note that the start of any particular interval will always be less than or equal to the end of that interval.
"""

def mergeOverlappingIntervals(intervals):
    intervals.sort(key=lambda x: x[0])
    prev_interval = intervals[0]
    result = [prev_interval]
    idx = 1
    while idx < len(intervals):
        curr_interval = intervals[idx]
        prev_interval = result[-1]
        if curr_interval[0] > prev_interval[1]:
            result.append(curr_interval)
        elif curr_interval[1] > prev_interval[1]:
            prev_interval[1] = curr_interval[1]
        idx += 1
    return result

"""
Time Complexity: O(nlogn) where n is the number of intervals
Space Complexity: O(n)
The time complexity is O(nlogn) because we sort the intervals array based on the start time of each interval. The space complexity is O(n) because we store the merged intervals in the result array.

The idea is to sort the intervals based on the start time of each interval. We then iterate through the sorted intervals and merge overlapping intervals. We keep track of the previous interval and the current interval. 
If the current interval starts after the end of the previous interval, we add the current interval to the result. If the current interval overlaps with the previous interval, we update the end time of the previous interval to be the maximum of the two end times.
"""