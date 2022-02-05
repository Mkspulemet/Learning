from datetime import date, datetime
from unittest.mock import call

import telebot, wikipedia, re
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
import calendar
from testing import *

db.connect()
Person.create_table(True)
db.close()

# Создаем экземпляр бота
bot = telebot.TeleBot('5056695729:AAEFCytVriAqwrskJaFYKgWqs0H1nXRs2vE')
# Устанавливаем русский язык в Wikipedia
wikipedia.set_lang("ru")


querystring = {"adults1": "1", "pageNumber": "1", "pageSize": "10",
               "checkIn": str(),
               "checkOut": str(),
               "currency": "USD", "locale": "ru_RU"}


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


def history(message):
    db.connect()
    user = Person.create(name=int(message.from_user.id), mess=getwiki(message.text))
    user.save()
    db.close()


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')


# Функция, обрабатывающая команду /history
@bot.message_handler(commands=["history"])
def history_out(message, res=False):
    id = message.from_user.id
    for i in Person.select().where(Person.name == id):
        print(i)
        bot.send_message(message.chat.id, i.mess)


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))
    bot.send_message(message.chat.id, 'Введите дату заселения')
    bot.register_next_step_handler(message, start)
    # querystring["checkIn"] = None
    history(message)


# @bot.message_handler()
# def start(m):
#     calendar, step = DetailedTelegramCalendar(min_date=date.today()).build()
#     bot.send_message(m.chat.id,
#                      f"Select {LSTEP[step]}",
#                      reply_markup=calendar)
#
#
# @bot.callback_query_handler(func=DetailedTelegramCalendar.func())
# def cal(c):
#     result, key, step = DetailedTelegramCalendar(min_date=date.today()).process(c.data)
#     if not result and key:
#         print('qwerty')
#         bot.edit_message_text(f"Select {LSTEP[step]}",
#                               c.message.chat.id,
#                               c.message.message_id,
#                               reply_markup=key)
#     elif result:
#         bot.edit_message_text(f"{result}",
#                               c.message.chat.id,
#                               c.message.message_id)
#     return result






# Запускаем бота

current_shown_dates = {}
@bot.message_handler(commands=['calendar'])
def get_calendar(message):
    now = datetime.datetime.now() #Current date
    chat_id = message.chat.id
    date = (now.year, now.month)
    current_shown_dates[chat_id] = date #Saving the current date in a dict
    markup = create_calendar(now.year, now.month)
    bot.send_message(message.chat.id, "Пожалуйста, выберите дату", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data[0:13] == 'calendar-day-')
def get_day(call):
    chat_id = call.message.chat.id
    bot.register_next_step_handler(call, date_for)
def date_for(chat_id):
    saved_date = current_shown_dates.get(chat_id)
    if(saved_date is not None):
        day = call.data[13:]
        date = datetime.date(int(saved_date[0]), int(saved_date[1]), int(day))
        bot.send_message(chat_id, str(date))
        bot.answer_callback_query(call.id, text="Выбрана дата")
        return date
    else:
        bot.send_message(chat_id, 'Ошибка')
        pass

bot.polling(none_stop=True, interval=0)


