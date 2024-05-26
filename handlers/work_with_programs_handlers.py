import telebot
from telebot import types
import winapps
import os

from telebot.types import Message
from telebot import TeleBot


# @bot.message_handler(regexp='Работа с программами')
# def work_with_programs(message: Message, bot: TeleBot):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     button1 = types.KeyboardButton("Открыть программу")
#     markup.add(button1)
#     markup.add("Вернуться в главное меню")
#     bot.send_message(message.chat.id, text="Выберите действие ", reply_markup=markup)
#
#
# # @bot.message_handler(regexp='Открыть программу')
# def open_programs(message: Message, bot: TeleBot):
#     markup = InlineKeyboardMarkup()
#     markup.add(InlineKeyboardButton(text='1 страница приложений', callback_data='1in'))
#     markup.add(InlineKeyboardButton(text='2 страница приложений', callback_data='2in'))
#     markup.add(InlineKeyboardButton(text='3 страница приложений', callback_data='3in'))
#     markup.add(InlineKeyboardButton(text='4 страница приложений', callback_data='4in'))
#     markup.add(InlineKeyboardButton(text='5 страница приложений', callback_data='5in'))
#     markup.add(InlineKeyboardButton(text='6 страница приложений', callback_data='6in'))
#
#     # @bot.callback_query_handler(func=lambda call: True)
#     def callback_query(call: CallbackQuery, bot: TeleBot):
#         req = call.data.split('_')
#         markup = InlineKeyboardMarkup()
#         if req[0] == '1in' or req[0] == '1off':
#             x = 0
#             markup.add(InlineKeyboardButton(text='<- Назад', callback_data='off'))
#             for app in winapps.list_installed():
#                 markup.add(InlineKeyboardButton(text=app.name, callback_data="programs " + str(x)))
#                 x += 1
#                 if x == 20:
#                     markup.add(InlineKeyboardButton(text='Вперёд ->', callback_data='2in'))
#                     x = 0
#                     break
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg.message_id, text=f"1 страница",
#                                   reply_markup=markup)
#
#         elif req[0] == '2in' or req[0] == '2off':
#             x = 0
#             markup.add(InlineKeyboardButton(text='<- Назад', callback_data='1off'))
#             for app in winapps.list_installed():
#                 if x >= 20:
#                     markup.add(InlineKeyboardButton(text=app.name, callback_data="programs " + str(x)))
#                 x += 1
#                 if x == 40:
#                     markup.add(InlineKeyboardButton(text='Вперёд ->', callback_data='3in'))
#                     x = 0
#                     break
#             bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text=f"2 страница",
#                                   reply_markup=markup)
#
#         elif req[0] == '3in' or req[0] == '3off':
#             x = 0
#             markup.add(InlineKeyboardButton(text='<- Назад', callback_data='2off'))
#             for app in winapps.list_installed():
#                 if x >= 40:
#                     markup.add(InlineKeyboardButton(text=app.name, callback_data="programs " + str(x)))
#                 x += 1
#                 if x == 60:
#                     markup.add(InlineKeyboardButton(text='Вперёд ->', callback_data='4in'))
#                     x = 0
#                     break
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg.message_id, text=f"3 страница",
#                                   reply_markup=markup)
#
#         elif req[0] == '4in' or req[0] == '4off':
#             x = 0
#             markup.add(InlineKeyboardButton(text='<- Назад', callback_data='3off'))
#             for app in winapps.list_installed():
#                 if x >= 60:
#                     markup.add(InlineKeyboardButton(text=app.name, callback_data="programs " + str(x)))
#                 x += 1
#                 if x == 80:
#                     markup.add(InlineKeyboardButton(text='Вперёд ->', callback_data='5in'))
#                     x = 0
#                     break
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg.message_id, text=f"4 страница",
#                                   reply_markup=markup)
#
#         elif req[0] == '5in' or req[0] == '5off':
#             x = 0
#             markup.add(InlineKeyboardButton(text='<- Назад', callback_data='4off'))
#             for app in winapps.list_installed():
#                 if x >= 80:
#                     markup.add(InlineKeyboardButton(text=app.name, callback_data="programs " + str(x)))
#                 x += 1
#                 if x == 100:
#                     markup.add(InlineKeyboardButton(text='Вперёд ->', callback_data='6in'))
#                     x = 0
#                     break
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg.message_id, text=f"5 страница",
#                                   reply_markup=markup)
#
#         elif req[0] == '6in' or req[0] == '6off':
#             x = 0
#             markup.add(InlineKeyboardButton(text='<- Назад', callback_data='5off'))
#             for app in winapps.list_installed():
#                 if x >= 100:
#                     markup.add(InlineKeyboardButton(text=app.name, callback_data="programs " + str(x)))
#                 x += 1
#                 if x == 120:
#                     x = 0
#                     break
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg.message_id, text=f"6 страница",
#                                   reply_markup=markup)
#
#         elif req[0] == 'off':
#             markup = InlineKeyboardMarkup()
#             markup.add(InlineKeyboardButton(text='1 страница приложений', callback_data='1in'))
#             markup.add(InlineKeyboardButton(text='2 страница приложений', callback_data='2in'))
#             markup.add(InlineKeyboardButton(text='3 страница приложений', callback_data='3in'))
#             markup.add(InlineKeyboardButton(text='4 страница приложений', callback_data='4in'))
#             markup.add(InlineKeyboardButton(text='5 страница приложений', callback_data='5in'))
#             markup.add(InlineKeyboardButton(text='6 страница приложений', callback_data='6in'))
#             bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
#                                   text=f"Выберите название приложения",
#                                   reply_markup=markup)
#
#         elif req[0].startswith("programs"):
#             program = int(req[0].replace('programs ', ''))
#             x = 0
#             markup = InlineKeyboardMarkup()
#             for app in winapps.list_installed():
#                 if x == program:
#                     fileExt = r".exe"
#                     y = [os.path.join(app.install_location, _) for _ in os.listdir(app.install_location) if
#                          _.endswith(fileExt)]
#                     bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg.message_id,
#                                           text=f"Открытие. . .",
#                                           reply_markup=markup)
#                     os.startfile(y[0]) if y[0] != "unins000.exe" else os.startfile(y[1])
#                     break
#                 x += 1
#
#         else:
#             p = 0
#
#     msg = bot.send_message(message.chat.id, 'Выберите название приложения', reply_markup=markup)
#
#
# work_with_programs = {
#     r'(?i)Работа с программами': work_with_programs, r'(?i)Открыть программу': open_programs,
# }


# TOKEN = "7018680254:AAHcFU4VECtrz9oBAsY41d1W7mK6qQMwLG4"
# bot = telebot.TeleBot(TOKEN)


# @bot.message_handler(commands=['start'])

def get_work_with_programs_markup(message: Message, bot: TeleBot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Работа с программами'))
    bot.reply_to(message, "Выбери действие", reply_markup=markup)


# @bot.message_handler(func=lambda message: message.text == 'Работа с программами')
def show_installed_apps(message: Message, bot: TeleBot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add("Открыть программу")
    bot.send_message(message.chat.id, "Выбери действие", reply_markup=markup)


# @bot.message_handler(func=lambda message: message.text == 'Открыть программу')
def select_app_for_open(message: Message, bot: TeleBot):
    apps = winapps.list_installed()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for app in apps:
        markup.add(types.KeyboardButton(app.name))
    message_for_user = bot.send_message(message.chat.id, "Выберите, что нужно открыть, сэр", reply_markup=markup)
    bot.register_next_step_handler(message_for_user, open_app, bot)


# @bot.message_handler(func=lambda message: message.text in [app.name for app in winapps.list_installed()])
def open_app(message: Message, bot: TeleBot):
    app_name = message.text
    app_info = next((app for app in winapps.list_installed() if app.name == app_name), None)
    if app_info:
        install_location = app_info.install_location
        if install_location is not None and os.path.exists(install_location):
            for root, dirs, files in os.walk(install_location):
                for file in files:
                    if file.endswith(".exe"):
                        executable_path = os.path.join(root, file)
                        try:
                            os.startfile(executable_path)
                            bot.reply_to(message, f"Приложение '{app_name}' открыто, сэр")
                        except OSError as e:
                            if e.winerror == 1223:
                                bot.reply_to(message,
                                             f"Операция открытия приложения {app_name} была отменена пользователем, сэр")
                            else:
                                bot.reply_to(message, f"Ошибка при открытии приложения {app_name}, сэр")
                        return
            bot.reply_to(message, f"Не удалось найти исполняемый файл для {app_name}, сэр")
        else:
            bot.reply_to(message, f"Не удалось найти директорию установки для {app_name}, сэр")
    else:
        bot.reply_to(message, f"Приложение {app_name} не найдено, сэр")


work_with_programs = {r'(?i)Работа с программами': show_installed_apps, r'(?i)Открыть программу': select_app_for_open}
# bot.polling(none_stop=True)
