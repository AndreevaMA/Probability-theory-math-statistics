# Проведите двусторонний тест гипотезы.
# Продавец утверждает, что средний вес пачки печенья составляет 200 г.
# Из партии извлечена выборка из 10 пачек.
# Вес каждой пачки составляет: 202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
# Известно, что их веса распределены нормально.
# Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна 99%?

import numpy as np

x = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])

# 1. Определим H0 и H1, тест по условию задачи двусторонний
# H0: средний вес пачки печенья составляет 200 г, mu = mu0
# H1: средний вес пачки печенья не равен 200 г, mu != mu0

# 2. Определим уровень статистической значимости α, по условию задачи доверительная вероятность равна 99%

alpha = 0.01

# 3. Выбор статистического критерия
# У нас одновыборочный тест: дисперсия генеральной совокупности неизвестна.
# Поэтому здесь используем t-критерий.

# 4. Расчёт наблюдаемого t-критерия для одной выборки: (X ̅ − μ) / (σнабл / √n)

average = np.mean(x) # 198.5
mu0 = 200
sigma = np.std(x, ddof = 1) # 4.453463071962462
size = len(x) # 10
t_emp = (average - mu0) / (sigma / np.sqrt(size)) # -1.0651074037450896

# 5. Находим t-критическое

# У нас двусторонний тест: ищем квантиль α/2 и (1-α)/2 (0.5% и 49.5%)
# Число степеней свободы = 18
# По таблице получается примерно -2.88 и 2.88
# Перепроверка с помощью функции:
from scipy import stats
t1 = stats.t.ppf(alpha / 2, df = 2 * (size - 1)) # -2.8784404727135864
t2 = stats.t.ppf(1 - alpha / 2, df = 2 * (size - 1)) # 2.878440472713585

# Сравниваем наблюдаемое и табличное (критическое) и делаем вывод

# t1 < t_emp < t2, попадание в область нулевой гипотезы H0
# Вывод: принимаем нулевую гипотезу; средний вес пачки печенья составляет 200 г с вероятностью ошибки 1%