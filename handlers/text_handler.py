import ctypes

import keyboard
import py_win_keyboard_layout
from telebot.types import Message, ReplyKeyboardMarkup
from telebot import TeleBot

from jarvis_telegram.markups.text_markups import *
from jarvis_telegram.markups.menu_markup import get_menu_markup


# @bot.message_handler(regexp='Работа с текстом')
def work_with_text(message: Message, bot: TeleBot):
    # if not jarvis_func[5]:
    #     bot.send_message(message.chat.id, 'Данный раздел не входит в функции подписки!')
    #     return
    markup = get_work_with_text_markup()
    bot.send_message(message.chat.id, 'Сделано!', reply_markup=markup)


def _change_keyboard_layout_to_english(telegram_bot: TeleBot, message: Message):
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
    telegram_bot.send_message(message.from_user.id, "Теперь английская раскладка")


def _change_keyboard_layout_to_russian(telegram_bot: TeleBot, message: Message):
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x4190419)
    telegram_bot.send_message(message.from_user.id, "Теперь русская раскладка")


# @bot.message_handler(regexp='Сменить раскладку')
def change_the_layout(message: Message, bot: TeleBot):
    user32_library = ctypes.windll.LoadLibrary("user32.dll")
    get_keyboard_layout_function = getattr(user32_library, "GetKeyboardLayout")
    current_keyboard_layout_hex_code = hex(get_keyboard_layout_function(0))

    if current_keyboard_layout_hex_code == '0x4190419':
        _change_keyboard_layout_to_english(bot, message)
    elif current_keyboard_layout_hex_code == '0x4090409':
        _change_keyboard_layout_to_russian(bot, message)


# @bot.message_handler(regexp='Зажать клавишу +')
def enter_keyboard(message: Message, bot: TeleBot):
    markup = enter_keyboard_markup()

    text_for_user = bot.send_message(message.chat.id, 'Выберите какую клавишу, либо введите сами', reply_markup=markup)
    bot.register_next_step_handler(text_for_user, press_button, bot)


# v1231 = str("Привет")


def press_button(message: Message, bot: TeleBot):
    # global v1231
    text_from_user = message.text
    if text_from_user == "Вернуться в главное меню":
        menu_markup = get_menu_markup()
        bot.send_message(chat_id=message.chat.id, text="Сделано!", reply_markup=menu_markup)
    else:
        keyboard.press(text_from_user)
        markup = get_button_for_click()
        text_for_user = bot.send_message(message.chat.id,
                                         'Клавиша зажата, вы можете нажимать на любые кнопки пока она зажата,'
                                         'просто отправьте букву АНГЛИЙСКОЙ кнопки для нажатия',
                                         reply_markup=markup)
        bot.register_next_step_handler(
            text_for_user, check_button_condition, text_from_user
        )


def check_button_condition(message: Message, bot: TeleBot, button: str):
    # global v1231
    text_from_user = str(message.text)
    if text_from_user == "Отжать кнопку":
        keyboard.release(button)
        bot.send_message(message.chat.id, 'Клавиша отжата')
        # с = send_welcomeTo(message)
        menu_markup = get_menu_markup()
        bot.send_message(chat_id=message.chat.id, text="Сделано!", reply_markup=menu_markup)
    else:
        keyboard.send(button)
        text_for_user = bot.send_message(message.chat.id, 'Клавиша нажата')
        bot.register_next_step_handler(text_for_user, check_button_condition, bot)


# @bot.message_handler(regexp='Сохранить документ')
def save_document(message: Message, bot: TeleBot):
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
    keyboard.press("ctrl")
    keyboard.send("s")
    keyboard.release("ctrl")


# @bot.message_handler(regexp='Ввести текст')
def enter_text(message: Message, bot: TeleBot):
    markup = select_language()
    text_for_user = bot.send_message(message.chat.id, 'Выберите язык ввода', reply_markup=markup)
    bot.register_next_step_handler(text_for_user, select_text_for_text)
    bot.register_next_step_handler(text_for_user, work_with_input_text, bot)


def select_text_for_text(message: Message):
    if message.text == "Английский":
        py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
    elif message.text == "Русский":
        py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x4190419)


def work_with_input_text(message: Message, bot: TeleBot):
    markup = select_action_with_input_text()
    # markup = ReplyKeyboardMarkup(resize_keyboard=True)
    # markup.row("Стереть", "Стереть слово", "Стереть всё", "CTRL+Z")
    # markup.row("Caps Lock", "Shift (С заглавной буквы)", "Enter (новый абзац)", "CTRL+Y")
    # markup.row("Влево", "Вверх", "Вниз", "Вправо")
    # markup.add("Скопировать слово", "Скопировать строку", "Вставить")
    # markup.add("Назад")
    text_for_user = bot.send_message(message.chat.id,
                                     'Вводите текст и он будет вводиться на пк! ',
                                     reply_markup=markup)
    bot.register_next_step_handler(text_for_user, manage_action_with_text, bot)


def manage_action_with_text(message: Message, bot: TeleBot):
    match message.text:
        case "Стереть слово" | "стереть слово":
            erase_word(message, bot)
        case "Скопировать слово" | "скопировать":
            copy_word(message, bot)
        case "Скопировать строку" | "скопировать строку":
            line_copy(message, bot)
        case "CTRL+Z" | "Отмена":
            cancel_last_action(message, bot)
        case "CTRL+Y" | "Отмена1":
            delete_line(message, bot)
        case "Вставить" | "вставить":
            paste(message, bot)
        case "вверх" | "Вверх":
            click_arrow_up(message, bot)
        case "Влево" | "влево":
            click_arrow_left(message, bot)
        case "Вниз" | "вниз":
            click_arrow_down(message, bot)
        case "Вправо" | "вправо":
            click_arrow_right(message, bot)
        case "Enter (новый абзац)" | "Enter":
            click_enter_for_new_paragraph(message, bot)
        case "Caps Lock":
            click_caps_lock(message, bot)
        case "Shift" | "Shift (С заглавной буквы)":
            clamp_shift(message, bot)
        case "Стереть" | "стереть":
            erase(message, bot)
        case "Стереть все" | "стереть все" | "Стереть всё" | "стереть всё":
            erase_all(message, bot)
        case "Назад":
            backward_from_text_input(message, bot)
        case message.text:
            # x1 = len(message.text)
            # keyboard.send(" ")
            # for i in range(x1):
            #     keyboard.send(x[c])
            #     c += 1
            keyboard.write(message.text, delay=0.2)
            message_for_user = bot.send_message(message.chat.id, 'Введено!')
            bot.register_next_step_handler(message_for_user, manage_action_with_text, bot)


def erase_word(message: Message, bot: TeleBot):
    # if x == "Стереть слово" or x == "стереть слово":
    keyboard.press("shift")
    keyboard.press("ctrl")
    keyboard.send("left")
    keyboard.release("shift")
    keyboard.release("ctrl")
    keyboard.send("backspace")
    message_for_user = bot.send_message(message.chat.id, 'Выполнено!')
    bot.register_next_step_handler(message_for_user, manage_action_with_text, bot)


# @bot.message_handler(regexp=r'(?i)Скопировать слово')
def copy_word(message: Message, bot: TeleBot):
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
    keyboard.press("shift")
    keyboard.press("ctrl")
    keyboard.send("left")
    keyboard.release("shift")
    keyboard.release("ctrl")
    keyboard.press("ctrl")
    keyboard.send("c")
    keyboard.release("ctrl")
    message_for_user = bot.send_message(message.chat.id, 'Скопировано!')
    bot.register_next_step_handler(message_for_user, manage_action_with_text, bot)


# @bot.message_handler(regexp=r'(?i)скопировать строку')
def line_copy(message: Message, bot: TeleBot):
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
    keyboard.press("shift")
    keyboard.press("ctrl")
    keyboard.send("up")
    keyboard.release("shift")
    keyboard.release("ctrl")
    keyboard.press("ctrl")
    keyboard.send("c")
    keyboard.release("ctrl")
    message_for_user = bot.send_message(message.chat.id, 'Скопировано!')
    bot.register_next_step_handler(message_for_user, manage_action_with_text, bot)


# @bot.message_handler(regexp=r'(?i)CTRL+Z')
def cancel_last_action(message: Message, bot: TeleBot):
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
    keyboard.press("ctrl")
    keyboard.send("z")
    keyboard.release("ctrl")
    text_for_user = bot.send_message(message.chat.id, 'Выполнено!')
    bot.register_next_step_handler(text_for_user, manage_action_with_text, bot)


# @bot.message_handler(regexp=r'(?i)CTRL+Y')
def delete_line(message: Message, bot: TeleBot):
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
    keyboard.press("ctrl")
    keyboard.send("y")
    keyboard.release("ctrl")
    text_for_user = bot.send_message(message.chat.id, 'Выполнено!')
    bot.register_next_step_handler(text_for_user, manage_action_with_text, bot)


# @bot.message_handler(regexp=r'(?i)Вставить')
def paste(message: Message, bot: TeleBot):
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
    keyboard.press("ctrl")
    keyboard.send("v")
    keyboard.release("ctrl")
    text_for_user = bot.send_message(message.chat.id, 'Выполнено!')
    bot.register_next_step_handler(text_for_user, manage_action_with_text, bot)


def click_arrow_up(message: Message, bot: TeleBot):
    keyboard.send("up")
    text_for_user = bot.send_message(message.chat.id, 'Вы уже выше!')
    bot.register_next_step_handler(text_for_user, manage_action_with_text, bot)


def click_arrow_left(message: Message, bot: TeleBot):
    keyboard.send("left")
    text_for_user = bot.send_message(message.chat.id, 'Вы уже левее!')
    bot.register_next_step_handler(text_for_user, manage_action_with_text, bot)


def click_arrow_down(message: Message, bot: TeleBot):
    keyboard.send("down")
    text_for_user = bot.send_message(message.chat.id, 'Вы уже ниже!')
    bot.register_next_step_handler(text_for_user, manage_action_with_text, bot)


def click_arrow_right(message: Message, bot: TeleBot):
    keyboard.send("right")
    text_for_user = bot.send_message(message.chat.id, 'Вы уже правее!')
    bot.register_next_step_handler(text_for_user, manage_action_with_text, bot)


# Enter (новый абзац)
def click_enter_for_new_paragraph(message: Message, bot: TeleBot):
    keyboard.send("Enter")
    message_for_user = bot.send_message(message.chat.id, 'Нажато!')
    bot.register_next_step_handler(message_for_user, manage_action_with_text, bot)


def click_caps_lock(message: Message, bot: TeleBot):
    keyboard.send("CAPS LOCK")
    message_for_user = bot.send_message(message.chat.id, 'Нажато!')
    bot.register_next_step_handler(message_for_user, manage_action_with_text, bot)


def clamp_shift(message: Message, bot: TeleBot):
    message_for_user = bot.send_message(message.chat.id, 'Вводите текст и он будет вводиться на пк! ')
    bot.register_next_step_handler(message_for_user, manage_action_with_text, bot)


def erase(message: Message, bot: TeleBot):
    keyboard.send("backspace")
    message_for_user = bot.send_message(message.chat.id, 'Уже сделано!')
    bot.register_next_step_handler(message_for_user, manage_action_with_text, bot)


def erase_all(message: Message, bot: TeleBot):
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
    keyboard.press("ctrl")
    keyboard.send("a")
    keyboard.release("ctrl")
    keyboard.send("backspace")
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x4190419)
    massage_for_user = bot.send_message(message.chat.id, 'Сделано!')
    bot.register_next_step_handler(massage_for_user, manage_action_with_text, bot)


def backward_from_text_input(message: Message, bot: TeleBot):
    massage_for_user = bot.send_message(message.chat.id, 'Сделано!')
    bot.register_next_step_handler(massage_for_user, work_with_text, bot)


def fuction_6(message: Message, bot: TeleBot):
    x = message.text
    c = 0
    x1 = len(x)
    x1 = x1 - 1
    keyboard.send(" ")
    keyboard.press("shift")
    keyboard.send(x[c])
    keyboard.release("shift")
    c = 1
    for i in range(x1):
        keyboard.send(x[c])
        c += 1
    message_for_user = bot.send_message(message.chat.id, 'Введено!')
    bot.register_next_step_handler(message_for_user, manage_action_with_text, bot)


text_handlers = {
    r'(?i)Работа с текстом': work_with_text, r'(?i)Сменить раскладку': change_the_layout,
    r'(?i)Зажать клавишу +': enter_keyboard, r'(?i)Сохранить документ': save_document,
    r'(?i)Ввести текст': enter_text}

# text_handlers = {
# : , r'(?i)Сменить раскладку': change_the_layout,
# r'(?i)Зажать клавишу +': enter_keyboard,
# fuction_1, fuction_2, r'(?i)Сохранить документ': save_document, r'(?i)Ввести текст': enter_text, fuction_4, fuction_5, fuction_6
# }
# def function_5(message: Message, bot: TeleBot):
#     x = message.text
#     if x == "Стереть слово" or x == "стереть слово":
#         keyboard.press("shift")
#         keyboard.press("ctrl")
#         keyboard.send("left")
#         keyboard.release("shift")
#         keyboard.release("ctrl")
#         keyboard.send("backspace")
#         x = bot.send_message(message.chat.id, 'Выполнено!')
#         bot.register_next_step_handler(x, st11)
#     elif x == "Скопировать слово" or x == "скопировать":
#         py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
#         keyboard.press("shift")
#         keyboard.press("ctrl")
#         keyboard.send("left")
#         keyboard.release("shift")
#         keyboard.release("ctrl")
#         keyboard.press("ctrl")
#         keyboard.send("c")
#         keyboard.release("ctrl")
#         x = bot.send_message(message.chat.id, 'Скопировано!')
#         bot.register_next_step_handler(x, st11)
#     elif x == "Скопировать строку" or x == "скопировать строку":
#         py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
#         keyboard.press("shift")
#         keyboard.press("ctrl")
#         keyboard.send("up")
#         keyboard.release("shift")
#         keyboard.release("ctrl")
#         keyboard.press("ctrl")
#         keyboard.send("c")
#         keyboard.release("ctrl")
#         x = bot.send_message(message.chat.id, 'Скопировано!')
#         bot.register_next_step_handler(x, st11)
#     elif x == "CTRL+Z" or x == "Отмена":
#         py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
#         keyboard.press("ctrl")
#         keyboard.send("z")
#         keyboard.release("ctrl")
#         x = bot.send_message(message.chat.id, 'Выполнено!')
#         bot.register_next_step_handler(x, st11)
#     elif x == "CTRL+Y" or x == "Отмена1":
#         py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
#         keyboard.press("ctrl")
#         keyboard.send("y")
#         keyboard.release("ctrl")
#         x = bot.send_message(message.chat.id, 'Выполнено!')
#         bot.register_next_step_handler(x, st11)
#     elif x == "Вставить" or x == "вставить":
#         py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
#         keyboard.press("ctrl")
#         keyboard.send("v")
#         keyboard.release("ctrl")
#         x = bot.send_message(message.chat.id, 'Выполнено!')
#         bot.register_next_step_handler(x, st11)
#     elif x == "вверх" or x == "Вверх":
#         keyboard.send("up")
#         x = bot.send_message(message.chat.id, 'Вы уже выше!')
#         bot.register_next_step_handler(x, st11)
#     elif x == "Влево" or x == "влево":
#         keyboard.send("left")
#         x = bot.send_message(message.chat.id, 'Вы уже левее!')
#         bot.register_next_step_handler(x, st11)
#     elif x == "Вниз" or x == "вниз":
#         keyboard.send("down")
#         x = bot.send_message(message.chat.id, 'Вы уже ниже!')
#         bot.register_next_step_handler(x, st11)
#     elif x == "Вправо" or x == "вправо":
#         keyboard.send("right")
#         x = bot.send_message(message.chat.id, 'Вы уже правее!')
#         bot.register_next_step_handler(x, st11)
#     elif x == "Enter (новый абзац)" or x == "Enter":
#         keyboard.send("Enter")
#         x = bot.send_message(message.chat.id, 'Нажато!')
#         bot.register_next_step_handler(x, st11)
#     elif x == "Caps Lock":
#         keyboard.send("CAPS LOCK")
#         x = bot.send_message(message.chat.id, 'Нажато!')
#         bot.register_next_step_handler(x, st11)
#     elif x == "Shift" or x == "Shift (С заглавной буквы)":
#         x = bot.send_message(message.chat.id, 'Вводите текст и он будет вводиться на пк! ')
#         bot.register_next_step_handler(x, st112)
#     elif x == "Стереть" or x == "стереть":
#         keyboard.send("backspace")
#         x = bot.send_message(message.chat.id, 'Уже сделано!')
#         bot.register_next_step_handler(x, st11)
#     elif x == "Стереть все" or x == "стереть все" or x == "Стереть всё" ox == "стереть всё":
#         py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
#         keyboard.press("ctrl")
#         keyboard.send("a")
#         keyboard.release("ctrl")
#         keyboard.send("backspace")
#         py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x4190419)
#         x = bot.send_message(message.chat.id, 'Сделано!')
#         bot.register_next_step_handler(x, st11)
#     elif x == "Назад":
#         x = bot.send_message(message.chat.id, 'Нажмите повторно, пожалуйста!')
#         bot.register_next_step_handler(x, send_welcomErt)
#     else:
#         с = 0
#         x1 = len(x)
#         keyboard.send(" ")
#         for i in range(x1):
#             keyboard.send(x[с])
#             с = с + 1
#         x = bot.send_message(message.chat.id, 'Введено!')
#         bot.register_next_step_handler(x, st11)
#
# @bot.message_handler(regexp='Работа с текстом')
#     def send_welcomErt(message):
#         if not jarvis_func[5]:
#             bot.send_message(message.chat.id, 'Данный раздел не входит в функции подписки!')
#             return
#         markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
#         markup.add("Ввести текст", "Сменить раскладку")
#         markup.add("Зажать клавишу +", "Сохранить документ")
#         markup.add("Вернуться в главное меню")
#         bot.send_message(message.chat.id, 'Сделано!', reply_markup=markup)
