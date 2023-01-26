"""
Plot histogram for the winnings of simulating a game n amount of times.
A player starts with $100 and plays the game 600 times.
Playing the game costs $1 and if a player wins the game, they get $10.
Feel free to change these numbers.

For more effective use, instead of the function game, use np.random.randint(start, end + 1, [iterations, 1]) and
define wins from np.count_nonzero((favourable outcome == x))

"""

import random
import numpy as np
from matplotlib import pyplot as plt

# constants
money = 100  # $

iterations = 600


def game():
    dice = random.randint(1, 12)
    if dice != 6:
        return 0
    else:
        return 10


def simulation(cash=100, times=600):
    for i in range(times):
        cash -= 1
        cash += game()
    return cash


# iterates our simulation n times
def probability(n, cash, times):
    sims, rets = n, [None]*n
    print(len(rets), n)
    for i in range(sims):
        rets[i] = simulation(cash, times)

    return rets


# gives frequency of our probability function
def frequency(given, lst, n):
    # return amount of iterations of given number
    # divided by number of total iterations
    return lst.count(given)


def final(cash, times, n):
    sim = probability(n, cash, times)
    # tmp is placeholder for better func
    tmp = np.linspace(-300, 300, 600)
    for i in range(len(tmp)):
        tmp[i] = frequency(i-300, sim, n)

    return tmp



n = 10_000
y = final(money, iterations, n)

x = np.linspace(-300, 300, 600)
# plt.plot(x, y)
plt.bar(x, height=y/n, width=10.0)

plt.show()

