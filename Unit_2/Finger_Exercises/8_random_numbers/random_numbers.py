import random

"""
Problem 1
"""

random.seed(9001)
for i in range(random.randint(1, 10)):
    print(random.randint(1, 10))

"""
Problem 2
"""
random.seed(9001)
d = random.randint(1, 10)
for i in range(random.randint(1, 10)):
    print(d)

"""
Problem 3
"""
random.seed(9001)
d = random.randint(1, 10)
for i in range(random.randint(1, 10)):
    if random.randint(1, 10) < 7:
        print(d)
    else:
        random.seed(9001)
        d = random.randint(1, 10)
        print(random.randint(1, 10))
