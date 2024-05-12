# @bot.message_handler(regexp='Ввести команду в консоль')
import subprocess

from telebot import TeleBot
from telebot.types import Message


# from telebot_router import TeleBot


def echo_message(message: Message, bot: TeleBot):
    # if not jarvis_func[6]:
    #     bot.send_message(message.chat.id, 'Данный раздел не входит в функции подписки!')
    #     return
    message_for_user = bot.send_message(message.chat.id, 'Введите команду для выполнения в консоли')
    bot.register_next_step_handler(message_for_user, Console)


def Console(message: Message, bot: TeleBot):
    v = message.text
    proc = subprocess.Popen(v, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = proc.communicate()
    bot.send_message(message.chat.id,
                     f'Вывод:\n {out} \n\n(Внимание! Если вы меняли каталог, то вывод будет пустой)')
