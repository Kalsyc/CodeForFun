"""
Write a function that takes in a non-empty list of non-empty strings and returns a list of characters that are common to all strings in the list, ignoring multiplicity.

Note that the strings are not guaranteed to only contain alphanumeric characters. The list you return can be in any order.
"""

def commonCharacters(strings):
    tracker_dict = dict()
    strings = list(map(lambda x: set(x), strings))
    for i in range(len(strings)):
        for letter in strings[i]:
            if letter in tracker_dict:
                tracker_dict[letter] += 1
            else:
                tracker_dict[letter] = 1
    result = []
    for key, value in tracker_dict.items():
        if value == len(strings):
            result.append(key)
    return result

"""
Time Complexity: O(n * m) where n is the number of strings and m is the length of the longest string
Space Complexity: O(n * m)
The time complexity is O(n * m) because we iterate through each string and each character in the string. The space complexity is O(n * m) because we store the characters in a dictionary.

The idea is to keep track of the characters that are common to all strings. We first convert each string to a set to remove duplicates. 
We then iterate through each string and each character in the string. We keep track of the characters in a dictionary and increment the count if the character is already in the dictionary. 
Finally, we iterate through the dictionary and append the characters that are common to all strings to the result list.
"""