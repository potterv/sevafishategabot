# -*- coding: utf-8 -*-

# import bs4, requests
import telebot

from config_bot import TOKEN
from parssevafisha import *
from telebot import types
# import re

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start_(message):
    name=''
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Обновить']])
    msg=bot.send_message(message.chat.id,'Для просмотра тыкни обновить',reply_markup=keyboard)
    if message=='Обновить':
                 bot.send_message(message.chat.id,'/text')
    # bot.register_next_step_handler(msg,name)


@bot.message_handler(content_types=["text"])

def send_messages(message): # Название функции не играет никакой роли, в принципе
    films=cinema_Read()
    print(films)
    listSortFilms=sortKeysDict(films)

    for cinema in listSortFilms:

        listSortKinoteatr=sortKeysDict(films.get(cinema)[1])
        text=''

        for kinoteatr in listSortKinoteatr:
                seance_=''
                keyboard = types.InlineKeyboardMarkup()
                seances = films.get(cinema)[1].get(kinoteatr)

                for seance in seances:
                     seance_=' '.join([seance_,seance])

                text='\n'.join([text,kinoteatr, seance_])
        strText=' \n'.join([cinema,films.get(cinema)[0],text])
        url_button = types.InlineKeyboardButton(text='Смотреть трейлер', url=''.join(["https://www.youtube.com/results?search_query=",cinema]))
        keyboard.add(url_button)
        bot.send_message(message.chat.id,strText,reply_markup=keyboard)
    bot.send_message(message.chat.id,'Для обновления, отправь любой текст')
    # update =types.InlineKeyboardButton(text='Обновить')
    # keyboard.add(update)
    # bot.send_message(message.chat.id, strText, reply_markup=keyboard)

if __name__ == '__main__':
   bot.polling(none_stop=True)
