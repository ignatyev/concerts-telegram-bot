# -*- coding: utf-8 -*-
# 455139656:AAE9id16VLNGI8gz4dBtCSs2WE8Jp1zsu1k
import threading
import telebot
from telebot import types
from event.EventStorage import read_all_events
from user.UserStorage import read_all_users, save_user


bot = telebot.TeleBot('455139656:AAE9id16VLNGI8gz4dBtCSs2WE8Jp1zsu1k')


@bot.message_handler(content_types=['text'])
def process(message):
    subscribe = 'Подписаться'
    if message.text == subscribe:
        save_user(message.from_user.id)
        bot.send_message(message.chat.id, 'Вы подписаны')
    else:
        markup = types.ReplyKeyboardMarkup()
        markup.row(subscribe)
        bot.send_message(message.chat.id, 'Выберите', reply_markup=markup)


def set_broadcast_timer():
    broadcast_all()
    timer = threading.Timer(30, set_broadcast_timer)
    timer.start()


def broadcast_all():
    for event in read_all_events():
        for user in read_all_users():
            bot.send_message(user.id, event.artist)


set_broadcast_timer()
bot.polling(none_stop=True)
