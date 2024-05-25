def solver(nbRows: int) -> list:
    if nbRows == 1:
        return [1]
    return recusrsiveHelper(nbRows-1, [1])
    
def recusrsiveHelper(nbRows: int, array: list):
    p1 = 0
    p2 = 1
    newArray = []
    while p2 < len(array):
        newArray.append(array[p1] + array[p2])
        p1 += 1
        p2 += 1
    newArray = [1] + newArray + [1]
    if nbRows == 1:
        return newArray
    else:
        return recusrsiveHelper(nbRows-1, newArray)

if __name__ == "__main__":
    print(solver(30))

