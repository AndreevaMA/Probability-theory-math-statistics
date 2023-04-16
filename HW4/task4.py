# Рост взрослого населения города X имеет нормальное распределение,
# причем, средний рост равен 174 см, а среднее квадратическое отклонение равно 8 см.
# Посчитайте, какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# 1. больше 182 см? 2. больше 190 см? 3. от 166 см до 190 см? 4. от 166 см до 182 см?
# 5. от 158 см до 190 см? 6. не выше 150 см или не ниже 190 см? 7. не выше 150 см или не ниже 198 см?
# 8. ниже 166 см?

# Задачу можно решить двумя способами: без использования сторонних библиотек (numpy, scipy, pandas и пр.),
# а затем проверить себя с помощью встроенных функций.

from scipy import stats

mu = 174
sigma = 8

# вопрос 1: рост больше 182 см?
x = 182
z = (x - mu) / sigma
print(z) # 1.0
# далее воспользуемся таблицей z
pLeft = 0.84134
pRight = 1 - pLeft
print(f'вопрос 1: {round(pRight * 100, 2)}%') # 15.87%
print(f'проверка 1: {round((1 - stats.norm.cdf(x, loc = mu, scale = sigma)) * 100, 2)}%.') # 15.87%

# вопрос 2: рост больше 190 см?
x = 190
z = (x - mu) / sigma
print(z) # 2.0
# далее воспользуемся таблицей z
pLeft = 0.97725
pRight = 1 - pLeft
print(f'вопрос 2: {round(pRight * 100, 2)}%') # 2.28%
print(f'проверка 2: {round((1 - stats.norm.cdf(x, loc = mu, scale = sigma)) * 100, 2)}%.') # 2.28%

# вопрос 3: рост от 166 см до 190 см?
a = 166
b = 190
za = (a - mu) / sigma
zb = (b - mu) / sigma
print(za, zb) # -1.0, 2.0
# далее воспользуемся таблицей z
pLeftA = 0.15866
pLeftB = 0.97725
p = pLeftB - pLeftA
print(f'вопрос 3: {round(p * 100, 2)}%') # 81.86%
checkA = stats.norm.cdf(a, loc = mu, scale = sigma)
checkB = stats.norm.cdf(b, loc = mu, scale = sigma)
print(f'проверка 3: {round((checkB - checkA) * 100, 2)}%.') # 81.86%

# вопрос 4: рост от 166 см до 182 см?
a = 166
b = 182
za = (a - mu) / sigma
zb = (b - mu) / sigma
print(za, zb) # -1.0, 1.0
# далее воспользуемся таблицей z
pLeftA = 0.15866
pLeftB = 0.84134
p = pLeftB - pLeftA
print(f'вопрос 4: {round(p * 100, 2)}%') # 68.27%
checkA = stats.norm.cdf(a, loc = mu, scale = sigma)
checkB = stats.norm.cdf(b, loc = mu, scale = sigma)
print(f'проверка 4: {round((checkB - checkA) * 100, 2)}%.') # 68.27%

# вопрос 5: рост от 158 см до 190 см?
a = 158
b = 190
za = (a - mu) / sigma
zb = (b - mu) / sigma
print(za, zb) # -2.0, 2.0
# далее воспользуемся таблицей z
pLeftA = 0.02275
pLeftB = 0.97725
p = pLeftB - pLeftA
print(f'вопрос 5: {round(p * 100, 2)}%') # 95.45%
checkA = stats.norm.cdf(a, loc = mu, scale = sigma)
checkB = stats.norm.cdf(b, loc = mu, scale = sigma)
print(f'проверка 5: {round((checkB - checkA) * 100, 2)}%.') # 95.45%

# вопрос 6: рост не выше 150 см или не ниже 190 см?
a = 150
b = 190
za = (a - mu) / sigma
zb = (b - mu) / sigma
print(za, zb) # -3.0, 2.0
# далее воспользуемся таблицей z
pLeftA = 0.00135
pLeftB = 0.97725
pRightB = 1 - pLeftB
p = pLeftA + pRightB
print(f'вопрос 6: {round(p * 100, 2)}%') # 2.41%
checkA = stats.norm.cdf(a, loc = mu, scale = sigma)
checkB = 1 - stats.norm.cdf(b, loc = mu, scale = sigma)
print(f'проверка 6: {round((checkA + checkB) * 100, 2)}%.') # 2.41%

# вопрос 7: рост не выше 150 см или не ниже 198 см?
a = 150
b = 198
za = (a - mu) / sigma
zb = (b - mu) / sigma
print(za, zb) # -3.0, 3.0
# далее воспользуемся таблицей z
pLeftA = 0.00135
pLeftB = 0.99865
pRightB = 1 - pLeftB
p = pLeftA + pRightB
print(f'вопрос 6: {round(p * 100, 2)}%') # 0.27%
checkA = stats.norm.cdf(a, loc = mu, scale = sigma)
checkB = 1 - stats.norm.cdf(b, loc = mu, scale = sigma)
print(f'проверка 6: {round((checkA + checkB) * 100, 2)}%.') # 0.27%

# вопрос 8: рост ниже 166 см?
x = 166
z = (x - mu) / sigma
print(z) # -1.0
# далее воспользуемся таблицей z
pLeft = 0.15866
print(f'вопрос 8: {round(pLeft * 100, 2)}%') # 15.87%
print(f'проверка 8: {round(stats.norm.cdf(x, loc = mu, scale = sigma) * 100, 2)}%.') # 15.87%