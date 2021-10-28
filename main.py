import telebot
from telebot import types

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

import os
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv('TOKEN')
OWMKEY = os.getenv('OWMKEY')

config_dict = get_default_config()
config_dict['language'] = 'ua'

owm = OWM(OWMKEY, config_dict )
mgr = owm.weather_manager()

bot = telebot.TeleBot(TOKEN)

def get_current_weather(city):
    observation = mgr.weather_at_place(city)

    return observation.weather

cities = {
    "Київ" : "Kyiv, UA",
    "Чернівці" : "Chernivtsi, UA",
    "Припять" : "Pripyat, UA"
}


def get_forecast(city):
    forecast = mgr.forecast_at_place(city, 'daily')

    return forecast.will_be_clear_at(timestamps.tomorrow())

    w = get_current_weather([])


def get_markup() -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup()
    buttonA = types.InlineKeyboardButton('Київ', callback_data='Київ')
    buttonB = types.InlineKeyboardButton('Чернівці', callback_data='Чернівці')
    buttonC = types.InlineKeyboardButton('Припять', callback_data='Припять')

    markup.row(buttonA, buttonB, buttonC)
    return markup


@bot.message_handler(content_types=['text'])
def get_text_messages(message):



    if message.text == "/start":
        bot.send_message(message.from_user.id, "Вибери місто", reply_markup=get_markup())


@bot.callback_query_handler(func=lambda call: True)
def handle(call):
    bot.delete_message(call.message.chat.id, call.message.id)
    w = get_current_weather(cities[call.data])
    bot.send_message(
        call.message.chat.id,
        "Місто {city}: {weather}\nТемпература: {temp} °C\nШвидкість вітру: {wind} М/с".format(
            city=call.data,
            weather=str(w.detailed_status).title(),
            temp=w.temperature('celsius')['temp'],
            wind=w.wind()['speed']
        )
    )
    bot.send_message(call.message.chat.id, "Вибери місто", reply_markup=get_markup())
    bot.answer_callback_query(call.id)

bot.polling(none_stop=True, interval=0)
