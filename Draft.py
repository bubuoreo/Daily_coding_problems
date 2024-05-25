"""
Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""

if __name__ == "__main__":
    entry = [6, 1, 3, 3, 3, 6, 6, 1, 1, 9]
    entry_sum = sum(entry)
    triple_unique_sum = sum(set(entry))*3
    print(int((triple_unique_sum - entry_sum)/2))
