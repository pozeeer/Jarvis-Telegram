from telebot.types import ReplyKeyboardMarkup


def get_markup_with_sites(lst: list) -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for button in lst:
        markup.add(button)
    return markup
