# Задача 5 - HARD необязательная
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними
# в N-мерном пространстве. Сначала задается N с клавиатуры, потом задаются координаты точек.

from random import randint

def dist(coordt1, coordt2):
    d2 = 0
    for i in range(len(coordt1)):
        d2 += (coordt1[i] - coordt2[i]) ** (2)
    dist = d2 ** (0.5)
    return dist

def coords (N, min, max):
    arrayA = []
    for i in range(N):
        arrayA.append(randint(min, max))
    return arrayA

try:
    nMer = int(input('Введите мерность пространства: '))
    min = int(input('Введите начало диапазона координат: '))
    max = int(input('Введите конец диапазона координат: '))
      
    arrayt1 = coords(nMer, min, max)
    arrayt2 = coords(nMer, min, max)

    D = round(dist(arrayt1, arrayt2), 2)

    print(f"Расстояние между точками = {D}")
            
except:
    print("Вы ввели некоректные данные")
