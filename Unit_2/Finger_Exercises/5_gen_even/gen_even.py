import random

def genEven():
    """
    Returns a random number x, where 0 <= x <= 100
    """
    all_evens = range(0, 100, 2)
    return random.choice(all_evens)

"""
Used for running.  Do not include when submitting to the grader.
"""
print(genEven())
"""
End Runner Code.
"""
