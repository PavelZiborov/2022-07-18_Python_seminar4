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


# Функция ввода данных
def InputResults(N):
    results = []
    for i in range(0, N):
        results.append(input().replace(' ', '').split(';'))
        results[i][1] = int(results[i][1])
        results[i][3] = int(results[i][3])
    return results


# Функция подсчета "Всего_игр Побед Ничьих Поражений Всего_очков"
def OutputResults(inputResults):

    # формирование общего списка
    ObshiySpisok = []
    for i in range(0, len(inputResults)):
        for j in range(0, len(inputResults[i])):
            ObshiySpisok.append(inputResults[i][j])

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
    pobedy = []
    for i in komandy:
        count = 0
        for x in range(0, len(inputResults)):
            if (inputResults[x][2] == i) and (inputResults[x][3] > inputResults[x][1]):
                count = count + 1
            elif (inputResults[x][0] == i) and (inputResults[x][1] > inputResults[x][3]):
                count = count + 1
            else:
                continue
        pobedy.append(count)

    # Подсчет ничьих
    nichya = []
    for i in komandy:
        count = 0
        for x in range(0, len(inputResults)):
            if (inputResults[x][2] == i) and (inputResults[x][3] == inputResults[x][1]):
                count = count + 1
            elif (inputResults[x][0] == i) and (inputResults[x][1] == inputResults[x][3]):
                count = count + 1
            else:
                continue
        nichya.append(count)

    # Подсчет поражений
    porazheniya = []
    for i in komandy:
        count = 0
        for x in range(0, len(inputResults)):
            if (inputResults[x][2] == i) and (inputResults[x][3] < inputResults[x][1]):
                count = count + 1
            elif (inputResults[x][0] == i) and (inputResults[x][1] < inputResults[x][3]):
                count = count + 1
            else:
                continue
        porazheniya.append(count)

    # подсчет очков
    ochki = []
    for i in range(0, len(komandy)):
        ochki.append(pobedy[i] * 3 + nichya[i] * 1)

    return komandy, igry_vsego, pobedy, nichya, porazheniya, ochki


# Функция вывода данных на экран
def PrintOutputResults(results):
    for k in range(0, len(results[0])):
        print(
            f'{results[0][k]} {results[1][k]} {results[2][k]} {results[3][k]} {results[4][k]} {results[5][k]}')



# inputResults = [['Спартак', 9, 'Зенит', 10], ['Локомотив', 12, 'Зенит', 3], ['Спартак', 8, 'Локомотив', 15]]
N = int(input('Введите число завершенных игр:\n'))
print('Введите результаты матчей:')
inputResults = InputResults(N)
results = OutputResults(inputResults)
print('\nТурнирная таблица:')
PrintOutputResults(results)
