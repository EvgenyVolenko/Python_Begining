# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

try:
    digit = int(input('Введите число: '))

    f1 = 0
    f2 = 1
    f3 = f1 + f2
    i = 2

    while digit >= f3:
        if digit == f3:
            print(f"Порядковый номер числа Фебоначчи {i + 1}")
            break
        temp = f3
        f3 = f3 + f2
        f2 = temp
        i += 1   
    else:
        print(-1)            
except:
    print("Вы ввели некоректные данные")
