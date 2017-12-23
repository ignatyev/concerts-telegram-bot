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

subscribe = 'Подписаться'
genres = ['rock', 'pop', 'jazz']


@bot.message_handler(content_types=['text'])
def process(message):
    if message.text == '/start':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text=subscribe, url='ya.ru', callback_data="1"))
        bot.send_message(message.chat.id, 'Выберите действие', reply_markup=markup)
    elif message.text == subscribe:
        markup = types.ReplyKeyboardMarkup()
        markup.row(*genres)
        bot.send_message(message.chat.id, 'Выберите стиль', reply_markup=markup)
    elif genres.__contains__(message.text):
        save_user(User(message.from_user.id, [message.text]))
        bot.send_message(message.chat.id, 'Вы подписаны на ' + message.text, reply_markup=types.ReplyKeyboardRemove())


@bot.inline_handler(lambda query: len(query.query) > 0)
def query_text(query):
    print(query)


@bot.callback_query_handler(func=lambda call: True)
def query_text(call):
    print(call)


def set_broadcast_timer():
    broadcast_all()
    timer = threading.Timer(30, set_broadcast_timer)
    timer.start()


def broadcast_all():
    all_events = read_all_events()
    all_users = read_all_users()
    for event in all_events:
        for user in all_users:
            intersection = set(event.genres).intersection(user.genres)
            if len(intersection) > 0 and not event.sent_to.__contains__(user.user_id):
                bot.send_message(user.user_id,
                                 event.place + " приглашает вас " + event.time + " на концерт исполнителя " + event.artist)
                event.sent_to.append(user.user_id)
    save_events(all_events)


set_broadcast_timer()
bot.polling(none_stop=True)


# https://github.com/ignatyev/concerts-telegram-bot
