import os
import sys

from telebot import TeleBot
from telebot.types import Message


# @bot.message_handler(regexp='Перезапустить бота')
def reboot_bot(message: Message, bot: TeleBot):
    bot.send_message(message.from_user.id, "Бот перезагружается. . .")
    os.startfile(__file__)
    sys.exit()


# @bot.message_handler(regexp='Остановить бота')
def off_bot(message: Message, bot: TeleBot):
    bot.send_message(message.from_user.id, "Бот завершает рабо...")
    os._exit(0)


work_with_bot_handlers = {r'(?i)Остановить бота': reboot_bot, r'(?i)Остановить бота': off_bot}
