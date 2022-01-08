<<<<<<< HEAD
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
=======
import telebot, wikipedia, re

# Создаем экземпляр бота
bot = telebot.TeleBot('5056695729:AAEFCytVriAqwrskJaFYKgWqs0H1nXRs2vE')
# Устанавливаем русский язык в Wikipedia
wikipedia.set_lang("ru")


# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую тысячу символов
        wikitext = ny.content[:1000]
        # Разделяем по точкам
        wikimas = wikitext.split('.')
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not ('==' in x):
                # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if (len((x.strip())) > 3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'В энциклопедии нет информации об этом'


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))


# Запускаем бота
bot.polling(none_stop=True, interval=0)
>>>>>>> origin/master
