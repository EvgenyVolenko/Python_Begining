# Задача HARD SORT необязательная.
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры.
# Отсортировать элементы по возрастанию слева направо и сверху вниз.
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
# После сортировки
# 1 2 3 4
# 5 7 9 10

from random import randint

def printMatrix(matrix): 
   for row in matrix: 
      for x in row: 
          print ( "{:4d}".format(x), end = "" ) 
      print ()

def matrixToArray(matrix):
    array = []
    for row in matrix: 
      for x in row: 
        array.append(x)
    return array
    
def arrayToMatrix(arr):
    i = 0
    for j in range ( len(massiv) ): 
        for k in range ( len(massiv[j]) ): 
            massiv[j][k] = arr[i]
            i += 1
    return massiv
            
n = int(input("Введите число строк: "))
m = int(input("Введите число столбцов: "))

massiv = [[randint(0, 10) for _ in range(m)] for _ in range(n)]

printMatrix(massiv)
arr = matrixToArray(massiv)
arr.sort()
print()
massiv = arrayToMatrix(arr)
printMatrix(massiv)
