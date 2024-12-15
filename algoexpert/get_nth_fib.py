"""
The Fibonacci sequence is defined as follows: the first number of the sequence is 0, the second number is 1, and the nth number is the sum of the (n - 1)th and (n - 2)th numbers. Write a function that takes in an integer n and returns the nth Fibonacci number.

Important note: the Fibonacci sequence is often defined with its first two numbers as F0 = 0 and F1 = 1. For the purpose of this question, the first Fibonacci number is F0; therefore, getNthFib(1) is equal to F0, getNthFib(2) is equal to F1, etc..
"""

def getNthFib(n):
    first, second = 0, 1
    for i in range(n - 1):
        first, second = second, first + second
    return first

"""
Time Complexity: O(n); Space Complexity: O(1)
The time complexity is O(n) where n is the input number n.
The space complexity is O(1) since we are not using any extra space.

The idea is to use two variables to keep track of the two previous Fibonacci numbers. We start with the first two Fibonacci numbers, 0 and 1, and iterate n - 1 times to calculate the nth Fibonacci number. 
We update the two variables in each iteration to keep track of the two previous Fibonacci numbers. After the loop, we return the first variable which contains the nth Fibonacci number.
"""