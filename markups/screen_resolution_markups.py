from telebot.types import ReplyKeyboardMarkup


def get_available_resolutions(resols: list) -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for resol in range(len(resols)):
        markup.add(resols[resol])
    markup.add("Отмена")
    return markup