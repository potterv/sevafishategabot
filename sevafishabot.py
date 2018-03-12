# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import telebot
import bs4, requests
from config_bot import TOKEN
from parssevafisha import cinemaRead 

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    
    bot.send_message(message.chat.id, cinemaRead())

if __name__ == '__main__':

    bot.polling(none_stop=True)
    