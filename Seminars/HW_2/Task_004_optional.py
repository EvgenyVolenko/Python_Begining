# задача 4 НЕГА необязательная Задайте число. 
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

try:
    digit = int(input('Введите порядковый номер числа Фибоначчи: '))

    f1 = 0
    f2 = 1
    f3 = f1 + f2
    i = 2

    while i < digit:
        temp = f3
        f3 = f3 + f2
        f2 = temp
        i += 1   
    print(f"Порядковый номер числа Фебоначчи {digit}, а число {f3}")

except:
    print("Вы ввели некоректные данные")