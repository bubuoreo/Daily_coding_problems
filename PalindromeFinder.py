"""
Given a string, split it into as few strings as possible such that each string is a palindrome.

For example, given the input string racecarannakayak, return ["racecar", "anna", "kayak"].

Given the input string abc, return ["a", "b", "c"].
"""

def palindromeFinder(string):
    ret= []
    tmp_string = string
    while len(string):
        i, j = (0, len(tmp_string)-1)
        while i <= j:
            if tmp_string[i] == tmp_string[j] and (i == j or abs(i-j) == 1):
                ret.append(tmp_string)
                string = string[len(tmp_string):]
                tmp_string = string
                break
            elif tmp_string[i] == tmp_string[j]:
                i += 1
                j -= 1
            else:
                tmp_string = tmp_string[:-1]
                break

    return ret

if __name__ == "__main__":
    # entry = "racecarannakayak"
    entry = "abc"
    palindrome_list = palindromeFinder(entry)
    print(palindrome_list)