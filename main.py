import telebot
import key
from telebot import types

bot = telebot.TeleBot(key.token)


@bot.message_handler(commands=["start"])
def keyboard_start(message):
    startKBoad = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    Yes = types.KeyboardButton(text="Да")
    No = types.KeyboardButton(text="Нет")
    startKBoad.add(Yes, No)
    bot.send_message(message.chat.id, "Пивет готов узнать Лор Valorant ", reply_markup=startKBoad)


# НЕт
@bot.message_handler(func=lambda m: m.text == "Нет")
def no_lor(message):
    bot.send_message(message.chat.id, "Окет держи ссылку на Valorant 'https://playvalorant.com/ru-ru/'")


# Да
@bot.message_handler(func=lambda m: m.text == "Да")
def lor(message):
    startKBoad = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    Chamber = types.KeyboardButton(text="Chamber")
    Jet = types.KeyboardButton(text="Jett")
    KaOy = types.KeyboardButton(text="Ka/Oy")
    Astra = types.KeyboardButton(text="Astra")
    Viper = types.KeyboardButton(text="Viper ")
    Skay = types.KeyboardButton(text="Skay")
    Yory = types.KeyboardButton(text="Yoru")
    startKBoad.add(Skay, Jet, KaOy, Astra, Viper, Yory, Chamber)
    bot.send_message(message.chat.id, " Ну и лор какого агента хочеш узнать", reply_markup=startKBoad)


@bot.message_handler(func=lambda m: m.text == "Skay")
def skay(message):
    photo = open('asets/img/Skay.png', 'rb')
    bot.send_photo(message.chat.id, photo, " Ок держи биограффию' https://playvalorant.com/ru-ru/agents/skye/ '")

@bot.message_handler(func=lambda m: m.text == "Jett")
def jett(message):
    photo = open('asets/img/Jett.png', 'rb')
    bot.send_photo(message.chat.id, photo, " Ок держи биограффию' https://playvalorant.com/ru-ru/agents/jett/ '")

@bot.message_handler(func=lambda m: m.text == "Ka/Oy")
def kaoy(message):
    photo = open('asets/img/KAYO.png', 'rb')
    bot.send_photo(message.chat.id, photo, " Ок держи биограффию' https://playvalorant.com/ru-ru/agents/kay-o/ '")


@bot.message_handler(func=lambda m: m.text == "Astra")
def astra(message):
    photo = open('asets/img/Astra.png', 'rb')
    bot.send_photo(message.chat.id, photo, " Ок держи биограффию' https://playvalorant.com/ru-ru/agents/astra/ '")

@bot.message_handler(func=lambda m: m.text == "Viper")
def viper(message):
    photo = open('asets/img/Viper.png', 'rb')
    bot.send_photo(message.chat.id, photo, " Ок держи биограффию' https://playvalorant.com/ru-ru/agents/viper/ '")

@bot.message_handler(func=lambda m: m.text == "Yoru")
def yoru(message):
    photo = open('asets/img/yoru.png', 'rb')
    bot.send_photo(message.chat.id, photo, " Ок держи биограффию' https://playvalorant.com/ru-ru/agents/yoru/ '")

@bot.message_handler(func=lambda m: m.text == "Chamber")
def chamber(message):
    photo = open('asets/img/chamber.png', 'rb')
    bot.send_photo(message.chat.id, photo, " Ок держи биограффию' https://playvalorant.com/ru-ru/agents/chamber/ '")

bot.polling()
