
# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
    
#     *Пример:*
    
#     - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1,


# n = int(input('Введите число: '))

# def get_fibonacci(n):
#     fibo_nums = []
#     a, b = 1, 1
#     for i in range(n-1):
#         fibo_nums.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n):
#         fibo_nums.insert(0, a)
#         a, b = b, a - b
#     return fibo_nums

# fibo_nums = get_fibonacci(n)
# print(get_fibonacci(n))
# print(fibo_nums.index(0))


def fibo(n):
    fibo_list = list()
    fibo_list.append(0)
    fibo_list.append(1)
    
    for i in range(2, n+1):
        fibo_list.append(fibo_list[i - 1] + fibo_list[i - 2])
    
    fibo_list.insert(0, 1)
    fibo_list.insert(0, -1)

    for i in range(0, n-2):
        fibo_list.insert(0, (fibo_list[1]) - (fibo_list[0])) # insert ?
    return fibo_list

x = fibo(10)
print(x)

