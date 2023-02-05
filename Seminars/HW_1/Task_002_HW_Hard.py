# Задача 2: - HARD необязательная, идет за 3 обязательных Найдите сумму 
# цифр любого вещественного или целого числа. Можно использовать decimal. 
# Через строку решать нельзя.

from decimal import Decimal


try:
    digit = Decimal(input('Введите число: '))
    digitInt = digitF = int(digit)
    
    sum1 = 0        
    figure = 0
    while digitInt > 0:
        figure = digitInt % 10
        sum1 += figure
        digitInt = digitInt // 10

    num = digit - digitF
    
    digits = num.as_tuple().digits
    print(sum(digits) + sum1)

except:
    print("Вы ввели некоректные данные")

