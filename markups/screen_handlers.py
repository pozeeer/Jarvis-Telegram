from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


def get_work_with_screen_markup() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Получить скриншот экрана", "Получить скриншот веб-камеры")
    markup.add('Яркость на максимум', 'Яркость на минимум')
    markup.add('Вернуться в главное меню')
    return markup


def get_inline_markup_work_with_bright() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='Яркость плюс (число)', switch_inline_query_current_chat="Яркость плюс "))
    markup.add(
        InlineKeyboardButton(text='Яркость минус (число)', switch_inline_query_current_chat="Яркость минус "))
    markup.add(InlineKeyboardButton(text='Яркость на (число)', switch_inline_query_current_chat="Яркость на "))
    return markup
