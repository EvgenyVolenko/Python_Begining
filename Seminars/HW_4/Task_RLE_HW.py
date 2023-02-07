# задача RLE необязательная. Реализуйте RLE алгоритм: реализуйте модуль сжатия 
# и восстановления данных (где только буквы присутствуют для простоты).
# например декодирование https://stepik.org/lesson/21300/step/2

def coding(strNot):
    unicSimbol = set(strNot)

    for i in unicSimbol:
        counter = 0
        for j in range(len(strNot)):
            if i == strNot[j]:
                counter += 1
                strNot[j] = (f"{strNot[j]}_{counter}")
    return strNot

str = 'aaabccccCCaB'
str = coding(str)

print(str)
