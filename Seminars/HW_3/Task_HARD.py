# Задача HARD необязательная Имеется список чисел. Создайте список, в который попадают числа, 
# описывающие максимальную возрастающую последовательность. Порядок элементов менять нельзя.
# Одно число - это не последовательность.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5]
# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5]

def vozrPosl (lst, lstMM, minZ, tempMIN):
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
    return (lstMM, tempMIN)

lst = [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ]
print(lst)

minZ = tempMIN = min(lst)
maxZ = max(lst)

lstMM = [minZ, maxZ]
bibl = {}

while tempMIN < maxZ:
    D = vozrPosl(lst, lstMM, minZ, tempMIN)
    tempMIN = D[1]
    lstMMT = D[0]
    if lstMMT[1] - lstMMT[0] != 0:
        bibl[lstMMT[1] - lstMMT[0] + 1] = D[0]
        
x = 0

for k, v in bibl.items():
    if k > x:
        x = k
        print(f"Наибольшая последовательность {bibl[x]}")
