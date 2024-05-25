"""
Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.
"""

import random

def toss_biased(p):
    random_value = random.random()
    if(random_value > p):
        return 0
    else:
        return 1

def toss_unbiased():
    while True:
        # Effectuez deux lancers biaisés
        toss1 = toss_biased(biased_probability)
        toss2 = toss_biased(biased_probability)

        # Si les lancers sont différents, retournez le premier lancer
        if toss1 != toss2:
            return toss1

if __name__ == "__main__":
    biased_probability = 0.27
    results = []
    for i in range(100000):
        results.append(toss_unbiased())
    proba = sum(results) / len(results)
    print(proba)