# Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175

# Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.

import numpy as np

daughter = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
mother = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])

# для разности средних арифметических используем формулу: delta +- t [α/2] * Sdelta,

average1 = np.mean(daughter)
average2 = np.mean(mother)
delta = average2 - average1 # 1.9

# стандартная ошибка для средних арифметических Sdelta = √ ( (D / n1) + (D / n2) ),
# где D = (D1 + D2) / 2 - ср. арифметическое дисперсий двух выборок D1 и D2

n1 = len(daughter)
n2 = len(mother)
sigma1 = np.std(daughter, ddof = 1)
sigma2 = np.std(mother, ddof = 1)
d1 = sigma1 * sigma1
d2 = sigma2 * sigma2
d = (d1 + d2) / 2
sDelta = np.sqrt(d / n1 + d / n2) # 3.888015775002291

# строим интервал с учётом, что степени свободы для критерия Стьюдента: df = 2 * (n - 1),
# где n - объём выборки (две выборки -> 2*(n-1))

from scipy import stats

alpha = 0.05
x1 = delta + stats.t.ppf(alpha / 2, df = 2 * (n1 - 1)) * sDelta
x2 = delta - stats.t.ppf(alpha / 2, df = 2 * (n1 - 1)) * sDelta
print(round(x1, 3), round(x2, 3)) # -6.268 10.068