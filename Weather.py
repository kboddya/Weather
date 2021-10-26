import telebot
from telebot import types

bot = telebot.TeleBot('1328514129:AAFTw6SJ_ri42qHTWFHZN7A1u3GJEOKrwRs');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text =="Прогноз" or message.text == "/start":

        markup = types.InlineKeyboardMarkup()
        buttonA = types.InlineKeyboardButton('A', callback_data='a')
        buttonB = types.InlineKeyboardButton('B', callback_data='b')
        buttonC = types.InlineKeyboardButton('C', callback_data='c')

        markup.row(buttonA, buttonB)
        markup.row(buttonC)

        bot.send_message(message.chat.id, 'It works!', reply_markup=markup)
        bot.send_message(message.from_user.id, "Впишы название города для получения прогноза")
    
    elif message.text =="/help":
        bot.send_message(message.from_user.id, "Напиши прогноз")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling()
