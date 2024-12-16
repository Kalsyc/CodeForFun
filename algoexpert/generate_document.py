"""
You're given a string of available characters and a string representing a document that you need to generate. Write a function that determines if you can generate the document using the available characters. If you can generate the document, your function should return true; otherwise, it should return false.

You're only able to generate the document if the frequency of unique characters in the characters string is greater than or equal to the frequency of unique characters in the document string. For example, if you're given characters = "abcabc" and document = "aabbccc" you cannot generate the document because you're missing one c.

The document that you need to create may contain any characters, including special characters, capital letters, numbers, and spaces.

Note: you can always generate the empty string ("").
"""

def generateDocument(characters, document):
    char_dict = {}
    for letter in characters:
        if letter in char_dict:
            char_dict[letter] += 1
        else:
            char_dict[letter] = 1
    for letter in document:
        if letter not in char_dict or char_dict[letter] == 0:
            return False
        char_dict[letter] -= 1
    return True

"""
Time Complexity: O(n + m) where n is the number of characters and m is the number of characters in the document
Space Complexity: O(c) where c is the number of unique characters in the characters string
The time complexity is O(n + m) because we iterate through the characters and the document once. The space complexity is O(c) where c is the number of unique characters in the characters string.

The idea is to keep track of the frequency of characters in the characters string using a dictionary. We then iterate through the document and check if the character is in the dictionary and if the frequency is greater than 0. 
If it is, we decrement the frequency by 1. If the character is not in the dictionary or the frequency is 0, we return False. If we are able to iterate through the entire document, we return True.
"""