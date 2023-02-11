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

def ret(s):
    if s.isdigit():
        return float(s)
    for c in ('+','-','*','/'):
        left, operator, right = s.partition(c)
        if operator == '*':
            return multiplication(ret(left), ret(right))
        elif operator == '/':
            return division(ret(left), ret(right))
        elif operator == '+':
            return addition(ret(left), ret(right))
        elif operator == '-':
            return subtraction(ret(left), ret(right))

a = "11-9/3*7+4" # input("Введите выражение для вычисления: ")

print(ret(a))
   
print(a)

