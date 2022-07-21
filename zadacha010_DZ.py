# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

def NeedIntNumber(text):  # Функция, которая принимает на вход целое число
    print(text)
    needTrue = False
    while needTrue == False:
        try:
            number = input()
            number = int(number)
            if number >1:
                needTrue = True
                return number
            else: print('Ошибка ввода. Число должно быть > 1. ')
        except:
            print('Ошибка ввода. Введите целое число: ')


def PrimeFactors (N): # Функция, которая раскладывает натуральное число на простые множители
    count = 2
    primefactors = []
    while N != 1:
        if N%count == 0:
            primefactors.append(count)
            N = N / count
        else:
            count += 1
    return primefactors


N = NeedIntNumber('Введите целое число > 1:')
print()
print(f'Простые множители числа {N}:\n{PrimeFactors(N)}')