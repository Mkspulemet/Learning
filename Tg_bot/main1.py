import re
import json
import telebot
import nltk
from telebot import TeleBot
from typing import List, Dict, Union
from dotenv import load_dotenv
import os
# импорт скриптов
from commands.help import help
from commands.hotel_commands import get_city
load_dotenv()
# BOT INFO: @hotelanalysisbot
TOKEN: str = os.getenv('TOKEN')
bot: TeleBot = telebot.TeleBot(TOKEN)
with open('botconfig.json', 'r', encoding='utf-8') as json_file:
    BOT_CONFIG: Dict[str, Union[Dict[str, Dict[str, Union[str, List]]], str]] = json.load(json_file)


def clean(text: str) -> str:
    """
    Function which is cleaning given text.
    :param text: text need to clean
    :return: cleaned text
    :rtype: str
    """
    text: str = text.lower()
    text = re.sub(r'[0-9]', '', text)
    return text


def get_answer(text: str) -> str:
    """
    Function which returns answer from different intents.
    :param text:
    :return: intent's answer
    :rtype: str
    """
    text: str = clean(text)
    for intent in BOT_CONFIG['intents']:
        if intent == 'commands':
            continue
        for example in BOT_CONFIG['intents'][intent]['example']:
            if nltk.edit_distance(text, example)/max(len(text), len(example)) * 100 < 40:
                return BOT_CONFIG['intents'][intent]['answer']
    else:
        return BOT_CONFIG['default']


@bot.message_handler(commands=['help', 'start'])
def main_commands_catcher(message) -> None:
    """
    Sends answer of commands to an user in a Telegram-chat: /start and /help.
    :param message: message-object from user
    """
    result: str = ''
    if message.text == '/start':
        result = 'Добро пожаловать!\nЯ помощник по подбору лучшего предложения в среде отелей для Вас\n'
    result += help(BOT_CONFIG)
    bot.send_message(message.from_user.id, result)


@bot.message_handler(commands=['lowprice', 'highprice', 'bestdeal'])
def hotel_commands(message) -> None:
    """
    Sends answer of commands to an user in a Telegram-chat: /lowprice, /highprice, /bestdeal.
    :param message: message-object from user
    """
    bot.send_message(message.from_user.id, 'Введите город, где будет проводится поиск.')
    bot.register_next_step_handler(message, get_city, message.text[1:], bot)


@bot.message_handler(content_types=['text'])
def text_catcher(message) -> None:
    """
    Main function which forces bot to work.
    :param message: text from user
    :return: None        print('Доступное кол-во отелей:', max_hotel_count)
    """
    reply: str = get_answer(message.text)
    bot.send_message(message.from_user.id, reply)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)