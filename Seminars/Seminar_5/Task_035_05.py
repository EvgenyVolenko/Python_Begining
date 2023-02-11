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

def simple2(n, m):
    if m == 1:
        return True
    elif n % m == 0:
        return False
    else:
        return True and simple2(n, m - 1)

n = int(input("Введите число для проверки: "))

print(simple(n))
print(simple2(n, n - 1))