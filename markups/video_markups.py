from telebot.types import ReplyKeyboardMarkup


def get_work_with_video_markup() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Остановка/Запуск видео", "Полноразмерное видео/Не полноразмерное видео")
    markup.add("Громкость")
    markup.add("Перемотать назад", "Перемотать вперед")
    markup.add("Вернуться в главное меню")
    return markup


def get_work_with_volume_markup() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Остановка/Запуск видео", "Полноразмерное видео/Не полноразмерное видео")
    markup.add("Громкость")
    markup.add("Перемотать назад", "Перемотать вперед")
    markup.add("Вернуться в главное меню")
    return markup