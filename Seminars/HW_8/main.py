# Задача №49. Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
# в файле. 
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

import functions as f

def procCommand(cmd):
    if cmd == 0:
        f.save(phones)
        return False
    elif cmd in range(1, 4):
        rezFind = f.findContacts(phones, cmd)
        print ('Найденные контакты:')
        for zap in rezFind:
            print(*f.printContacts(phones, phones.index(zap) + 1))
    elif cmd == 4:
        f.addContact(phones)
    elif cmd == 5:
        print("\n".join(f.printContacts(phones)))
        f.editContact(phones)
    elif cmd == 6:
        print("\n".join(f.printContacts(phones)))
        f.delContact(phones)
    elif cmd == 7:
        print("\n".join(f.printContacts(phones)))
    else:
        print ('Неизвестна команда')
    return True

phones = f.load()
print(f.printHelp())

while True:
    try:
        inputCommand = int(input('Введите номер команды: '))
        if not procCommand(inputCommand):
            break
    except ValueError:
        print('Неизвестная')