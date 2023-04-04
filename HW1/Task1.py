# Задача 1. Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все 4 карты – крести.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.


allCardsNum = 52
takenCardsNum = 4
clubsNum = int(allCardsNum / 4) # количество крестей в колоде
acesNum = 4 # количество тузов в колоде
nonacesNum = allCardsNum - acesNum # количество не-тузов в колоде

import comb as c

#------------------a) Найти вероятность того, что все 4 карты – крести.--------------------

# благоприятные исходы
m1 = c.combinations(clubsNum, takenCardsNum) # 715

# все исходы
n = c.combinations(allCardsNum, takenCardsNum) # 270725

result = m1 / n
print(f'Вероятность того, что все 4 карты – крести: {round(result * 100, 2)}%.') # 0.26%


#-----------б) Найти вероятность того, что среди 4-х карт окажется хотя бы один туз.-------------

# благоприятные исходы: среди 4х карт 1 туз ИЛИ 2 туза ИЛИ 3 туза ИЛИ 4 туза (несовместные события)

oneAce = c.combinations(acesNum, 1) * c.combinations(nonacesNum, 3)
twoAce = c.combinations(acesNum, 2) * c.combinations(nonacesNum, 2)
threeAce = c.combinations(acesNum, 3) * c.combinations(nonacesNum, 1)
fourAce = c.combinations(acesNum, 4)
m2 = oneAce + twoAce + threeAce + fourAce # 76145

# все исходы см. решение задания а)

result = m2 / n
print(f'Вероятность того, что среди 4х карт окажется хотя бы один туз: {round(result * 100, 2)}%.') # 28.13%