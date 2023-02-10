# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint

n = int(input("Введите количество оценок: "))

ved = []

for i in range(n):
    ved.append(randint(1, 5))

print(ved)

maxO = max(ved)

for i in range(n):
     if ved[i] == maxO:
        ved[i] = 1

print(ved)