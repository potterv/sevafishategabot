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

    listSortFilms=sortKeysDict(cinema_Read())
    for cinema in listSortFilms:
        #print(cinema)
        #print(cinema_Read().get(cinema)[0])
        strText=' \n'.join([cinema,cinema_Read().get(cinema)[0]])
        bot.send_message(message.chat.id, strText)

        #print(cinema_Read().get(cinema)[1])
        listSortKinoteatr=sortKeysDict(cinema_Read().get(cinema)[1])
        for kinoteatr in listSortKinoteatr:
                 #print(kinoteatr)
                # bot.send_message(message.chat.id, "kinoteatr", reply_markup=keyboard)
                 #keyboard = types.InlineKeyboardMarkup()

                 for seance in cinema_Read().get(cinema)[1].get(kinoteatr):
                   # print(seance)
                    keyboard = types.InlineKeyboardMarkup()
                    url_button = types.InlineKeyboardButton(text=seance, url="https://ya.ru")
                    keyboard.add(url_button)
                    bot.send_message(message.chat.id,kinoteatr,reply_markup=keyboard)
                 #bot.send_message(message.chat.id, kinoteatr)
        #bot.send_message(message.chat.id, cinemaRead())

    #keyboard = types.InlineKeyboardMarkup()
    #url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
    #keyboard.add(url_button)
    #bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)


if __name__ == '__main__':

   '''
    films=cinema_Read()
    listSortFilms=sortKeysDict(films)
    print(films)
    #print(listSortFilms)

    for cinema in listSortFilms:
       #print('\n'+cinema+'\n')
       #print(films.get(cinema)[0])
       kinoteatrs=films.get(cinema)[1]
       #print(kinoteatrs)
        #listSortKinoteatr=sortKeysDict(cinema_Read().get(cinema)[1]))
        #print(listSortKinoteatr)


        listSortKinoteatr=sortKeysDict(cinema_Read().get(cinema)[1])
        for kinoteatr in listSortKinoteatr:
                 print(kinoteatr)
                 print()
                 for seance in cinema_Read().get(cinema)[1].get(kinoteatr):
                    print(seance)
    '''

   bot.polling(none_stop=True)
