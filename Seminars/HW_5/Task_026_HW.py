# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def rec(n, k):
    if k == 0:
        return 1
    rez = n * rec(n, k - 1) 
    return rez
  
a = int(input("Введите число А: "))
b = int(input("Введите число B: "))

print(rec(a, b))