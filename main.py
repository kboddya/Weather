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
    "Припять" : "Pripyat, UA",
    "Львів" : "Lviv, UA",
    "Тернопіль" : "Ternopil, UA",
    "Одеса" : "Odessa, UA",
    "Житомир" : "Zhytomyr, UA",
    "Полтава" : "Poltava, UA",
    "Кропивницкий" : "Kropyvnytskyi, UA ",
    "Івано-Франківськ" : "Ivano-Frankivsk, UA",
    "Харків" : "Kharkiv, UA ",
    "Хмельницкий" : "Khmelnytskyi, UA"

}


def get_forecast(city):
    forecast = mgr.forecast_at_place(city, 'daily')
    answer = forecast.will_be_clear_at(timestamps.tomorrow())

    return forecast.will_be_clear_at(timestamps.tomorrow())

    w = get_current_weather([])


def get_markup() -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup()
    buttonA = types.InlineKeyboardButton('Київ', callback_data='Київ')
    buttonB = types.InlineKeyboardButton('Чернівці', callback_data='Чернівці')
    buttonC = types.InlineKeyboardButton('Припять', callback_data='Припять')
    buttonD = types.InlineKeyboardButton('Львів', callback_data='Львів')
    buttonE = types.InlineKeyboardButton('Тернопіль', callback_data='Тернопіль')
    buttonF = types.InlineKeyboardButton('Одеса', callback_data='Одеса')
    buttonG = types.InlineKeyboardButton('Житомир', callback_data='Житомир')
    buttonH = types.InlineKeyboardButton('Полтава', callback_data='Полтава')
    buttonI = types.InlineKeyboardButton('Кропивницкий', callback_data='Кропивницкий')
    buttonJ = types.InlineKeyboardButton('Івано-Франківськ', callback_data='Івано-Франківськ')
    buttonK = types.InlineKeyboardButton('Харків', callback_data='Харків')
    buttonL = types.InlineKeyboardButton('Хмельницкий', callback_data='Хмельницкий')


    markup.row(buttonA, buttonB, buttonC)
    markup.row(buttonD, buttonE, buttonF)
    markup.row(buttonG, buttonH, buttonI)
    markup.row(buttonJ, buttonK, buttonL)
    return markup


@bot.message_handler(content_types=['text'])
def get_text_messages(message):



    if message.text == "/startf":
        bot.send_message(message.from_user.id, "Вибери місто", reply_markup=get_markup())


@bot.callback_query_handler(func=lambda call: True)
def handle(call):
    bot.delete_message(call.message.chat.id, call.message.id)
    w = get_current_weather(cities[call.data])
    bot.send_message(
        call.message.chat.id,
        "В місті {city} зараз {weather}\n{text_temp} {temp}°C, {f}°F\n{text_max} {max}°C, {fmax}°F\n{text_min} {min}°C, {fmin}°F\n{text_wind} {wind} М/с".format(
            city=call.data,
            weather=str(w.detailed_status).title(),
            temp=round(w.temperature('celsius') ['temp']),
            f=round(w.temperature('fahrenheit') ['temp']),
            wind=round(w.wind()['speed']),
            max=round(w.temperature('celsius') ['temp_max']),
            min=round(w.temperature('celsius') ['temp_min']),
            fmax=round(w.temperature('fahrenheit') ['temp_max']),
            fmin=round(w.temperature('fahrenheit') ['temp_min']),
            text_temp='Температура повітря',
            text_max='Повітря прогріється максимум до',
            text_min='Мінімальна температура повітря',
            text_wind='Середня швидкість вітру'
        )
    )
    bot.send_message(call.message.chat.id, "Вибери місто", reply_markup=get_markup())
    bot.answer_callback_query(call.id)

def get_markups() -> types.InlineKeyboardMarkup:
    markup = types.InlineKeyboardMarkup()
    buttonA = types.InlineKeyboardButton('Київ', callback_data='Київ')
    buttonB = types.InlineKeyboardButton('Чернівці', callback_data='Чернівці')
    buttonC = types.InlineKeyboardButton('Припять', callback_data='Припять')
    buttonD = types.InlineKeyboardButton('Львів', callback_data='Львів')
    buttonE = types.InlineKeyboardButton('Тернопіль', callback_data='Тернопіль')
    buttonF = types.InlineKeyboardButton('Одеса', callback_data='Одеса')
    buttonG = types.InlineKeyboardButton('Житомир', callback_data='Житомир')
    buttonH = types.InlineKeyboardButton('Полтава', callback_data='Полтава')
    buttonI = types.InlineKeyboardButton('Кропивницкий', callback_data='Кропивницкий')
    buttonJ = types.InlineKeyboardButton('Івано-Франківськ', callback_data='Івано-Франківськ')
    buttonK = types.InlineKeyboardButton('Харків', callback_data='Харків')
    buttonL = types.InlineKeyboardButton('Хмельницкий', callback_data='Хмельницкий')


    markup.row(buttonA, buttonB, buttonC)
    markup.row(buttonD, buttonE, buttonF)
    markup.row(buttonG, buttonH, buttonI)
    markup.row(buttonJ, buttonK, buttonL)
    return markup
@bot.message_handler(content_types=['text'])
def get_text_messag(message):
    if message.text == "/startc":
        bot.send_message(message.from_user.id, "Вибери місто", reply_markup=get_markups())


@bot.callback_query_handler(func=lambda call: True)
def handled(call):
    bot.delete_message(call.message.chat.id, call.message.id)
    w = get_current_weather(cities[call.data])
    bot.send_message(
        call.message.chat.id,
        "В місті {city} зараз {weather}\n{text_temp} {f}°F\n{text_max}  {fmax}°F\n{text_min} {fmin}°F\n{text_wind} {wind} М/с".format(
            city=call.data,
            weather=str(w.detailed_status).title(),
            temp=round(w.temperature('celsius') ['temp']),
            f=round(w.temperature('fahrenheit') ['temp']),
            wind=round(w.wind()['speed']),
            max=round(w.temperature('celsius') ['temp_max']),
            min=round(w.temperature('celsius') ['temp_min']),
            fmax=round(w.temperature('fahrenheit') ['temp_max']),
            fmin=round(w.temperature('fahrenheit') ['temp_min']),
            text_temp='Температура повітря',
            text_max='Повітря прогріється максимум до',
            text_min='Мінімальна температура повітря',
            text_wind='Середня швидкість вітру'
        )
    )
    bot.send_message(call.message.chat.id, "Вибери місто", reply_markup=get_markups())
    bot.answer_callback_query(call.id)



bot.polling(none_stop=True, interval=0)
