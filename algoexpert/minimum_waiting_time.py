"""
You're given a non-empty array of positive integers representing the amounts of time that specific queries take to execute. Only one query can be executed at a time, but the queries can be executed in any order.

A query's waiting time is defined as the amount of time that it must wait before its execution starts. In other words, if a query is executed second, then its waiting time is the duration of the first query; if a query is executed third, then its waiting time is the sum of the durations of the first two queries.

Write a function that returns the minimum amount of total waiting time for all of the queries. For example, if you're given the queries of durations [1, 4, 5], then the total waiting time if the queries were executed in the order of [5, 1, 4] would be (0) + (5) + (5 + 1) = 11. The first query of duration 5 would be executed immediately, so its waiting time would be 0, the second query of duration 1 would have to wait 5 seconds (the duration of the first query) to be executed, and the last query would have to wait the duration of the first two queries before being executed.

Note: you're allowed to mutate the input array.
"""

def minimumWaitingTime(queries):
    queries.sort()
    result = 0
    prev_query = queries[0]
    for i in range(1, len(queries)):
        result += prev_query
        prev_query += queries[i]
    return result


"""
Time Complexity: O(nlogn); Space Complexity: O(1)
The time complexity is O(nlogn) where n is the number of queries in the input array.
The space complexity is O(1) since we are not using any extra space.

The idea is to sort the queries in ascending order. This way, we can minimize the waiting time for each query by executing the shortest queries first. We then calculate the total waiting time by summing up the waiting time for each query. 
The waiting time for each query is the sum of the durations of all the previous queries.
"""