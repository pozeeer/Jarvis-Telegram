from telebot.types import ReplyKeyboardMarkup


def get_user_confirmation() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Да", "Нет")
    return markup


def return_to_main_menu() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Вернуться в главное меню")
    return markup


def get_work_with_pc_markups() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Свернуть все окна", "Развернуть все окна")
    markup.add("Закрытие окна", "Поменять фон рабочего стола")
    markup.add('Информация', 'Вывести сообщение на экран', 'Произнести аудио')
    markup.add('Комплектующие', 'Состояние', 'Мониторинг')
    markup.add("Выключить пк...", 'Перезагрузить пк', 'Спящий режим')
    markup.add("Вернуться в главное меню")
    return markup


def get_turn_off_markup() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Выключить пк", "Поставить таймер на выключение", "Остановить таймер")
    markup.add("Вернуться в главное меню")
    return markup


def get_tun_off_timer_markup() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("1", "2", "5", '10', '15', '20')
    markup.row("30", "40", "50", '60', '90', '120')
    markup.add("Вернуться в главное меню")
    return markup


def get_warning_markup() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Вывести важное сообщение')
    markup.add('Вывести предупреждение')
    markup.add('Вывести информационное сообщение')
    markup.add("Вернуться в главное меню")
    return markup


def get_monitoring_markup() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('5', '10', '20', '40', '60', '120')
    return markup
