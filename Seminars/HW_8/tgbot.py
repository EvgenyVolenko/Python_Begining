import telebot
import functions as f

phones = []

API_TOKEN='___'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        global phones 
        phones = f.load()
        bot.send_message(message.chat.id,"Телефонный справочник загружен успешно!")
        bot.send_message(message.chat.id, f.printHelp())
    except:
        bot.send_message(message.chat.id,"Телефонный справочник НЕ загружен!")


@bot.message_handler(commands=['7'])
def show_all(message):
    bot.send_message(message.chat.id,"Показать все контакты с номерами в справочнике")
    bot.send_message(message.chat.id, "\n".join(f.printContacts(phones)))

@bot.message_handler(commands=['6'])
def show_all(message):
    bot.send_message(message.chat.id,"Удалить контакт по номеру записи в справочнике")
    bot.send_message(message.chat.id, "\n".join(f.printContacts(phones)))

@bot.message_handler(commands=['5'])
def show_all(message):
    bot.send_message(message.chat.id,"Редактировать контакт по номеру записи в справочнике")
    bot.send_message(message.chat.id, "\n".join(f.printContacts(phones)))

@bot.message_handler(commands=['4'])
def show_all(message):
    bot.send_message(message.chat.id,"Добавить контакт")
    bot.send_message(message.chat.id, "\n".join(f.printContacts(phones)))

@bot.message_handler(commands=['3'])
def show_all(message):
    bot.send_message(message.chat.id,"Поиск по номмеру телефона")
    bot.send_message(message.chat.id, "\n".join(f.printContacts(phones)))

@bot.message_handler(commands=['2'])
def show_all(message):
    bot.send_message(message.chat.id,"Поиск по фамилии контакта")
    bot.send_message(message.chat.id, "\n".join(f.printContacts(phones)))

@bot.message_handler(commands=['1'])
def show_all(message):
    bot.send_message(message.chat.id,"Поиск по имени контакта")
    bot.send_message(message.chat.id, "\n".join(f.printContacts(phones)))


@bot.message_handler(commands=['save'])
def save_all(message):
    try:
        print("Получилось")
        bot.send_message(message.chat.id,"Фильмотека была успешно сохранена!")
    except:
        bot.send_message(message.chat.id,"Что-то пошло не ТАК!!!")

@bot.message_handler(content_types='text')
def message_reply(message):
    if 'привет' in message.text :
        bot.send_message(message.chat.id,'и тебе привет')

bot.polling()
