# задача калькулятор необязательная.
# Решать только через рекурсию!. Пользоваться встроенными функциями вычисления таких выражений нельзя, если только для проверки вашего алгоритма.
# на вход подается строка из операторов / * + - и целых чисел. Надо посчитать результат введенного выражения.
# Например,
# на входе
# 1+9/3*7-4
# на выходе
# 18

def multiplication(n, k):
    if k == 0:
        return 0
    rez = n + multiplication(n, k - 1) 
    return rez

def division(n, k):
    if n - k == 0:
        return 1
    rez = division(n - k, k) + 1
    return rez

def addition(n, k):
    if k == 0:
        return n
    return addition(n + 1, k - 1)

def subtraction(n, k):
    if k == 0:
        return n
    return subtraction(n - 1, k - 1)

def digitSLR(stroka, razdel):
    digL = ''
    digR = ''
    i = j = 1
    while a[razdel - i].isdigit() and razdel - i > -1:
        digL += a[razdel - i]
        i += 1
    while a[razdel + j].isdigit() and razdel + j < len(stroka) - 1:
        digR += a[razdel + j]
        j += 1
    return [digL, i, digR, j]


a = " 11-9/3*7+4 " # input("Введите выражение для вычисления: ")

print(a)

while "/" in a:
    numD = a.find("/")
    nabor = digitSLR(a, numD)
    digitL = nabor[0]
    i = nabor[1]
    digitR = nabor[2]
    j = nabor[3]
    rezd = division(int(digitL[::-1]), int(digitR))
    a = a.replace(a[numD - i + 1: numD + j], str(rezd), 1)
    
print(a)

while "*" in a:
    numD = a.find("*")
    nabor = digitSLR(a, numD)
    digitL = nabor[0]
    i = nabor[1]
    digitR = nabor[2]
    j = nabor[3]
    rezd = multiplication(int(digitL[::-1]), int(digitR))
    a = a.replace(a[numD - i + 1: numD + j], str(rezd), 1)

print(a)

while "-" in a:
    numD = a.find("-")
    nabor = digitSLR(a, numD)
    digitL = nabor[0]
    i = nabor[1]
    digitR = nabor[2]
    j = nabor[3]
    rezd = subtraction(int(digitL[::-1]), int(digitR))
    a = a.replace(a[numD - i + 1: numD + j], str(rezd), 1)

print(a)

while "+" in a:
    numD = a.find("+")
    nabor = digitSLR(a, numD)
    digitL = nabor[0]
    i = nabor[1]
    digitR = nabor[2]
    j = nabor[3]
    rezd = addition(int(digitL[::-1]), int(digitR))
    a = a.replace(a[numD - i + 1: numD + j], str(rezd), 1)

print(a)


    