# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def change(ved1, max1, min1):
    if len(ved1) == 0:
        return[]
    else:
        if ved1[0] == max1:
            ved1[0] = min1
        return [ved1[0]] + change(ved1[1:], max1, min1)
    
from random import randint

n = int(input("Введите количество оценок: "))
ved = [randint(1, 5) for _ in range(n)]

print(ved)

maxO = max(ved)
minO = min(ved)

print(change(ved, maxO, minO))
