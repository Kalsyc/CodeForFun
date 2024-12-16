"""
Write a function that takes in a non-empty string and returns its run-length encoding.

From Wikipedia, "run-length encoding is a form of lossless data compression in which runs of data are stored as a single data value and count, rather than as the original run." For this problem, a run of data is any sequence of consecutive, identical characters. So the run "AAA" would be run-length-encoded as "3A".

To make things more complicated, however, the input string can contain all sorts of special characters, including numbers. And since encoded data must be decodable, this means that we can't naively run-length-encode long runs. For example, the run "AAAAAAAAAAAA" (12 As), can't naively be encoded as "12A", since this string can be decoded as either "AAAAAAAAAAAA" or "1AA".

Thus, long runs (runs of 10 or more characters) should be encoded in a split fashion; the aforementioned run should be encoded as "9A3A".
"""

def runLengthEncoding(string):
    result = []
    curr_repeat = 1
    prev_letter = string[0]
    for letter in string[1:]:
        if curr_repeat == 9 or letter != prev_letter:
            result.append(str(curr_repeat) + prev_letter)
            curr_repeat = 0
        curr_repeat += 1
        prev_letter = letter
    result.append(str(curr_repeat) + prev_letter)
    return "".join(result)

"""
Time Complexity: O(n)
Space Complexity: O(n)

Time complexity is O(n) because we iterate through the string once. Space complexity is O(n) because we store the result in a list.
Space complexity is O(n) because we store the result in a list/string.

The idea is to keep track of the current repeat count and the previous letter. We iterate through the string and if the current repeat count is 9 or the current letter is different from the previous letter, we append the current repeat count and the previous letter to the result list. 
We then reset the current repeat count to 0. We then increment the current repeat count and update the previous letter. 
Finally, we append the last repeat count and letter to the result list and return the result as a string.
"""