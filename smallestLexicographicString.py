"""
You are given a string of length N and a parameter k. The string can be manipulated by taking one of the first k letters and moving it to the end.

Write a program to determine the lexicographically smallest string that can be created after an unlimited number of moves.

For example, suppose we are given the string daily and k = 1. The best we can create in this case is ailyd.
"""

def smallestLexicographicString(entry, k):
    if k > len(entry):
        return "Error: indice must be lower than the size of the entry"
    all_strings = []
    for i in range(k):
        new_string = entry[:i] + entry[i+1:] + entry[i]
        all_strings.append(new_string)
    print(all_strings)
    all_strings.sort()
    print(all_strings)
    return all_strings[0]


if __name__ == "__main__":
    entry = "abbaababbbaba"
    k = 8
    result = smallestLexicographicString(entry, k)
    print(result)