# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

n = int(input('Введите N: '))

def addWord(ind, str):
    if (ind >= n):
        return str
    str += input(f'Введите {ind+1}-ый символ: ')
    return addWord(ind +1, str)

def revertStr(ind, inputStr, resultStr):
    if (ind < 0):
        return resultStr
    resultStr += inputStr[ind]
    return revertStr(ind -1, inputStr, resultStr)

inputStr = addWord(0, "")
torevertStr = revertStr(len(inputStr) -1, inputStr, "")
print(inputStr)
print(torevertStr)