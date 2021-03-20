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
