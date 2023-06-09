# Посчитать коэффициент линейной регрессии при заработной плате (zp),
# используя градиентный спуск (без intercept).

import numpy as np

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110]) # независимая переменная х
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832]) # зависимая переменная y

n = len(zp) # 10

# функция потерь
def mse(B1, y = ks, x = zp, n = 10):
    return np.sum((y - B1 * x)**2) / n

# скорость обучения
alpha = 0.000001

B1 = 0.1 # для модели без интерсепта определяем стартовое значение только для β1

# 3000 итераций с выводом каждой 500й итерации + mse
for i in range(3000):
    B1 -= alpha * (2/n) * np.sum((B1 * zp - ks) * zp)
    if i % 500 == 0:
        print(f'Iteration = {i}, B1 = {B1}, mse = {mse(B1)}')

# Iteration = 0, B1 = 0.25952808, mse = 493237.7212546963
# Iteration = 500, B1 = 5.889815595583751, mse = 56516.858416040064 
# Iteration = 1000, B1 = 5.8898204201285544, mse = 56516.85841571941
# Iteration = 1500, B1 = 5.889820420132673, mse = 56516.85841571943
# Iteration = 2000, B1 = 5.889820420132673, mse = 56516.85841571943
# Iteration = 2500, B1 = 5.889820420132673, mse = 56516.85841571943

# B1 и mse прекращают изменения на 1500-й итерации
# получили модель: ks = 5.8898 * zp

# проверка:
checkIt = mse(5.8898)
print(checkIt) # 56516.858421464