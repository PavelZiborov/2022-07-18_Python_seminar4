# 1. Задайте строку из набора чисел. Напишите программу,
# которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.


# A = input()
# list = A.split()
# print(list)

# def Find_min_max(list):
#     max = int(list[0])
#     min = int(list[0])
#     try:
#         for i in list:
#             if int(i) > max:
#                 max = int(i)
#         for i in list:
#             if int(i) < min:
#                 min = int(i)
#     except:
#         print('Ошибка. Одно из введенных значений не число.')
#     return min, max

# print(f'Min: {Find_min_max(list)[0]}, Max: {Find_min_max(list)[1]}')



a = input('введите числа через пробел: ')

def num (a):
    f = [int(s) for s in a.split()]
    # f = []
    # for i in a.split():
    #     f.append(int(i))
    print(f)
    print(min(f),max(f))

num(a)