import threading

from telebot.types import ReplyKeyboardMarkup

from main import jfv


def get_menu_markup() -> ReplyKeyboardMarkup:
    my_thread = threading.Thread(target=jfv)
    my_thread.start()
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Работа с экраном", "Работа с пк", "Ввести команду в консоль")
    markup.add('Работа в интернете', "Jarvis Ai")
    markup.add("Работа с программами", "Работа с папками и файлами пк", "Почисти пк от не нужных файлов")
    markup.add('Автоматическое написание текста', "Работа с видео и фильмами", "Изменить разрешение экрана")
    markup.add("Работа с мышкой", "Работа с текстом")
    markup.add('Остановить бота', 'Перезапустить бота')
    return markup
    # bot.send_message(message.chat.id, 'Сделано!', reply_markup=markup)

def get_cancel_button()-> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)