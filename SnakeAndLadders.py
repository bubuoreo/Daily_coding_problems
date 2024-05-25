from random import randint
from queue import PriorityQueue


def solve_snakes_and_ladders(snakes, ladders):
    case = 0
    weight = 0
    queue = PriorityQueue()
    previous = []
    queue.put((weight,(case, previous)))
    while case < 100:
        weight, (case, previous) = queue.get()
        previous.append(case)
        flag = False

        for i in range(6,0,-1):
            if (case + i) in snakes.keys():
                queue.put((weight + 1 ,(snakes[case+i], previous)))
            elif (case + i) in ladders.keys():
                queue.put((weight + 1 ,(ladders[case+i], previous)))
            elif not flag:
                flag = True
                queue.put((weight + 1 ,(min(100, case + i), previous)))

    print((case, weight, previous))

def main_snakes_and_ladders():
    # example set of snakes and ladders
    snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    # tricky set of snakes and ladders
    # snakes = {37: 21}
    # ladders = {7: 35, 26: 60, 65: 96}
    # empty set of snakes and ladders
    # snakes = {}
    # ladders = {}
    solve_snakes_and_ladders(snakes, ladders)


def solve_smallest_window_contain_all(mot : str):
    letterSet = set([letter for letter in mot])
    smallestWindow = list(letterSet)
    #print(smallestWindow)
    p1 = 0
    p2 = len(mot)
    saved_p1 = p1
    saved_p2 = p2

    tmp = ""
    while True:
        saved_p2 = p2
        p2 -= 1
        for letter in smallestWindow:
            if letter not in mot[p1:p2]:
                p2 += 1
                #print("pas p2", mot[p1:p2])
                break
        
        if saved_p2 == p2:
            break

    while True:
        saved_p1 = p1
        p1 += 1
        for letter in smallestWindow:
            if letter not in mot[p1:p2]:
                p1 -= 1
                #print("pas p1", mot[p1:p2])
                break
        
        if saved_p1 == p1:
            break
 
    print(f"{mot[p1:p2]} , {len(mot[p1:p2])}")
    
def solve_smallest_window_contain_all2(mot : str):
    letterSet = set([letter for letter in mot])
    smallestWindow = list(letterSet)
    print(smallestWindow)
    p1 = 0
    p2 = len(mot)-1
    minLen = len(mot)
    tmp = ""
    secondStep = False
    while p2 < len(mot):
        if not secondStep:
            p2 -= 1
            for letter in smallestWindow:
                if letter not in mot[p1:p2]:
                    p2 += 1
                    print("fin step 1", mot[p1:p2])
                    minLen = min(len(mot[p1:p2]),minLen)
                    tmp = mot[p1:p2]
                    secondStep = True
                    break
        
        else:
            p1 += 1
            for letter in smallestWindow:
                if letter not in mot[p1:p2]:
                    p2 += 1
                    break
            if minLen > len(mot[p1:p2]):
                tmp = mot[p1:p2]
                minLen = len(mot[p1:p2])
        
    return (minLen, tmp)

def main_smallest_window_contain_all():
    # mot = 'jiujitsu'
    mot = 'adeabccddaeabccdeade'
    print(solve_smallest_window_contain_all2(mot[::-1]))


def helper_find_biggest_element(element1, element2):
    for i in range(min(len(element1), len(element2))):
        if int(element1[i]) > int(element2[i]):
            return element1
        elif int(element1[i]) < int(element2[i]):
            return element2
        else:
            return element1 if len(element1) < len(element2) else element2

def solve_largest_possible_integer(elements):

    string_list = [str(number) for number in elements]

    element_max = str(0)
    valren = ""
    for _ in range(len(elements)):
        for element in string_list:
            element_max = helper_find_biggest_element(element, element_max)
        
        valren += element_max
        element_max = 0

    return valren

def main_largest_possible_integer():
    elements = [10, 7, 76, 415]
    print(solve_smallest_window_contain_all(elements))

if __name__ == "__main__":
    pass