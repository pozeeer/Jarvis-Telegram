from telebot.types import ReplyKeyboardMarkup


def select_distance() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("1", "2", "5", "10", "15", "20")
    markup.add("Назад")
    return markup


def select_mouse_option() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Нажатие ЛКМ", "Вверх", "Нажатие ПКМ")
    markup.add("Влево", "", "Вправо")
    markup.add("Прокрутка вниз", "Вниз", "Прокрутка вверх")
    markup.add("Вернуться в главное меню")
    return markup


def select_mouse_function() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Нажатие ЛКМ", "Вверх", "Нажатие ПКМ")
    markup.add("Влево", "", "Вправо")
    markup.add("Прокрутка вниз", "Вниз", "Прокрутка вверх")
    markup.add("Вернуться в главное меню")
    markup.row("Зажатие ЛКМ на 5 секунд", "Зажатие ПКМ на 5 секунд")
    return markup