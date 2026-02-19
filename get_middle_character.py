#! python 3.14
"""
You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

If the string's length is odd, return the middle character.
If the string's length is even, return the middle 2 characters.
Examples:
"test" --> "es"
"testing" --> "t"
"middle" --> "dd"
"A" --> "A"
"""


def get_middle(s):
    middle_idx = len(s) // 2
    if len(s) % 2 == 0:
        return s[middle_idx - 1 : middle_idx + 1]
    else:
        return s[middle_idx]


def divmod_solution(s):
    idx, odd = divmod(len(s), 2)
    return s[idx] if odd else s[idx - 1 : idx + 1]


if __name__ == "__main__":
    tests = ["test", "testing", "middle", "A", "of", "qJwRqoOBwVaTJ"]
    for test in tests:
        print(get_middle(test))
