"""
Write a function that takes in a string of lowercase English-alphabet letters and returns the index of the string's first non-repeating character.

The first non-repeating character is the first character in a string that occurs only once.

If the input string doesn't have any non-repeating characters, your function should return -1.
"""

def firstNonRepeatingCharacter(string):

    check_dict = dict()
    for letter in string:
        check_dict[letter] = check_dict.get(letter, 0) + 1
    for idx in range(len(string)):
        if check_dict[string[idx]] == 1:
            return idx
    return -1

"""
Time Complexity: O(n) where n is the length of the string
Space Complexity: O(1)
The time complexity is O(n) because we iterate through the string once. The space complexity is O(1) because we store the characters in a dictionary.

The idea is to keep track of the frequency of characters in the string using a dictionary. We then iterate through the string and return the index of the first character that has a frequency of 1. If there are no non-repeating characters, we return -1.
"""