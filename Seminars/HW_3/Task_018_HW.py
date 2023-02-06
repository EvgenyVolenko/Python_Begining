# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint

n = int(input("Введите колличество элементов массива N: "))
sp = [randint(0, 100) for _ in range(n)]
print(sp)
x = int(input("Введите искомое число X: "))

distance = abs(sp[0] - x)
y = sp[0]

for i in range(1, len(sp)):
    if abs(sp[i] - x) < distance:
        y = sp[i]

print(f"Число {y} ближе всех к числу {x}.")