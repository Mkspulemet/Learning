import telebot, wikipedia, re
from testing import *

db.connect()
Person.create_table(True)
db.close()

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


def history(message):
    db.connect()
    user = Person.create(name=int(message.from_user.id), mess=getwiki(message.text))
    user.save()
    # if not Person.select().where(Person(name=int(message.from_user.id), mess=getwiki(message.text))):
    #     new_user = Person.create(
    #         name=message.from_user.id,
    #         mess=getwiki(message.text),
    #     )
    #     new_user.save()
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
        # bot.send_message(message.chat.id, Person.mess)


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))
    # history(getwiki(message.text))
    # db.connect()
    # new_user = Person.create(name=int(message.from_user.id), mess=getwiki(message.text))
    # new_user.save()
    history(message)
    print(message.from_user.id)


# Запускаем бота
bot.polling(none_stop=True, interval=0)
