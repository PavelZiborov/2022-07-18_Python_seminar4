# Импортирование модуля двумя способами:
# 1 способ
# import polezno as module
# module.NeedFloatNumber("Введите вещественное число: ")

# 2 способ
from polezno import *
# NeedFloatNumber("Введите вещественное число: ")

# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

#     *Пример:*

#     - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

sp = [0, 3, 5, 9, 3]


def summ(sp):
    sum = 0
    for i in range (0, len(sp) - 1, 2):
        sum = sum + i
    return sum


print(summ(sp))




# ls = [2, 3, 5, 9, 3]
# def ls_sum(a):
#     result = 0
#     for i in range(len(a)):
#         if i % 2 != 0:
#             result += int(a[i])
#     print(result)

# ls_sum(ls)