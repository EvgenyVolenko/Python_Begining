# задача RLE необязательная. Реализуйте RLE алгоритм: реализуйте модуль сжатия 
# и восстановления данных (где только буквы присутствуют для простоты).
# например декодирование https://stepik.org/lesson/21300/step/2

def coding(strNot):
    
    strSpis = []
    strCount = []
    for i in strNot:
        strSpis.append(i)

    count = 0
    fSimb = ''
    for i in range(len(strSpis)):
        if fSimb != strSpis[i]:
            if fSimb != None:
                if count > 1:
                    strCount.append(str(count))
                strCount.append(fSimb)
            count = 1
            fSimb = strSpis[i]
        else:
            count += 1
    else:
        if count > 1:
            strCount.append(str(count))
        strCount.append(fSimb)
    strNot = ''.join(strCount)
    return strNot

def decoding(strYes):
    count = ''
    strOut = ''
    for simbol in strYes:
        if simbol.isdigit():
            count += simbol
        else:
            if not count:
                strOut += simbol
            else:
                for i in range(int(count)):
                    strOut += simbol
            count = ''
    return strOut

strS = 'aaabccccCCaBBd'
print(strS)
strS = coding(strS)
print(strS)
strS = decoding(strS)
print(strS)
