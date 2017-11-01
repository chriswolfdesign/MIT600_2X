import random

def stochasticNumber():
    """
    Stochastically generates and returns a uniformly distributed even number
    between 9 and 21.
    """
    numbers = range(10, 21, 2)
    return random.choice(numbers)

print(stochasticNumber())
