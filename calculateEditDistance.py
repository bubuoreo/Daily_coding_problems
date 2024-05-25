"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""

# O(np(n-p))
def calculateEditDistance(entry, target):
    if (entry == target):
        return 0
    length_difference = abs(len(entry) - len(target))

    common_letters = 0
    longest_string, smallest_string = (entry, target) if (len(entry) > len(target)) else (target, entry)
    print(longest_string, smallest_string)
    for i in range(length_difference+1):
        p1, p2 = (i, 0)
        tmp_common_letter_counter = 0
        while p2 < len(smallest_string):
            if (longest_string[p1] == smallest_string[p2]):
                tmp_common_letter_counter += 1
            p1 += 1
            p2 += 1
        if tmp_common_letter_counter > common_letters:
            common_letters = tmp_common_letter_counter
    return len(longest_string) - common_letters


if __name__ == "__main__":
    entry = "toit"
    target = "cartotte"
    result = calculateEditDistance(entry, target)
    print(result)
