import keyboard
import py_win_keyboard_layout
from PIL import ImageGrab
from telebot.types import Message
from telebot import TeleBot, types
import tempfile

from jarvis_telegram.markups.video_markups import get_work_with_video_markup, get_work_with_volume_markup


# @bot.message_handler(regexp='Работа с видео и фильмами')
def video_handlers_markup(message: Message, bot: TeleBot):
    markup = get_work_with_video_markup()
    bot.send_message(message.chat.id, 'Выберите действие', reply_markup=markup)


# @bot.message_handler(regexp='Перемотать назад')
def rewind_back(message: Message, bot: TeleBot):
    keyboard.send("left")
    bot.send_message(message.chat.id, 'Перемотано!')


# @bot.message_handler(regexp='Перемотать вперёд')
def rewind_forward(message: Message, bot: TeleBot):
    keyboard.send("right")
    bot.send_message(message.chat.id, 'Перемотано!')


# @bot.message_handler(regexp='Громкость')
def volume(message: Message, bot: TeleBot):
    markup = get_work_with_volume_markup()
    bot.send_message(message.chat.id, 'Слишком громко? Слишком тихо? Сейчас все решим', reply_markup=markup)


# @bot.message_handler(regexp='Сделать погромче')
def volume_up(message: Message, bot: TeleBot):
    keyboard.send("volume up")
    bot.send_message(message.chat.id, 'Сделано!')


# @bot.message_handler(regexp='Сделать потише')
def volume_down(message: Message, bot: TeleBot):
    keyboard.send("volume down")
    bot.send_message(message.chat.id, 'Сделано!')


# @bot.message_handler(regexp='Отключить/Включить звук')
def volume_off_on(message: Message, bot: TeleBot):
    keyboard.send("volume mute")
    bot.send_message(message.chat.id, 'Сделано!')


# @bot.message_handler(regexp='Полноразмерное видео/Не полноразмерное видео')
def full_screen_on_full(message: Message, bot: TeleBot):
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
    keyboard.send("f")
    bot.send_message(message.chat.id, 'Сделано!')


# @bot.message_handler(regexp='Остановка/Запуск видео')
def play_video_stop(message: Message, bot: TeleBot):
    keyboard.send("space")
    bot.send_message(message.chat.id, 'Сделано!')
    path = tempfile.gettempdir() + 'screenshot.png'
    screenshot = ImageGrab.grab()
    screenshot.save(path, 'PNG')
    bot.send_photo(message.chat.id, open(path, 'rb'))


handlers_video = {
    r'(?i)Работа с видео и фильмами': video_handlers_markup,
    r'(?i)Перемотать назад': rewind_back, r'(?i)Перемотать вперед': rewind_forward,
    r'(?i)Громкость': volume, r'(?i)Сделать погромче': volume_up,
    r'(?i)Сделать потише': volume_down, r'(?i)Отключить/Включить звук': volume_off_on,
    r'(?i)Полноразмерное видео/Не полноразмерное видео': full_screen_on_full,
    r'(?i)Остановка/Запуск видео': play_video_stop,

}
