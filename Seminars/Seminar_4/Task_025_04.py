# Задача №25. Решение в группах Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n. Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2 Для решения данной задачи используйте функцию
# .split()

str = 'a a a b c a a d c d d'
str = str.split()
unicSimbol = set(str)

for i in unicSimbol:
    counter = 0
    for j in range(len(str)):
        if i == str[j]:
            counter += 1
            if counter >= 2:
                str[j] = (f"{str[j]}_{counter - 1}")

print(str)
print(' '.join(str))
