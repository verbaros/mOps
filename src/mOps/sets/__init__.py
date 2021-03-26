import random
from mOps.sets.operations import *
from mOps.sets.core import Set

EmptySet = []


def new_set(size, f=0, c=10, repeat=False, sort=True):
    result = []

    if (f > c):
        raise ValueError(f'f{f} > c{c}')

    if (not repeat and size > (c - f)):
        raise IndexError('Not enough elements for set')



    while (len(result) < size):
        if (repeat):
            result.append(random.randint(f, c))
        else:
            n = random.randint(f, c)
            if n not in result:
                result.append(n)
    if (sort):
        result.sort()

    return result

def new_set2(size, f=0, c=10, repeat=False, sort=True):

    if (f > c):
        raise ValueError(f'f{f} > c{c}')

    if (not repeat and size > (c - f)):
        raise IndexError('Not enough elements for set')

    if (repeat):
        result = random.sample(range(f, c), size)
    else:
        result = set()
        while (len(result) < size):
            result.add(random.randint(f, c))
        result = list(result)

    if (sort):
        result.sort()

    return result

