# Задача 3. В ящике имеется 15 деталей, из которых 9 окрашены.
# Рабочий случайным образом извлекает 3 детали.
# Какова вероятность того, что все 3 извлеченные детали окрашены?

allDetailsNum = 15
coloredNum = 9
noncoloredNum = allDetailsNum - coloredNum
takenNum = 3

import comb as c

# благоприятные исходы
m = c.combinations(coloredNum, takenNum) # 84

# все исходы
n = c.combinations(allDetailsNum, takenNum) # 455

result = m / n
print(f'Вероятность того, что все 3 извлеченные детали окрашены: {round(result * 100, 2)}%.') # 18.46%