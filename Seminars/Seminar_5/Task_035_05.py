# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

def simple(digit):
    deliteli = []
    for i in range(1, digit + 1):
        if digit % i == 0:
            deliteli.append(i)
    print(deliteli)
    if len(deliteli) == 2:
        anser = True
    else:
        anser = False
    return anser

n = int(input("Введите число для проверки: "))

print(simple(n))