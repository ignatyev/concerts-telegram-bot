# -*- coding: utf-8 -*-
# 455139656:AAE9id16VLNGI8gz4dBtCSs2WE8Jp1zsu1k
import json
import threading

import os
import urllib2

import telebot
from telebot import types

from event.EventStorage import read_all_events
# from weather import Weather

# weather = Weather()
bot = telebot.TeleBot("455139656:AAE9id16VLNGI8gz4dBtCSs2WE8Jp1zsu1k")


@bot.message_handler(content_types=["text"])
def process(message):
    subscribe = 'Подписаться на оповещения'
    propose = 'Предложить концерт'

    if message.text.encode('utf-8').startswith('/event'):
        save_event(message.text)
    elif message.text == subscribe:
        bot.send_message(message.chat.id, 'OK')
        save_user(message.from_user.id)
    elif message.text == propose:
        bot.send_message(message.chat.id,
                         'Предложить событие: /event artist place date, например: /event Metallica Олимпийский 5.10.17')
    markup = types.ReplyKeyboardMarkup()
    markup.row(subscribe, propose)
    bot.send_message(message.chat.id, 'Выберите', reply_markup=markup)
    # lookup = weather.lookup(560743)
    # bot.send_message(message.chat.id, fahrenheit_to_celsius(int(lookup.condition()['temp'])))


def save_user(user_id):
    print('saving user: ' + str(user_id))
    users = open('users.txt', 'a')
    users.write(str(user_id))
    users.write('\n')
    users.close()


def save_event(event):
    print('saving event: ' + event)
    with open('events.txt', 'a') as events:
        events.write(event)
        events.write('\n')


# def fahrenheit_to_celsius(temp):
#     return int((temp - 32) / 1.8)

def set_broadcast_timer():
    broadcast_all()
    timer = threading.Timer(30, set_broadcast_timer)
    timer.setDaemon(True)
    timer.start()




def broadcast_all():
    if os.path.isfile('users.txt') and os.path.isfile('events.txt'):
        with open('users.txt', 'r') as users:
            for event in read_all_events():
                for user in users.readlines():
                    bot.send_message(user, event.artist)
                    # events_from_kudago = get_events_from_kudago()
                    # print(events_from_kudago)
                    # bot.send_message(user, events_from_kudago)


# def get_events_from_kudago():
#     get = urllib2.urlopen("https://kudago.com/public-api/v1.3/events/").read()
#     events = json.loads(get)
#     results = events['results']
#     titles = []
#     for result in results:
#         titles.append(result['title'].encode('utf-8'))
#     return str('\n'.join(titles))


if __name__ == '__main__':
    set_broadcast_timer()
    bot.polling(none_stop=True)
