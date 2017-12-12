# -*- coding: utf-8 -*-
# 455139656:AAE9id16VLNGI8gz4dBtCSs2WE8Jp1zsu1k
import threading
import telebot
from telebot import types
from event.EventStorage import read_all_events
from event.EventStorage import save_events
from user.User import User
from user.UserStorage import read_all_users, save_user

bot = telebot.TeleBot('455139656:AAE9id16VLNGI8gz4dBtCSs2WE8Jp1zsu1k')


@bot.message_handler(content_types=['text'])
def process(message):
    subscribe = 'Подписаться'
    add = 'Добавить'
    genres = ['rock', 'pop', 'jazz']
    if message.text == '/start':
        markup = types.ReplyKeyboardMarkup()
        markup.row(subscribe, add)
        bot.send_message(message.chat.id, 'Выберите действие', reply_markup=markup)
    elif message.text == subscribe:
        markup = types.ReplyKeyboardMarkup()
        markup.row(*genres)
        bot.send_message(message.chat.id, 'Выберите стиль', reply_markup=markup)
    elif message.text == add:
        pass
    elif genres.__contains__(message.text):
        save_user(User(message.from_user.id, [message.text]))
        bot.send_message(message.chat.id, 'Вы подписаны на ' + message.text, reply_markup=types.ReplyKeyboardMarkup())


def set_broadcast_timer():
    broadcast_all()
    timer = threading.Timer(30, set_broadcast_timer)
    timer.start()


def broadcast_all():
    all_events = read_all_events()
    for event in all_events:
        for user in read_all_users():
            if len(set(event.genres).intersection(set(user.genres))) > 0 and not event.sent_to.__contains__(user.user_id):
                bot.send_message(user.user_id, event.artist)
                event.sent_to.append(user.user_id)
    save_events(all_events)


set_broadcast_timer()
bot.polling(none_stop=True)
