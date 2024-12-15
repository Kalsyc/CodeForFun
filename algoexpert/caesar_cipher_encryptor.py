"""
Given a non-empty string of lowercase letters and a non-negative integer representing a key, write a function that returns a new string obtained by shifting every letter in the input string by k positions in the alphabet, where k is the key.

Note that letters should "wrap" around the alphabet; in other words, the letter z shifted by one returns the letter a.
"""

def caesarCipherEncryptor(string, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = {alphabet[idx]: alphabet[((key + idx) % len(alphabet))] for idx in range(len(alphabet))}
    return "".join([cipher[letter] for letter in string])

"""
Time Complexity: O(n); Space Complexity: O(1)
The time complexity is O(n) where n is the length of the input string.
The space complexity is O(1) since we are using a fixed-size dictionary to store the cipher mapping.

The idea is to create a dictionary that maps each letter of the alphabet to the letter obtained by shifting it by k positions. 
We then iterate through the input string and use the dictionary to get the corresponding cipher letter for each letter in the input string.
"""