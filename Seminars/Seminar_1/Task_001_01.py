# За день машина проезжает n километров. 
# Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

# from math import ceil

# n = 700 # скорость
# m = 750 # дистанция

# time = ceil (m / n)

# ost = m // n

# d = int(m / n) + ost

# print(time)

try:
    distance = int(input('Введите дистанцию: '))
    speed = int(input('Введите скорость: '))

    if distance % speed == 0:
        time = distance / speed
    else:
        time = distance // speed + 1

    print(time)
except:
    print("Вы ввели некоректные данные")