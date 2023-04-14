# Даны значения зарплат из выборки выпускников:
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean)
# среднее арифметическое, среднее квадратичное отклонение,
# смещенную и несмещенную оценки дисперсий для данной выборки.

import numpy as np

salaryData = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])

# среднее арифметическое
def dataAverage(array):
    arrayLen = array.shape[0]
    arraySum = 0
    for i in range(arrayLen):
        arraySum = arraySum + array[i]
    arrayAverage = arraySum / arrayLen
    return arrayAverage

# несмещённая оценка дисперсии
def dataVarianceUn(array):
    n = array.shape[0]
    sumVar = 0
    dataAvg = dataAverage(array)
    for i in range(n):
        sumVar = sumVar + pow((array[i] - dataAvg), 2)
    dataVar = sumVar / (n - 1)
    return dataVar

# смещённая оценка дисперсии
def dataVariance(array):
    n = array.shape[0]
    sumVar = 0
    dataAvg = dataAverage(array)
    for i in range(n):
        sumVar = sumVar + pow((array[i] - dataAvg), 2)
    dataVar = sumVar / n
    return dataVar

# СКО (в основе - несмещённая оценка дисперсии)
def dataSigmaUn(array):
    import math
    dataS = math.sqrt(dataVarianceUn(array))
    return dataS

a = dataAverage(salaryData)
b = dataVarianceUn(salaryData)
c = dataVariance(salaryData)
d = dataSigmaUn(salaryData)

print(f'Cреднее арифметическое зарплат выпускников равно {a}.') # 65.3
print(f'Несмещённая оценка дисперсии равна {b}.') # 1000.1157894736842
print(f'Смещённая оценка дисперсии равна {c}.') # 950.11
print(f'Cреднее квадратичное отклонение равно {d}.') # 31.624607341019814


# кросс-чек с помощью библиотеки numpy
a1 = np.mean(salaryData) # 65.3
b1 = np.var(salaryData, ddof = 1) # 1000.1157894736842
c1 = np.var(salaryData, ddof = 0) # 950.11
d1 = np.std(salaryData, ddof = 1) # 31.624607341019814
print(a1, b1, c1, d1)