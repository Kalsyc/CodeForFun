"""
Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome.

A palindrome is defined as a string that's written the same forward and backward. Note that single-character strings are palindromes.
"""

def isPalindrome(string):
    first_pointer, second_pointer = 0, len(string) - 1
    while first_pointer < second_pointer:
        if string[first_pointer] != string[second_pointer]:
            return False
        first_pointer += 1
        second_pointer -= 1
    return True


"""
Time Complexity: O(n); Space Complexity: O(1)
The time complexity is O(n) where n is the length of the input string.
The space complexity is O(1) since we are not using any extra space.

The idea is to use two pointers, one starting from the beginning of the string and the other starting from the end of the string. We compare the characters at the two pointers and move them towards each other until they meet in the middle of the string. 
If at any point the characters are not equal, we return False. If the pointers meet in the middle of the string, we return True, indicating that the string is a palindrome.
"""