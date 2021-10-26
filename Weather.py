import telebot
from telebot import types

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps


owm = OWM('your free OWM API key')
mgr = owm.weather_manager()

bot = telebot.TeleBot('1328514129:AAFTw6SJ_ri42qHTWFHZN7A1u3GJEOKrwRs')

def get_current_weather(city):
    observation = mgr.weather_at_place(city)
    
    return observation.weather

def get_forecast(city):
    forecast = mgr.forecast_at_place(city, 'daily')
    
    return forecast.will_be_clear_at(timestamps.tomorrow())

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text =="Прогноз" or message.text == "/start":

        markup = types.ReplyKeyboardMarkup()
        buttonA = types.KeyboardButton('Прогноз')
        buttonB = types.KeyboardButton('/start')
        buttonC = types.KeyboardButton('/help')

        markup.row(buttonA, buttonB)
        markup.row(buttonC)
        bot.send_message(message.chat.id, 'Впишы название города для получения прогноза', reply_markup=markup)


    elif message.text =="/help":
        bot.send_message(message.from_user.id, "Напиши прогноз")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling()
