def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list
        of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            if (i // (3**j)) % 3 == 1:
                bag1.append(items[j])
            elif (i // (3**j)) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)

"""
Used for running, do not include when submitting to grader.
"""
items = [1, 2, 3, 4]
foo = yieldAllCombos(items)
for i in range(500):
    print(foo.__next__())

"""
End Runner Code
"""
