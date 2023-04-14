# В первом ящике находится 8 мячей, из которых 5 - белые.
# Во втором ящике - 12 мячей, из которых 5 белых.
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4 мяча.
# Какова вероятность того, что 3 мяча белые?

balls1 = 8
white1 = 5
others1 = balls1 - white1

balls2 = 12
white2 = 5
others2 = balls2 - white2

choice1 = 2
choice2 = 4

# в данном случае понимаю вопрос задачи, как "ровно три мяча белые"

import comb as c

# благоприятные исходы: 0 и 3 ИЛИ 1 и 2 ИЛИ 2 и 1
m11 = c.combinations(white1, 0) * c.combinations(others1, 2) # 0 из 1й: 3
m12 = c.combinations(white1, 1) * c.combinations(others1, 1) # 1 из 1й: 15
m13 = c.combinations(white1, 2) * c.combinations(others1, 0) # 2 из 1й: 10
m21 = c.combinations(white2, 3) * c.combinations(others2, 1) # 3 из 2й: 70
m22 = c.combinations(white2, 2) * c.combinations(others2, 2) # 2 из 2й: 210
m23 = c.combinations(white2, 1) * c.combinations(others2, 3) # 1 из 2й: 175
print(m11, m12, m13, m21, m22, m23)

# все исходы
n1 = c.combinations(balls1, choice1) # 28
n2 = c.combinations(balls2, choice2) # 495
print(n1, n2)

result1 = (m11 / n1) * (m21 / n2) # 0 из 1й и 3 из 2й
result2 = (m12 / n1) * (m22 / n2) # 1 из 1й и 2 из 2й
result3 = (m13 / n1) * (m23 / n2) # 2 из 1й и 1 из 2й
result = result1 + result2 + result3

print(f'Вероятность того, что 3 мяча белые, равна {round(result * 100, 2)}%.') # 36.87%