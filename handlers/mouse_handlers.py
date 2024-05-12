from typing import Callable

import win32api
from telebot.types import Message
from telebot import TeleBot, types
import time
import pyautogui as pag

from jarvis_telegram.markups.mouse_markups import select_mouse_option, select_distance, select_mouse_function

scrolls_dict = {'down': -50, 'up': 50}


def mouse_move_to_somewhere(message: Message, bot: TeleBot, x: int = 0, y: int = 0) -> None:
    if message.text == "Назад":
        bot.send_message(message.chat.id, 'Куда направимся', reply_markup=select_mouse_option())
    else:
        message_about_start = bot.send_message(message.chat.id, 'Запущено!')
        amount_movements = int(message.text)
        for i in range(amount_movements):
            pag.moveRel(xOffset=x, yOffset=y, duration=0.01)
        bot.register_next_step_handler(
            message_about_start, mouse_move_to_right, bot
        )


def scroll_in_direction(message: Message, bot: TeleBot, direction: int) -> None:
    if message.text == "Назад":
        bot.send_message(
            message.chat.id, 'Куда направимся', reply_markup=select_mouse_option()
        )
    else:
        message_for_user = bot.send_message(message.chat.id, 'Запущено!')
        amount_scroll = int(message.text)
        correct_amount_scroll = amount_scroll * 15
        for i in range(correct_amount_scroll):
            pag.scroll(direction)
        bot.register_next_step_handler(message_for_user, scroll_in_direction, bot=bot)


def chose_time_for_moving(message: Message, bot: TeleBot, next_function: Callable) -> None:
    message_for_user = bot.send_message(
        message.chat.id, 'На сколько? (Можно ввести своё число)', reply_markup=select_distance()
    )
    bot.register_next_step_handler(message_for_user, next_function, bot=bot)


def work_with_mouse(message: Message, bot: TeleBot) -> None:
    # if not jarvis_func[3]:
    #     bot.send_message(message.chat.id, 'Данный раздел не входит в функции подписки!')
    #     return
    bot.send_message(message.chat.id, 'Куда направимся', reply_markup=select_mouse_function())


def enter_lkm_five_sec(message: Message, bot: TeleBot) -> None:
    win32api.mouse_event(2, 0, 0)
    time.sleep(5)
    win32api.mouse_event(4, 0, 0)


def enter_pkm_five_sec(message: Message, bot: TeleBot) -> None:
    win32api.mouse_event(8, 0, 0)
    time.sleep(5)
    win32api.mouse_event(10, 0, 0)


def scroll_down_scroll(message: Message, bot: TeleBot) -> None:
    scroll_in_direction(message, bot, scrolls_dict['down'])


def scroll_up_scroll(message: Message, bot: TeleBot) -> None:
    scroll_in_direction(message, bot, scrolls_dict['up'])


def enter_lkm(message: Message, bot: TeleBot) -> None:
    pag.leftClick()


def enter_pkm(message: Message, bot: TeleBot) -> None:
    pag.rightClick()


def choose_time_for_scroll_down(message: Message, bot: TeleBot) -> None:
    chose_time_for_moving(message, bot, scroll_down_scroll)


def choose_time_for_scroll_up(message: Message, bot: TeleBot) -> None:
    chose_time_for_moving(message, bot, scroll_up_scroll)


def choose_time_for_right(message: Message, bot: TeleBot) -> None:
    chose_time_for_moving(message, bot, mouse_move_to_right)


def choose_time_for_left(message: Message, bot: TeleBot) -> None:
    chose_time_for_moving(message, bot, mouse_move_to_left)


def choose_time_for_up(message: Message, bot: TeleBot) -> None:
    chose_time_for_moving(message, bot, mouse_move_to_up)


def choose_time_for_down(message: Message, bot: TeleBot) -> None:
    chose_time_for_moving(message, bot, mouse_move_to_down)


def mouse_move_to_right(message: Message, bot: TeleBot) -> None:
    mouse_move_to_somewhere(message, bot, x=25)


def mouse_move_to_left(message: Message, bot: TeleBot) -> None:
    mouse_move_to_somewhere(message, bot, x=-25)


def mouse_move_to_up(message: Message, bot: TeleBot) -> None:
    mouse_move_to_somewhere(message, bot, y=-25)


def mouse_move_to_down(message: Message, bot: TeleBot) -> None:
    mouse_move_to_somewhere(message, bot, y=25)


handlers_mouse = {
    r'(?i)Зажатие ЛКМ на 5 секунд': enter_lkm_five_sec,
    r'(?i)Зажатие ПКМ на 5 секунд': enter_pkm_five_sec,
    r'(?i)Прокрутка вниз': choose_time_for_scroll_down,
    r'(?i)Прокрутка вверх': choose_time_for_scroll_up,
    r'(?i)Нажатие ЛКМ': enter_lkm, r'(?i)Нажатие ПКМ': enter_pkm,
    r'(?i)Вправо': choose_time_for_right,
    r'(?i)Влево': choose_time_for_left,
    r'(?i)Вниз': choose_time_for_down, r'(?i)Вверх': choose_time_for_up
}
