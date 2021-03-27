import random

rangeGenerator = lambda start=0, size=10, skip=1: (x for x in range(start, size, skip))
randomGenerator = lambda size=10, min=10, max=100: (x for x in random.sample(range(min, max), size))


def isPrime(n):
    if (n <= 1 or n % 1 > 0):
        return False
    for i in range(2, n // 2):
        if (n % i == 0):
            return False
    return True


def isEven(n):
    return n % 2 == 0


def isOdd(n):
    return n % 2 == 1


def isWhole(n):
    return int(n) == n


def isPositiveInt(n):
    return isWhole(n) and n > 0

def isIn(n,s):
    return n in s

def isNotIn(n,s):
    return n not in s