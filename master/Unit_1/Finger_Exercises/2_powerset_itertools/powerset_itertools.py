from itertools import chain, combinations

def powerset(items):
    tools = chain.from_iterable(combinations(items, r) for r in range(len(items)+1))

    for answer in tools:
        yield answer

"""
Code used for running.  Do not include when submitting to grader.
"""
my_list = [1, 2, 3, 4]
my_powerset = powerset(my_list)

for i in range(500):
    print(my_powerset.__next__())
