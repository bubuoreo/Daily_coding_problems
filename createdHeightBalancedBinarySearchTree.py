"""
Given a sorted array, convert it into a height-balanced binary search tree.
"""

from random import randint

COUNT = [10]

class Node:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
    

def createdHeightBalancedBinarySearchTree(array):
    if not array:
        return None

    middle = len(array) // 2
    root = Node(val=array[middle])

    root.left = createdHeightBalancedBinarySearchTree(array[:middle])
    root.right = createdHeightBalancedBinarySearchTree(array[middle+1:])

    return root

def print2DUtil(root, space):
 
    # Base case
    if (root == None):
        return
 
    # Increase distance between levels
    space += COUNT[0]
 
    # Process right child first
    print2DUtil(root.right, space)
 
    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.val)
 
    # Process left child
    print2DUtil(root.left, space)
 
# Wrapper over print2DUtil()
 
 
def print2D(root):
 
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)

if __name__ == "__main__":
    entry = [randint(1, 100) for _ in range(10)]
    entry.sort()
    print(entry)
    root = createdHeightBalancedBinarySearchTree(entry)
    print2D(root)
