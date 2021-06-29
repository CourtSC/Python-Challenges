# A program that identifies the first character in a string that does not repeat.
# String will consist of lowercase english letters only and will not be empty.
# Length is 1 <= N <= 100000.
# Return "_" undercore if there is no non-repeating character.

def firstNRC(string):
    charCount = {}
    for c in string:
        if c not in charCount.keys():
            charCount[c] = 0
        charCount[c] += 1
    for k, v in charCount.items():
        if v == 1:
            return k
    return "_"

# Tests
print(
    firstNRC("aaabcccdeeef"), # b
    firstNRC("abcbad"), # c
    firstNRC("abcabcabc") # _
)