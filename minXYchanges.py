"""
You are given a string consisting of the letters x and y, such as xyxxxyxyy. 
In addition, you have an operation called flip, which changes a single x to y 
or vice versa.

Determine how many times you would need to apply this operation to ensure that 
all x's come before all y's. In the preceding example, it suffices to flip 
the second and sixth characters, so you should return 2.
"""

string = "xxyxxyxxxyxyyyyxy"
i = 0
j = len(string)-1
count = 0
newString = string

while i < j:
    if (string[i] == 'y'):
        newString = newString[:i] + 'x' + newString[i+1:]
        count += 1
    if (string[j] == 'x'):
        newString = newString[:j] + 'y' + newString[j+1:]
        count += 1
    i += 1
    j -= 1

print(string)
print(newString)
print(count)