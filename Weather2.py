import telebot
from telebot import types

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps


owm = OWM('b57da7a65340381f8cabd14555c9dee3')
mgr = owm.weather_manager()

bot = telebot.TeleBot('2032267716:AAHzTqX4wcLUTiUmPP6o3r6ZcREZ4KMzk84')

def get_current_weather(city):
    observation = mgr.weather_at_place(city)


    return observation.weather

cities = {
    "Київ" : "Kyiv, UA"
}

def get_forecast(city):
    forecast = mgr.forecast_at_place(city, 'daily')

    return forecast.will_be_clear_at(timestamps.tomorrow())

    w = get_current_weather([])

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    markup = types.InlineKeyboardMarkup()
    buttonA = types.InlineKeyboardButton('Київ', callback_data='Київ')
    buttonB = types.InlineKeyboardButton('Чернівці', callback_data='Чернівці')

    markup.row(buttonA, buttonB)


    if message.text == "/start":
        bot.send_message(message.from_user.id, "Вибери місто", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle(call):
        w = get_current_weather([])
        bot.send_message(call.message.chat.id, 'Місто  {city}:' + str(w.temperature('celsius')['temp']) + '°C'.format(city = str(call.data)))
        bot.answer_callback_query(call.id)



bot.polling()
