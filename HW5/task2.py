# Проведите тест гипотезы. Утверждается, что шарики для подшипников,
# изготовленные автоматическим станком, имеют средний диаметр 17 мм.
# Используя односторонний критерий с α = 0.05, проверить эту гипотезу, если в выборке из n = 100 шариков
# средний диаметр оказался равным 17.5 мм, а дисперсия известна и равна 4 кв. мм.

# 1. Определим H0 и H1
# H0: средний диаметр подшипников равен 17 мм, mu = mu0
# H1: средний диаметр подшипников больше 17 мм, mu > mu0

# 2. Уровень статистической значимости α равен 5% по условию задачи

alpha = 0.05

# 3. Выбор статистического критерия
# У нас одновыборочный тест: есть генеральная совокупность с известной дисперсией и выборка.
# Поэтому здесь используем z-критерий.

# 4. Расчёт наблюдаемого z-критерия для выборки: (X ̅ − μ) / (σ / √n)

from math import sqrt

average = 17.5
mu = 17
var = 4
sigma = sqrt(var)
n = 100
z_emp = (average - mu) / (sigma / sqrt(n)) # 2.5

# 5. Находим z-критическое

# У нас правосторонний тест: ищем квантиль 1-α (95%)
# По таблице получается примерно 1.645
# Перепроверка с помощью функции:
from scipy import stats
z_table = stats.norm.ppf(1 - alpha) # 1.6448536269514729

# Сравниваем наблюдаемое и табличное (критическое) и делаем вывод

# z_emp > z_table, попадание в критическую область
# Вывод: отвергаем нулевую гипотезу; средний диаметр подшипников больше 17 мм с вероятностью ошибки 5%