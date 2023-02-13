# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:           Вывод:
# 1 2 3 2 3       2

from random import randint as rnd

def find_pairs_in_list (users_list): 
    count = 0 
    for i in range(len(users_list)): 
        for j in range(i+1,len(users_list)): 
            if users_list[i] == users_list[j] and users_list[j] != '' and users_list[i] != '': 
                count += 1 
                users_list[j] = '' 
                users_list[i] = '' 
    return count 
    
users_len_list = int(input("Введите предполагаемую длину массива: "))
users_list = []

for i in range(users_len_list): 
    users_list.append(rnd(1,10))

print(users_list)

res = find_pairs_in_list(users_list)
print (res)