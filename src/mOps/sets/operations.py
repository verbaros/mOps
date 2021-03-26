from mOps.sets.core import Set
from itertools import chain, combinations

def union(inSet, *args):
    result = inSet.copy()
    for s in args:
        result.extend(s)
    return result

U = union


def intersection(inSet,*args):
    result = set(inSet.copy())
    for s in args:
        result = result.intersection(s)
    return Set(*result)


I = intersection


def set_diffrence(a, b):
    return Set(*set(a.items()).difference(b.items()))



SetD = set_diffrence


def symmetric_diffrence(a, b):
    return Set(*set(a.items()).symmetric_difference(b.items()))


SymD = symmetric_diffrence


def cartesian_product(a, b):
    return Set(*[(ax, bx) for bx in b for ax in a])


CarP = cartesian_product


def power_set(a, sort=False):
    result = list(chain.from_iterable(combinations(a, r) for r in range(len(a) + 1)))
    return Set(*[Set(elem) for elem in result])


PwrS = power_set
