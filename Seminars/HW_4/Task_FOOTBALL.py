# Задача FOOTBALL необязательная. Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
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

from random import randint
commands = ['Спартак', 'Зенит', 'Локомотив']
n = int(input("Введите количество матчей: "))
tableRez = {}
for i in commands:
    tableRez[i] = [0, 0, 0, 0, 0]

rezGNabor = []
for i in range(n):
    comanda1 = comanda2 = ''
    while comanda1 == comanda2:
        comanda1 = commands[randint(0, len(commands) - 1)]
        comanda2 = commands[randint(0, len(commands) - 1)]
    rezG = f"{comanda1};{str(randint(0, 5))};{comanda2};{str(randint(0, 5))}"
    rezGNabor.append(rezG)

tempComanda1 = []
tempComanda2 = []

for i in range(n):
    strRez = rezGNabor[i].split(';')
    if strRez[1] > strRez[3]:
        tempComanda1 = tableRez[strRez[0]]
        tempComanda2 = tableRez[strRez[2]]
        tempComanda1[0] += 1
        tempComanda2[0] += 1
        tempComanda1[1] += 1
        tempComanda1[4] += 3
        tempComanda2[3] += 1
    elif strRez[1] < strRez[3]:
        tempComanda1 = tableRez[strRez[0]]
        tempComanda2 = tableRez[strRez[2]]
        tempComanda1[0] += 1
        tempComanda2[0] += 1
        tempComanda2[1] += 1
        tempComanda2[4] += 3
        tempComanda1[3] += 1
    else:
        tempComanda1 = tableRez[strRez[0]]
        tempComanda2 = tableRez[strRez[2]]
        tempComanda1[0] += 1
        tempComanda2[0] += 1
        tempComanda1[2] += 1
        tempComanda2[2] += 1
        tempComanda1[4] += 1
        tempComanda2[4] += 1

tempStr = ''

for (k, v) in tableRez.items():
    for i in v:
        tempStr += str(i) + " "
    print(f"{k}: {tempStr}")
    tempStr = ''

print(rezGNabor)
