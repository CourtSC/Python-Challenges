"""You are given a string s. Every letter in s appears once.

Consider all strings formed by rearranging the letters in s. After ordering these strings in dictionary order, return the middle term. (If the sequence has a even length n, define its middle term to be the (n/2)th term.)

Example
For s = "abc", the result should be "bac".

 The permutations in order are: "abc", "acb", "bac", "bca", "cab", "cba" So, The middle term is "bac".

Input/Output
[input] string s
unique letters (2 <= length <= 26)

[output] a string
middle permutation."""

from math import factorial


def middle_permutation(string):
    n = len(string)
    total_permutations = factorial(n)
    middle_index = total_permutations // 2
    letters = sorted(list(string))
    result = []
    for current_n in range(n, 0, -1):
        block = factorial(current_n - 1)
        index = (middle_index - 1) // block
        result.append(letters.pop(index))
        middle_index = middle_index - index * block
        print(current_n, block, index, result, middle_index)
    return "".join(result)
