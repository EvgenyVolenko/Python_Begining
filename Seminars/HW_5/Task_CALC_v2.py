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

def digitSL(stroka, razdel, digL = ''):
    i =  1
    while stroka[razdel - i].isdigit() and razdel - i > -1:
        digL += stroka[razdel - i]
        i += 1
    return [digL[::-1].replace('.', '', 1), i]

def digitSR(stroka, razdel, digR = ''):
    j = 1
    while stroka[razdel + j].isdigit() and razdel + j < len(stroka) - 1:
        digR += stroka[razdel + j]
        j += 1
    return [digR.replace('.', '', 1), j]

a = " 11-9/3*7+4 " # input("Введите выражение для вычисления: ")

print(a)

while "/" in a:
    numD = a.find("/")
    naborL = digitSL(a, numD)
    digitL = naborL[0]
    i = naborL[1]
    naborR = digitSR(a, numD)
    digitR = naborR[0]
    j = naborR[1]
    rezd = division(int(digitL), int(digitR))
    a = a.replace(a[numD - i + 1: numD + j], str(rezd), 1)
    
print(a)

while "*" in a:
    numD = a.find("*")
    naborL = digitSL(a, numD)
    digitL = naborL[0]
    i = naborL[1]
    naborR = digitSR(a, numD)
    digitR = naborR[0]
    j = naborR[1]
    rezd = multiplication(int(digitL), int(digitR))
    a = a.replace(a[numD - i + 1: numD + j], str(rezd), 1)

print(a)

while "-" in a:
    numD = a.find("-")
    naborL = digitSL(a, numD)
    digitL = naborL[0]
    i = naborL[1]
    naborR = digitSR(a, numD)
    digitR = naborR[0]
    j = naborR[1]
    rezd = subtraction(int(digitL), int(digitR))
    a = a.replace(a[numD - i + 1: numD + j], str(rezd), 1)

print(a)

while "+" in a:
    numD = a.find("+")
    naborL = digitSL(a, numD)
    digitL = naborL[0]
    i = naborL[1]
    naborR = digitSR(a, numD)
    digitR = naborR[0]
    j = naborR[1]
    rezd = addition(int(digitL), int(digitR))
    a = a.replace(a[numD - i + 1: numD + j], str(rezd), 1)

print(a)
    