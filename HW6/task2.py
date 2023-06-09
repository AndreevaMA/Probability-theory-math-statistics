# В результате 10 независимых измерений некоторой величины X, выполненных с одинаковой точностью,
# получены опытные данные: 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
# Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей,
# оценить истинное значение величины X при помощи доверительного интервала,
# покрывающего это значение с доверительной вероятностью 0,95.

import numpy as np

test_result = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])

average = np.mean(test_result) # 6.59
alpha = 0.05
n = len(test_result) # 10

# нам неизвестна дисперсия ген. совокупности, поэтому используем t-критерий: Х ̅  +- t [α/2] * (σ / √n)
# где σ вычисляется по выборке как несмещённое СКО

sigma = np.std(test_result, ddof = 1) # 0.4508017549014448

from scipy import stats

x1 = average + stats.t.ppf(alpha / 2, df = n - 1) * (sigma / np.sqrt(n))
x2 = average - stats.t.ppf(alpha / 2, df = n - 1) * (sigma / np.sqrt(n))

print(f'p({round(x1, 2)} < mu < {round(x2, 2)}) = 95%')
# p(6.27 < mu < 6.91) = 95%