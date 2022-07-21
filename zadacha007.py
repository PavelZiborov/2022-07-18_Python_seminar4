# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

#     1) с помощью математических формул нахождения корней квадратного уравнения
#     2) с помощью дополнительных библиотек Python

import math
from polezno import *

A = NeedFloatNumber('Введите число А: ')
B = NeedFloatNumber('Введите число B: ')
C = NeedFloatNumber('Введите число C: ')


def Find_x1_x2(A, B, C):
    D = B ** 2 - 4 * A * C
    print(f'Дискриминант D = {D}')
    if D > 0:
        x1 = ((-B) - math.sqrt(D)) / (2 * A)
        x2 = ((-B) + math.sqrt(D)) / (2 * A)
    elif D == 0:
        x1 = x1 = (-B / (2 * A))
    else:
        x1 = x2 = None
    return x1, x2

x1 = Find_x1_x2(A, B, C)[0]
x2 = Find_x1_x2(A, B, C)[1]

print(f'x1 = {x1}, x2 = {x2}')