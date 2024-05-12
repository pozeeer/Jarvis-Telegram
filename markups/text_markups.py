from telebot.types import ReplyKeyboardMarkup


def get_work_with_text_markup() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Ввести текст", "Сменить раскладку")
    markup.add("Зажать клавишу +", "Сохранить документ")
    markup.add("Вернуться в главное меню")
    return markup


def enter_keyboard_markup() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("CTRL", "SHIFT", "ALT")
    markup.add("Вернуться в главное меню")
    return markup


def get_button_for_click() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("C", "V", "Z", "Y")
    markup.add("Отжать кнопку")
    return markup


def select_language() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Английский", "Русский")
    markup.add("Вернуться в главное меню")
    return markup


def select_action_with_input_text() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Стереть", "Стереть слово", "Стереть всё", "CTRL+Z")
    markup.row("Caps Lock", "Shift (С заглавной буквы)", "Enter (новый абзац)", "CTRL+Y")
    markup.row("Влево", "Вверх", "Вниз", "Вправо")
    markup.add("Скопировать слово", "Скопировать строку", "Вставить")
    markup.add("Назад")
    return markup
