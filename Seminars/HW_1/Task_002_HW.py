# Задача 2: Найдите сумму цифр трехзначного числа.

try:
    digit = int(input('Введите трехзначное число: '))
    sum = 0        
    figure = 0
    while digit > 0:
        figure = digit % 10
        sum += figure
        digit = digit // 10
    print(sum)
except:
    print("Вы ввели некоректные данные")
    