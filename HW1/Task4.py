# Задача 4. В лотерее 100 билетов. Из них 2 выигрышных.
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

totalNum = 100
winNum = 2
nonwinNum = totalNum - winNum
purchasedNum = 2

import comb as c

# благоприятные исходы
m = c.combinations(winNum, purchasedNum) # 1

# все исходы
n = c.combinations(totalNum, purchasedNum) # 4950

result = m / n
print(f'Вероятность того, что 2 приобретённых билета окажутся выигрышными: {round(result * 100, 2)}%.') # 0.02%