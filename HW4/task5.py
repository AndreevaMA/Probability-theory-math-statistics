# На сколько сигм (средних квадратичных отклонений) отклоняется рост человека, равный 190 см,
# от математического ожидания роста в популяции, в которой M(X) = 178 см и D(X) = 25 кв.см?

x = 190
mu = 178
var = 25
sigma = 5 # √ var

dist = abs((x - mu) / sigma)
print(dist) # 2.4