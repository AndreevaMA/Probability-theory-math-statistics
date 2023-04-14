

from math import factorial

def combinations(n, k):
    # где n - количество элементов в множестве, k - количество элементов в комбинации
    return factorial(n) // (factorial(k) * factorial(n - k)) # // - целочисленное деление