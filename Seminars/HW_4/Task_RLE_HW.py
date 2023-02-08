# задача RLE необязательная. Реализуйте RLE алгоритм: реализуйте модуль сжатия 
# и восстановления данных (где только буквы присутствуют для простоты).
# например декодирование https://stepik.org/lesson/21300/step/2

def coding(strNot):
    
    strSpis = []
    strCount = []
    for i in strNot:
        strSpis.append(i)

    print(strSpis)
    count = 1
    fSimb = strSpis[0]
    for i in range(1, len(strSpis)):
        if fSimb == strSpis[i]:
            count += 1
            print(strSpis[i], count)
        else:
            if count > 1:
                strCount.append(count)
            strCount.append(fSimb)
            fSimb = strSpis[i]
            count = 1
            print(strSpis[i], count)
    return strCount

str = 'aaabccccCCaB'
print(str)
str = coding(str)
print(str)
