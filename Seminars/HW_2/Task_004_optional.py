# задача 4 НЕГА необязательная Задайте число. 
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def febon (k):
    if k >= 0: 
        f3 = 0
    if k >= 1:
        f3 = 1
    if k >= 2:
        f1 = 0
        f2 = 1
        f3 = f1 + f2
        i = 2
        while i < k:
            temp = f3
            f3 = f3 + f2
            f2 = temp
            i += 1   
    return f3

try:
    digit = int(input('Введите значение k для расчета чисел Фибоначчи: '))
    digitOtr = - digit
    
    arrayF = []

    if digitOtr < 0:
        for i in range(digitOtr, 0):
            arrayF.append((-1)**(abs(i) - 1) * febon(abs(i)))
    if digit >= 0:
        for i in range(0, digit + 1):
            arrayF.append(febon(i))
    
    print(f"Значение k {digit}, а числа {arrayF}")

except:
    print("Вы ввели некоректные данные")
