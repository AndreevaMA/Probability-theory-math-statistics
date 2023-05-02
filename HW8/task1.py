# Даны значения величины заработной платы заемщиков банка (zp)
# и значения их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Найдите ковариацию этих двух величин с помощью элементарных действий,
# а затем с помощью функции cov из numpy.
# Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков,
# а затем с использованием функций из библиотек numpy и pandas.

import numpy as np

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])


#------------------------------------------КОВАРИАЦИЯ------------------------------------------

cov1 = np.mean(zp * ks) - np.mean(zp) * np.mean(ks)
print(cov1) # 9157.84 - смещённая ковариация

cov2 = np.cov(zp, ks, ddof = 0)
print(cov2) # [[3494.64 9157.84] [9157.84 30468.89]]
# ковариация равна 9157.84 - смещённая ковариация

# cov1 = cov2, расчёт верный

cov3 = np.cov(zp, ks, ddof = 1)
print(cov3) # [[3882.93333333 10175.37777778] [10175.37777778 33854.32222222]]
# ковариация равна 10175.38 - несмещённая ковариация


#--------------------------------коэффициент корреляции Пирсона--------------------------------

# r = cov / (sigmax * sigmay)

# смещённая ковариация при смещённом сигма
# S^2 = ∑((i = от 1 до m) (xi − Х ̅ )^2)) / m

def findVar(array):
    sum = 0
    for i in range(len(array)):
        sum += (array[i] - np.mean(array))**2
    return sum / len(array)

varx = findVar(zp)
vary = findVar(ks)
sigmax = np.sqrt(varx)
sigmay = np.sqrt(vary)
pearson1 = cov1 / (sigmax * sigmay) # cov1 уже посчитана выше
print(pearson1) # 0.8874900920739158

# перепроверка
checkPearson1 = 9157.84 / (np.std(zp, ddof = 0) * np.std(ks, ddof = 0)) # cov уже посчитана выше
print(checkPearson1) # 0.8874900920739162

# несмещённая ковариация при несмещённом сигма
# S^2 = ∑((i = от 1 до n) (xi − Х ̅ )^2)) / (n - 1)

def findVarNesm(array):
    sum = 0
    for i in range(len(array)):
        sum += (array[i] - np.mean(array))**2
    return sum / (len(array) - 1)

varx = findVarNesm(zp)
vary = findVarNesm(ks)
sigmax = np.sqrt(varx)
sigmay = np.sqrt(vary)
pearson2 = 10175.38 / (sigmax * sigmay) # cov уже посчитана выше
print(pearson2) # 0.8874902858947499

# перепроверка
checkPearson2 = 10175.38 / (np.std(zp, ddof = 1) * np.std(ks, ddof = 1)) # cov уже посчитана выше
print(checkPearson2) # 0.8874902858947499