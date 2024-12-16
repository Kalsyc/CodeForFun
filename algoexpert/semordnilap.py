"""
Write a function that takes in a list of unique strings and returns a list of semordnilap pairs.

A semordnilap pair is defined as a set of different strings where the reverse of one word is the same as the forward version of the other. For example the words "diaper" and "repaid" are a semordnilap pair, as are the words "palindromes" and "semordnilap".

The order of the returned pairs and the order of the strings within each pair does not matter.
"""

def semordnilap(words):
    check_dict = set()
    result = []
    for word in words:
        if word in check_dict:
            result.append([word, word[::-1]])
        else:
            check_dict.add(word)
            check_dict.add(word[::-1])
    return result

"""
Time Complexity: O(n * m) where n is the number of words and m is the length of the longest word
Space Complexity: O(n * m)
The time complexity is O(n * m) because we iterate through each word and reverse the word. The space complexity is O(n * m) because we store the words in a set.

The idea is to keep track of the words and their reverse in a set. We iterate through each word and check if the word is in the set. 
If it is, we append the word and its reverse to the result list. If it is not, we add the word and its reverse to the set.
"""