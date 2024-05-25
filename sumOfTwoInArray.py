"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
from random import randint
import time

def sumOfTwoInArrayOnePass(array, k):
    seen_numbers = set()
    for number in array:
        if (k - number) in seen_numbers:
            print(number, k-number)
            return True
        seen_numbers.add(number)
    return False

if __name__ == "__main__":
    array = [randint(1,1000) for _ in range(1000)]
    k = randint(1,1000)
    print(array)
    print(k)
    
    start = time.time()
    print(sumOfTwoInArrayOnePass(array=array, k=k))
    print("Duration : ", time.time() - start, "s")
