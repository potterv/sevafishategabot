# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import telebot
import bs4, requests
from config_bot import TOKEN
from parssevafisha import *
from telebot import types
import re

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])
def send_messages(message): # Название функции не играет никакой роли, в принципе
    films=cinema_Read()
    listSortFilms=sortKeysDict(films)

    for cinema in listSortFilms:

        listSortKinoteatr=sortKeysDict(films.get(cinema)[1])
        text=''

        for kinoteatr in listSortKinoteatr:

                keyboard = types.InlineKeyboardMarkup()
                seances = films.get(cinema)[1].get(kinoteatr)
                seance_=''
                for seance in seances:
                     seance_=' '.join([seance_,seance])

                text='\n'.join([text,kinoteatr, seance_])
        strText=' \n'.join([cinema,films.get(cinema)[0],text])
        url_button = types.InlineKeyboardButton(text='Смотреть трейлер', url=''.join(["https://www.youtube.com/results?search_query=",cinema]))
        keyboard.add(url_button)
        bot.send_message(message.chat.id,strText,reply_markup=keyboard)


if __name__ == '__main__':

    bot.polling(none_stop=True)
