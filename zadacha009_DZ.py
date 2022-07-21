# Вычислить результат деления двух чисел c заданной точностью d

# Пример:
# - при $d = 0.001, π = 3.141.$
# при этом 0.0000000001 <= d <= 0.1

import math

print('Введите заданную точность (0.0000000001 <= d <= 0.1): ')
D = float(input())
number = math.pi


def Otsechenie(number, D):
    if 0.0000000001 <= D <= 0.1:
        count = len(str(D).split('.')[1])
        short_number = int((number * 10**count)) / 10**count
        return short_number
    else:
        print('Число должно быть от 0.0000000001 до 0.1')
        return number


print(number)
print(Otsechenie(number, D))
