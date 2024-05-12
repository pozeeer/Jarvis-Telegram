import ctypes

import pywintypes
import win32api
import win32con
from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardMarkup

from jarvis_telegram.markups.work_with_pc_markups import return_to_main_menu
from jarvis_telegram.markups.screen_resolution_markups import get_available_resolutions


# @bot.message_handler(regexp='Изменить разрешение экрана')
def get_current_screen_extensions(message: Message, bot: TeleBot):
    res = []
    i = 0
    try:
        while True:
            ds = win32api.EnumDisplaySettings(None, i)
            res.append(f"{ds.PelsWidth}x{ds.PelsHeight}")
            i += 1
    except:
        pass
    res = list(set(res))
    # for i in range(len(res)):
    #     markup.add(res[i])
    # markup.add("Отмена")
    markup = get_available_resolutions(res)
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    message_for_user = bot.send_message(
        message.chat.id,
        f'Какое разрешение экрана желаете установить?\nТекущее разрешение экрана: {screensize}',
        reply_markup=markup
    )
    bot.register_next_step_handler(message_for_user, change_screen_resolution, bot)


def change_screen_resolution(message: Message, bot: TeleBot):
    markup = return_to_main_menu()
    v = message.text
    if v == 'Отмена':
        bot.send_message(message.chat.id, f'Отменено', reply_markup=markup)
    else:
        v1 = v.split("x")
        devmode = pywintypes.DEVMODEType()
        devmode.PelsWidth = int(v1[0])
        devmode.PelsHeight = int(v1[1])
        devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
        win32api.ChangeDisplaySettings(devmode, 0)
        bot.send_message(message.chat.id, 'Успешно!', reply_markup=markup)


change_screen_handlers = {'Изменить разрешение экрана': get_current_screen_extensions}
