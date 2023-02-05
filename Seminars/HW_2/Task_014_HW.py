# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.

num = int(input("Введите число: "))
digit = 0
rez = 0

while rez <= num:
    rez = 2 ** (digit)
    digit += 1
    if rez <= num:
        print(rez)