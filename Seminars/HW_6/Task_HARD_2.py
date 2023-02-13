# задача 2 HARD необязательная
# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры),
# причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей.
# Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно и только один раз
# переместился на другое место и выполнить это за m*n / 2 итераций. То есть если массив три на четыре,
# то надо выполнить не более 6 итераций. И далее в конце опять вывести на экран как таблицу.

from random import randint

def printMatrix(matrix): 
   for row in matrix: 
      for x in row: 
          print ( "{:4d}".format(x), end = "|" ) 
      print ()

while True:
    n = int(input("Введите число строк: "))
    m = int(input("Введите число столбцов: "))
    if n * m % 2 == 0:
        break
    print(f"Количество элементов массива {m} * {n} НЕЧЕТНОЕ. А нужно четное!")

massiv = [[randint(0, 10) for _ in range(m)] for _ in range(n)]

printMatrix(massiv)