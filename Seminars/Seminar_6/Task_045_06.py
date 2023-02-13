# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести все
# пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:           Вывод:
# 300             220 284

def sumDel(digit):
    deliteli = 0
    for i in range(1, digit):
        if digit % i == 0:
            deliteli += i
    return deliteli

n = int(input("Введите число для проверки: "))

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if sumDel(i) == j and sumDel(j) == i:
            print(i, j)
    