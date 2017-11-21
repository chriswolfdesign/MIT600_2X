def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if L == []:
        return float("NaN")

    mean = 0
    for item in L:
        mean += len(item)
    mean = mean / float(len(L))

    total = 0.0

    for item in L:
        total += (len(item) - mean)**2

    return (total / len(L))**0.5

"""
Used for running, do not include when submitting to the grader.
"""
list1 = ["a", "z", "p"]
print("Test 1 [a, z, p] =", stdDevOfLengths(list1))
print()

list2 = ["apples", "oranges", "kiwis", "pineapples"]
print("Test 2 [apples, oranges, kiwis, pineapples] =", stdDevOfLengths(list2))
