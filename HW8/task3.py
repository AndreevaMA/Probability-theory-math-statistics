# Известно, что рост футболистов в сборной распределен нормально
# с дисперсией генеральной совокупности, равной 25 кв.см.
# Объем выборки равен 27, среднее выборочное составляет 174.2.
# Найдите доверительный интервал для математического ожидания с надёжностью 0.95.

# нам известна дисперсия ген. совокупности, поэтому используем z-критерий: Х ̅  +- z [α/2] * (σ / √n)

from math import sqrt

average = 174.2
alpha = 0.05
var = 25
sigma = sqrt(var)
n = 27

from scipy import stats

x1 = average + stats.norm.ppf(alpha / 2) * (sigma / sqrt(n))
x2 = average - stats.norm.ppf(alpha / 2) * (sigma / sqrt(n))

print(f'p({round(x1, 2)} < mu < {round(x2, 2)}) = 95%')
# p(172.31 < mu < 176.09) = 95%