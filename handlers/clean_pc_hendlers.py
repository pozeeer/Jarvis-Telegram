import os
import subprocess
import tempfile

from telebot.types import Message
from telebot import TeleBot

from jarvis_telegram.markups.work_with_pc_markups import get_user_confirmation, return_to_main_menu
from languges import ERRORS


# @bot.message_handler(regexp='Почисти пк от не нужных файлов')
def clean_out_of_junk_files(message: Message, bot: TeleBot):
    markup = get_user_confirmation()
    bot.send_message(message.chat.id, 'Начинаю очистку. . .')
    try:
        del_dir = tempfile.gettempdir()
        pObj = subprocess.Popen('del /S /Q /F %s\\*.*' % del_dir, shell=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        rTup = pObj.communicate()
        rCod = pObj.returncode
        # os.system("rd /s /q %systemdrive%\$Recycle.bin")
        # del_command = ['del', '/S', '/Q', '/F', f'{tempfile.gettempdir()}\\*.*']
        # subprocess.Popen(del_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        os.system("rd /s /q %systemdrive%\$Recycle.bin")
        x = bot.send_message(message.chat.id,
                             f'Очистка прошла успешно! Хотите ли вы, чтобы я очистил папку загрузок?',
                             reply_markup=markup)
        bot.register_next_step_handler(x, clean_downloads,bot)
    except:
        bot.send_message(message.chat.id,
                         ERRORS['unclear'])


def clean_downloads(message: Message, bot: TeleBot):
    markup = return_to_main_menu()
    v = message.text
    if v == "Да":
        bot.send_message(message.chat.id, 'Начинаю очистку. . .')
        default_path_d_win = r"C:/Users/" + os.getlogin() + r"/Downloads/"
        files_to_remove = os.listdir(default_path_d_win)
        for remove_files in files_to_remove:
            try:
                os.remove(default_path_d_win + "/" + remove_files)
            except:
                p = 0
        bot.send_message(message.chat.id, 'Успешно!', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Жаль(', reply_markup=markup)


clean_pc_handlers = {'Почисти пк от не нужных файлов':clean_out_of_junk_files}