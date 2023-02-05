# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

def funcHalf(halfNumber):
    sum = 0
    for i in range(3):
        sum += int(halfNumber[i])
    return sum

try:
    numberTicket = input('Введите номер билета из 6 цифр: ')
    numberTicket1 = numberTicket[:3]
    numberTicket2 = numberTicket[3:]

    numberTicket1 = funcHalf(numberTicket1)
    numberTicket2 = funcHalf(numberTicket2)

    if numberTicket1 == numberTicket2:
        print("Ваш билет СЧАСТЛИВЫЙ")
    else: 
        print("Ваш билет НЕ счасливый")
    
except:
    print("Вы ввели некоректные данные")
