# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств

from random import randint

n = int(input("Введите колличество элементов Первого набора чисел: "))
m = int(input("Введите колличество элементов Второго набора чисел: "))

strN = [randint(0, 10) for _ in range(n)]
strM = [randint(0, 10) for _ in range(m)]

print(strN)
print(strM)

strP = set(strN) & set(strM)
strR = []

for i in strP:
    strR.append(str(i))

print(' '.join(sorted(strR)))
