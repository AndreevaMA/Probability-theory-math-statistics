# Определить сочетания, размещения или перестановки используются для решения этой задачи.
# Сколькими способами можно выбрать из колоды, состоящей из 36 карт, 4 карты?

from math import factorial

def combinations(n, k):
    # где n - количество элементов в множестве, k - количество элементов в комбинации
    return factorial(n) // (factorial(k) * factorial(n - k)) # // - целочисленное деление

def main():
    n = int(input('Введите n: '))
    k = int(input('Введите k: '))
    
    result = combinations(n, k)
    print(f'Результат: {result}.')

if __name__ == "__main__":
    main()