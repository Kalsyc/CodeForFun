"""
Given an array of positive integers representing the values of coins in your possession, write a function that returns the minimum amount of change (the minimum sum of money) that you cannot create. 
The given coins can have any positive integer value and aren't necessarily unique (i.e., you can have multiple coins of the same value).

For example, if you're given coins = [1, 2, 5], the minimum amount of change that you can't create is 4. If you're given no coins, the minimum amount of change that you can't create is 1.
"""

def nonConstructibleChange(coins):
    coins.sort()
    current_possible_change = 0
    for coin in coins:
        if coin > current_possible_change + 1:
            return current_possible_change + 1
        else:
            current_possible_change += coin
    return current_possible_change + 1

"""
Time Complexity: O(nlogn); Space Complexity: O(1)
- The time complexity is O(nlogn) because we are sorting the coins array.
- The space complexity is O(1) because we are using a constant amount of space.

The idea is to sort the coins array and iterate through the coins. At each step, we check if the current coin is greater than the current_possible_change + 1. If it is, then we return current_possible_change + 1. 
Otherwise, we update the current_possible_change by adding the current coin value. This works because if the current coin is greater than the current_possible_change + 1, then we cannot create the amount current_possible_change + 1.
"""
