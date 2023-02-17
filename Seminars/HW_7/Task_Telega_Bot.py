from random import *
import json

films = []

def save():
    with open('films.json', 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(films, ensure_ascii = False))
        print('Наша фильмотека была успешно сохранена в файле films.json')

    # films = []
    # films.append('Матрица')
    # films.append('Солярис')
    # films.append('Властелин колец')
    # films.append('Техассая резня бензопилой')
    # films.append('Санта барбара')

while True:
    command = input('Введите команду ')
    if command == '/start':
        print('Бот-фильмотека начал свою работу')
    elif command == '/stop':
        save()
        print('Бот остановил свою работу. Заходите еще, будем рады!')
        break
    elif command == '/all':
        print(f"Вот текущий список фильмов\n {', '.join(films)}")
    elif command == '/add':
        films.append(input('Введите наименование фильма для добавления '))
        print('Фильм был успешно добавлен в коллекцию.')
    elif command == '/delete':
        f = input('Введите наименование фильма для удаления ')
        '''
        if f in films:
            films.remove(f)
            print('Фильм был успешно удален из коллекции.')
        else:
            ('Такого фильма нет в фильмотеке')
        '''
        try:
            films.remove(f)
            print('Фильм был успешно удален из коллекции.')
        except:
            print('Такого фильма нет в фильмотеке')
    elif command == 'help':
        print('Здесь какой-то мануал')
    elif command == '/random':
        # rnd = randint(0, len(films) - 1)
        # print('Слепой жребий показал вам фильм -' + ' ' + films[rnd])
        print('Слепой жребий показал вам фильм -' + ' ' + choice(films))
    elif command == '/save':
        save()
    elif command == '/load':
        with open('films.json', 'r', encoding='utf-8') as fh:
            films = json.load(fh)
        print('Наша фильмотека была успешно загружена')
    else:
        print('Неопознанная команда. Просьба погладить манула через /help')