# coding=utf-8
import telebot


bot = telebot.TeleBot('455139656:AAE9id16VLNGI8gz4dBtCSs2WE8Jp1zsu1k')


@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


bot.polling()
