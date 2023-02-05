# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть

from random import randint

num = int(input("Введите количество монет: "))

array = []

for i in range(num):
    array.append(randint(0, 1))

orel = 0
reshka = 0

for i in range(num):
    if array[i] == 0:
        orel += 1
    elif array[i] == 1:
        reshka += 1

if orel > reshka:
    print(f"Нужно перевернуть {reshka} монету(ы)")
elif reshka > orel:
    print(f"Нужно перевернуть {orel} монету(ы)")
else:
    print(f"А все равно... количество решек {reshka} = количеству орлов {orel}")