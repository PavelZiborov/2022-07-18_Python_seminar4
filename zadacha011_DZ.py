# 3. Напишите программу, которая принимает на стандартный вход список
# игр футбольных команд с результатом матча и выводит на стандартный
# вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Первая_команда; Забито_первой_командой; Вторая_команда; Забито_второй_командой

# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков

# Конкретный пример ввода-вывода приведён ниже.

# Порядок вывода команд произвольный.

# Sample Input:

# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15

# Sample Output:

# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6



inputResults = [['Спартак', 9, 'Зенит', 10], ['Локомотив', 12, 'Зенит', 3], ['Спартак', 8, 'Локомотив', 15]]

# N = int(input('Введите число завершенных игр: '))
# def InputResults(N):                                         # Функция ввода данных
#     results = []
#     for i in range (0, N):
#         results.append(input().replace(' ', '').split(';'))
#         results[i][1] = int(results[i][1])
#         results[i][3] = int(results[i][3])
#     return results


# def OutputResults(inputResults):

#     for item in inputResults:
#         count(item)

# inputResults = InputResults(N)
print('Исходные данные: ')
print(inputResults)

# формирование общего списка
ObshiySpisok = []
for i in range(0, len(inputResults)):
    for j in range (0, len(inputResults[i])):
        ObshiySpisok.append(inputResults[i][j])
print('Общий список: ')
print(ObshiySpisok)

# Формирование уникального списка
UnikalniyObshiySpisok = set(ObshiySpisok)

# Формирование команд и "игр всего сыграно"
komandy = []
igry_vsego = []
for i in UnikalniyObshiySpisok:
    if type(i) == str:
        komandy.append(i)
        igry_vsego.append(ObshiySpisok.count(i))

# Подсчет побед
ochkov_vsego = []
ochkov_vsego_temp = []
for j in komandy:
    for i in range(0, len(ObshiySpisok) - 1):
        if ObshiySpisok[i] == j:
            ochkov_vsego_temp.append(ObshiySpisok[i+1])
ochkov_vsego = [ochkov_vsego_temp[i] + ochkov_vsego_temp[i+1] for i in range(0, len(ochkov_vsego_temp)-1) if i%2 == 0] 



pobedy = []
for i in komandy:
    




print('Команды: ')
print(komandy)
print('Всего игр: ')
print(igry_vsego)
print('Очков всего: ')
print(ochkov_vsego)

# print(UnikalniyObshiySpisok)
