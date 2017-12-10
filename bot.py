# -*- coding: utf-8 -*-
# 455139656:AAE9id16VLNGI8gz4dBtCSs2WE8Jp1zsu1k
import threading
import telebot
from telebot import types
from event.EventStorage import read_all_events
from event.EventStorage import save_events
from event.EventStorage import clear_events
from user.UserStorage import read_all_users, save_user

bot = telebot.TeleBot('455139656:AAE9id16VLNGI8gz4dBtCSs2WE8Jp1zsu1k')


@bot.message_handler(content_types=['text'])
def process(message):
    subscribe = 'Подписаться'
    add = 'Добавить'
    if message.text == subscribe:
        save_user(message.from_user.id)
        markup = types.ReplyKeyboardMarkup()
        markup.row()
        bot.send_message(message.chat.id, 'Выберите стиль', reply_markup=markup)
    elif message.text == add:
        pass
    else:
        markup = types.ReplyKeyboardMarkup()
        markup.row(subscribe)
        bot.send_message(message.chat.id, 'Вы подписаны ', reply_markup=markup)


def set_broadcast_timer():
    broadcast_all()
    timer = threading.Timer(30, set_broadcast_timer)
    timer.start()


def broadcast_all():
    all_events = read_all_events()
    for event in all_events:
        for user in read_all_users():
            if not event.sent_to.__contains__(user.user_id):
                bot.send_message(user.user_id, event.artist)
                event.sent_to.append(user.user_id)
    save_events(all_events)


set_broadcast_timer()
bot.polling(none_stop=True)
