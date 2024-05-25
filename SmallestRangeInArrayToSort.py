# Intructions
# Given an array of integers out of order, determine the bounds of the smallest window 
# that must be sorted in order for the entire array to be sorted. 
# For example, given [3, 7, 5, 6, 9], you should return (1, 3).


def solver(array: list):
    p1 = 0
    p2 = len(array) - 1
    condition = True
    while condition:
        # get the leftmost list (from the beginning of the input array to the pointer p1)
        left = array[:p1+1]
        # check if the rightest is lower than all the rest of the input array
        if left[-1] > min(array[p1+1:]):
            p1 -= 1
            break
        # check if it is in order seeing if the following number is always higher than the previous
        for index in range(len(left)-1):
            if left[index] > left[index+1]:
                p1 -= 1
                condition = False
        # increase p1 if condition still valid
        if not condition:
            break
        else:
            p1 += 1
    while condition:
        # get the rightest list (from the pointer p2 to the end of the input array)
        right = array[p2:]
        # check if the leftest is higher than all the rest of the input array
        if right[0] < max(array[:p2]):
            p2 += 1
            break
        # check if it is in order seeing if the following number is always higher than the previous
        for index in range(len(right)-1):
            if right[index] > right[index+1]:
                p2 += 1
                condition = False
        # decrease p2 if True
        if not condition:
            break
        else:
            p2 -= 1
    return (p1+1,p2-1)

if __name__ == "__main__":
    entry = [3, 4, 7, 5, 6, 9]
    print(solver(entry))