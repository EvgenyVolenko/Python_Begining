# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

n1 = int(input('Введите коллличестов учеников в первом классе: '))
n2 = int(input('Введите коллличестов учеников во втором классе: '))
n3 = int(input('Введите коллличестов учеников в третьем классе: '))

if n1 % 2 == 0:
    p1 = n1 / 2
else:
    p1 = n1 // 2 + 1

if n2 % 2 == 0:
    p2 = n2 / 2
else:
    p2 = n2 // 2 + 1

if n3 % 2 == 0:
    p3 = n3 / 2
else:
    p3 = n3 // 2 + 1

sum = p1 + p2 + p3

print(f'Необходимое количество парт: {int(sum)}')