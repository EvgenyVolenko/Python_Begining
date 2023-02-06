# Задача HARD необязательная Имеется список чисел. Создайте список, в который попадают числа, 
# описывающие максимальную возрастающую последовательность. Порядок элементов менять нельзя.
# Одно число - это не последовательность.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5]
# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5]

lst = [1, 5, 3, 4, 1, 9, 8, 15, 14, 1]
print(lst)

minZ = tempMIN = min(lst)
maxZ = max(lst)

lstMM = [minZ, maxZ]
lstMMT = list()

for i in range(len(lst)):
    if tempMIN + 1 in lst:
        if tempMIN > minZ:
            minZ = tempMIN + 1
        break
    else:
        tempMIN += 1
        
for j in range(len(lst)):
    if tempMIN + 1 in lst:
        tempMIN += 1
        lstMM = [minZ, tempMIN]

a = lstMM[1] - lstMM[0]        
print(lstMM, a + 1)

for i in range(len(lst)):
    if tempMIN + 1 in lst:
        if tempMIN > minZ:
            minZ = tempMIN + 1
        break
    else:
        tempMIN += 1
        
for j in range(len(lst)):
    if tempMIN + 1 in lst:
        tempMIN += 1
        lstMMT = [minZ, tempMIN]

b = lstMMT[1] - lstMMT[0]        
print(lstMMT, b + 1)


