# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

try:
    sumJur = int(input('Введите количество сделанных журавликов: '))
    sumEd = int (sumJur / 6)

    sumPetr = sumSerj = sumEd
    sumKate = sumEd * 4

    print(f'Петя сделал {sumPetr} журавлика(ов),\nКатя сделала {sumKate} журавлика(ов),\nСережа сделал {sumSerj} журавлика(ов).')
except:
    print("Вы ввели некоректные данные")
