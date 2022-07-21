# 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

#     *Пример:*

#     - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

sp = [1.1, 1.2, 3.1, 5, 10.01]


def dif_max_min(sp):
    max = sp[0]
    min = sp[0]
    for i in sp:
        if (i*10) % 10 > max:
            max = i
        if ((i*10) % 10 < min) and (((i*10) % 10) != 0):
            min = i
    max_dr = (max*10) % 10
    min_dr = (min*10) % 10
    return max_dr, min_dr


print(dif_max_min(sp))
max = dif_max_min(sp)[0]
min = dif_max_min(sp)[1]
dif = max - min
print(round(dif, 2))


a = [1.1, 1.2, 3.1, 5.10, 10.01]


# def MaxMin(list):
#     for i in range(len(list)):
#         list[i] = (list[i] % 1)
#     Result = round(max(list)- (min(list), 3))
#     return f'Разница между остатком дробей {round(max(list),3)} и {round(min(list),3)} = {Result}'


# print(MaxMin(a))
