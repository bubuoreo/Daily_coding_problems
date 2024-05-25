"""
Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.

There are no transaction costs and you can trade fractional quantitie
"""

import numpy as np

def detect_arbitrage(exchange_rates):
    n = len(exchange_rates)
    log_rates = -np.log(exchange_rates)  # Take the negative logarithm of exchange rates

    # Initialize distances to positive infinity
    distances = [float('inf')] * n
    print(distances)
    distances[0] = 1  # Start with an initial amount of currency
    print(distances)

    # Relax edges repeatedly
    for _ in range(n - 1):
        for source in range(n):
            for dest in range(n):
                if distances[dest] > distances[source] + log_rates[source][dest]:
                    distances[dest] = distances[source] + log_rates[source][dest]

    # Check for negative cycles
    for source in range(n):
        for dest in range(n):
            if distances[dest] > distances[source] + log_rates[source][dest]:
                return True  # Arbitrage opportunity found

    return False  # No arbitrage opportunity found

if __name__ == "__main__":
    # Example exchange rates
    exchange_rates = [
        [1.0, 0.741, 0.657, 1.061],  # USD
        [1.349, 1.0, 0.888, 1.433],   # EUR
        [1.521, 1.126, 1.0, 1.614],   # GBP
        [0.942, 0.698, 0.619, 1.0]    # AUD
    ]

    if detect_arbitrage(exchange_rates):
        print("Arbitrage opportunity detected!")
    else:
        print("No arbitrage opportunity detected.")
