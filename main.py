# This is a sample Python script.
import telebot
from telebot import types
from io import BytesIO
import urllib

token = '5594158515:AAF6Fl1f6lgRPcoT7kf8sHCTgnJ38h2o_Sc'
url='https://thumbs.dreamstime.com/z/cartoon-robot-riding-bicycle-191440013.jpg'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def start_massage(message):
    bot.send_message(message.chat.id, "Привет " + message.chat.first_name + "!\nМеня зовут ВелоБот! Я помощник команды Сам Себе Велосипед. Можешь задать мне любой вопрос по работе станций проката)\n")
    img = BytesIO(urllib.request.urlopen(url).read())
    bot.send_photo(message.chat.id, img)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
    item1 = types.KeyboardButton("Режим работы")
    item2 = types.KeyboardButton("Цены")
    item3 = types.KeyboardButton("Как вас найти?")
    item4 = types.KeyboardButton("Где можно кататься?")
    item5 = types.KeyboardButton("Какие нужны документы?")
    item6 = types.KeyboardButton("Забронировать инвентарь")

    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    markup.add(item5)
    markup.add(item6)
    bot.send_message(message.chat.id, 'Что бы вы хотели узнать?', reply_markup=markup)

def home(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
    item1 = types.KeyboardButton("Режим работы")
    item2 = types.KeyboardButton("Цены")
    item3 = types.KeyboardButton("Как вас найти?")
    item4 = types.KeyboardButton("Где можно кататься?")
    item5 = types.KeyboardButton("Какие нужны документы?")
    item6 = types.KeyboardButton("Забронировать инвентарь")

    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    markup.add(item5)
    markup.add(item6)
    bot.send_message(message.chat.id, 'Что бы вы хотели узнать?', reply_markup=markup)

def stationChoose(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Кампус ДВФУ")
    item2 = types.KeyboardButton("Набережная Цесаревича")
    item3 = types.KeyboardButton("мыс Ахлестышева")
    item4 = types.KeyboardButton("<- Назад")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    bot.send_message(message.chat.id, "Какая станция проката вас интересует?", reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):

    if message.text == "Режим работы":
        bot.send_message(message.chat.id,"Мы работаем каждый день)\n По будням с 12:00 до 21:00\n По выходным и праздникам с 10:00 до 21:00!")
    if message.text == "Цены":
        bot.send_message(message.chat.id, "Первый час = 300 рублей\nкаждый последующий час = 250 рублей\n\nДень (с открытия до закрытия станции) = 1200 рублей\nСутки = 1500 рублей\nНеделя = 4500 рублей\nМесяц = 9000 рублей")
        bot.send_message(message.chat.id, "Обратите внимание - час не делится! Если вы покатались 1 час 15 минут - заплатить необходимо за 2 часа катания.")
    if message.text == "Как вас найти?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Кампус ДВФУ")
        item2 = types.KeyboardButton("Набережная Цесаревича")
        item3 = types.KeyboardButton("мыс Ахлестышева")
        item4 = types.KeyboardButton("<- Назад")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        bot.send_message(message.chat.id, "Какая станция проката вас интересует?", reply_markup=markup)

    elif message.text == "<- Назад":
        home(message)
    elif message.text == "<-- Назад":
        stationChoose(message)

    ## ПЕРЕДЕЛАТЬ ССЫЛКИ НА КАРТЫ
    elif message.text == "Кампус ДВФУ":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("2GIS (Кампус ДВФУ)")
        item2 = types.KeyboardButton("Google Карты (Кампус ДВФУ)")
        item3 = types.KeyboardButton("Yandex Карты (Кампус ДВФУ)")
        item4 = types.KeyboardButton("<-- Назад")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        bot.send_message(message.chat.id, "В каких картах вам будет удобней посмотреть маршрут?", reply_markup=markup)


    ## ПЕРЕДЕЛАТЬ ССЫЛКИ НА КАРТЫ
    elif message.text == "Набережная Цесаревича":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("2GIS (Набережная Цесаревича)")
        item2 = types.KeyboardButton("Google Карты (Набережная Цесаревича)")
        item3 = types.KeyboardButton("Yandex Карты (Набережная Цесаревича)")
        item4 = types.KeyboardButton("<-- Назад")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        bot.send_message(message.chat.id, "В каких картах вам будет удобней посмотреть маршрут?", reply_markup=markup)

    ## ПЕРЕДЕЛАТЬ ССЫЛКИ НА КАРТЫ
    elif message.text == "мыс Ахлестышева":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("2GIS (мыс Ахлестышева)")
        item2 = types.KeyboardButton("Google Карты (мыс Ахлестышева)")
        item3 = types.KeyboardButton("Yandex Карты (мыс Ахлестышева)")
        item4 = types.KeyboardButton("<-- Назад")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        bot.send_message(message.chat.id, "В каких картах вам будет удобней посмотреть маршрут?", reply_markup=markup)

    elif message.text == "2GIS (Кампус ДВФУ)":
        bot.reply_to(message, "https://go.2gis.com/eymfa")
    elif message.text == "Google Карты (Кампус ДВФУ)":
        bot.send_message(message.chat.id, "https://goo.gl/maps/NsCzSmPi5wAfUUWAA")
    elif message.text == "Yandex Карты (Кампус ДВФУ)":
        bot.send_message(message.chat.id, "Маршрут на ДВФУ в Яндекс")

    elif message.text == "2GIS (Набережная Цесаревича)":
        bot.reply_to(message, "Маршрут на ЦЕС в 2GIS")
    elif message.text == "Google Карты (Набережная Цесаревича)":
        bot.send_message(message.chat.id, "Маршрут на ЦЕС в GOGGLE MAPS")
    elif message.text == "Yandex Карты (Набережная Цесаревича)":
        bot.send_message(message.chat.id, "Маршрут на ЦЕС в Яндексе")


    elif message.text == "2GIS (мыс Ахлестышева)":
        bot.reply_to(message, "Маршрут на Ахлестышева в 2GIS")
    elif message.text == "Google Карты (мыс Ахлестышева)":
        bot.send_message(message.chat.id, "Маршрут на Ахлестышева в GOOGLE MAPS")
    elif message.text == "Yandex Карты (мыс Ахлестышева)":
        bot.send_message(message.chat.id, "Маршрут на Ахлестышева в YANDEX")



    elif message.text == "Где можно кататься?":
        bot.reply_to(message, "Вы можете кататься где угодно)\nМожете взять велосипед и поехать в другой город. Главное вернуть инвентарь в целости и сохранности)")

    elif message.text == "Какие нужны документы?":
        bot.reply_to(message, "Чтобы получить инвентарь в прокат понадобиться оригинал документа (Паспорт РФ либо Водительское удостоверение)\n\nНа один документ можно взять 3 ед. инвентаря.\n\nОбратите внимание, подойдет только оригинал.\nФото документов мы не принимаем.\n\nНу а если вы у нас уже были - достаточно будет назвать номер телефона)")

    elif message.text == "Забронировать инвентарь":
        bot.reply_to(message, "К сожалению, забронировать велосипед пока нельзя(\nНо мы работаем над этим!")
#markup.add(item1)

bot.infinity_polling()