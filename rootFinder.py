def is_prime(x):
    return all(x % i for i in primeFactors)

def next_prime(x):
    return min([a for a in range(x+1, 2*x) if is_prime(a)])

if __name__ == "__main__":
    entry = 57942544
    primeFactors = [2]

    factors = {}
    factorIndex = 0
    while (entry > 1):
        print("entry = ", entry)
        print("factor = ", primeFactors[factorIndex])
        if (entry % primeFactors[factorIndex] == 0):
            if primeFactors[factorIndex] in factors:
                factors[primeFactors[factorIndex]] += 1
            else:
                factors[primeFactors[factorIndex]] = 1
            
            entry /= primeFactors[factorIndex]
            factorIndex = 0
        else:
            if factorIndex == (len(primeFactors) - 1):
                primeFactors.append(next_prime(primeFactors[-1]))
            factorIndex += 1
    
    result = 1

    print(factors)
    for key, value in factors.items():
        result *= key**(value/2)
    print(int(result))
