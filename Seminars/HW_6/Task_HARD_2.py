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

def matrixToArray(matrix):
    array = []
    arrayN = []
    i = 0
    for row in matrix: 
      for x in row: 
        array.append(x)
        arrayN.append(i)
        i += 1
    return array, arrayN

def arrayToMatrix(arr):
    i = 0
    for j in range ( len(massiv) ): 
        for k in range ( len(massiv[j]) ): 
            massiv[j][k] = arr[i]
            i += 1
    return massiv

while True:
    n = int(input("Введите число строк: "))
    m = int(input("Введите число столбцов: "))
    if n * m % 2 == 0:
        break
    print(f"Количество элементов массива {m} * {n} НЕЧЕТНОЕ. А нужно четное!")

massiv = [[0,1,2,3],[4,5,6,7]]#[[randint(0, 10) for _ in range(m)] for _ in range(n)]

printMatrix(massiv)
print()
arr = matrixToArray(massiv)[0]
arrN = matrixToArray(massiv)[1]

for i in range(len(arr) // 2):
    j = randint(0, len(arrN) - 1)
    tempJ = arr[arrN[j]]
    print(f"J {arrN[j]} {tempJ}")
    arrN.pop(j)
    k = randint(0, len(arrN) - 1)
    if k == j:
        k = randint(0, len(arrN) - 1)
    tempK = arr[arrN[k]]
    print(f"K {arrN[k]} {tempK}")
    arrN.pop(k)
    tempArr = arr[tempJ]
    arr[tempJ] = arr[tempK]
    arr[tempK] = tempArr
    print(arr)
    
printMatrix(arrayToMatrix(arr))
