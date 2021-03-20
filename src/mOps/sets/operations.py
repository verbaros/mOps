from itertools import chain, combinations

def union(*args, sort=True):
    if all([hasattr(a, '__iter__') for a in args]):
        result = []
        [result.extend(s) for s in args]
        if (sort):
            result.sort()
        result = list(set(result))
        return result
    else:
        raise TypeError('Set must be iterable')


U = union


def intersection(*args):
    if all([hasattr(a, '__iter__') for a in args]):
        result = list(set.intersection(*map(set, args)))
        result.sort()
        return result
    else:
        raise TypeError('Set must be iterable')


I = intersection


def set_diffrence(a, b, sort=True):
    intr = I(a, b)
    result = []
    [ai if ai in intr else result.append(ai) for ai in a]
    if (sort):
        result.sort()
    return result


SetD = set_diffrence


def symmetric_diffrence(a, b, sort=True):
    intr = I(a, b)
    result = []
    [ai if ai in intr else result.append(ai) for ai in union(a, b)]
    if (sort):
        result.sort()
    return result


SymD = symmetric_diffrence


def cartesian_product(a, b):
    if all([hasattr(a, '__iter__') for a in [a, b]]):
        result = [(ax, bx) for bx in b for ax in a]
        return result
    else:
        raise TypeError('Set must be iterable')


CarP = cartesian_product


def power_set(a, sort=True):
    if (hasattr(a, '__iter__')):
        result = list(chain.from_iterable(combinations(a, r) for r in range(len(a)+1)))
        result = [list(elem) for elem in result]
        if (sort):
            result.sort()
        return result
    else:
        raise TypeError('Set must be iterable')


PwrS = power_set
