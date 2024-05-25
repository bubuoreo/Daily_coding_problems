"""
Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
you should return:

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
Follow-up: What if you couldn't use any extra space?
"""


def rotate(matrix):
    new_matrix = [[] for _ in range(MATRIX_SIZE)]
    for i in range(len(matrix)):
        line = matrix.pop()
        for index in range(len(line)):
            new_matrix[index].append(line[index])
    return new_matrix

if __name__ == "__main__":
    MATRIX_SIZE = 3
    entry = []

    count = 1
    for i in range(MATRIX_SIZE):
        tmp = []
        for i in range(MATRIX_SIZE):
            tmp.append(count)
            count += 1
        entry.append(tmp)

    for element in entry:
        print(element)
    print("--------------------")
    new_matrix = rotate(entry)
    for element in new_matrix:
        print(element)