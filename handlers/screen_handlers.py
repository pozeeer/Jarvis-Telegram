import cv2
import screen_brightness_control as sbc
import tempfile
import re
from PIL import ImageGrab
from telebot.types import Message
from telebot import TeleBot


from languges import ERRORS

from jarvis_telegram.markups.screen_handlers import *

# bot = OwnBot(token='6929408227:AAFg7V3Qgu_86FQPmD3p5ifzvxvUInyJO84')


# @bot.message_handler(regexp=r'(?i)Получить скриншот экрана')
def screenshot(message: Message, bot: TeleBot):
    path = tempfile.gettempdir() + 'screenshot.png'
    screenshot = ImageGrab.grab(all_screens=True)
    screenshot.save(path, 'PNG')
    bot.send_photo(message.chat.id, open(path, 'rb'))


# @bot.message_handler(regexp=r'(?i)Получить скриншот веб-камеры')
def screenshot_web_camera(message: Message, bot: TeleBot):
    # WindowMessage(0)
    video_capture = cv2.VideoCapture(0)
    ret, frame = video_capture.read()
    cv2.imwrite('screenshot.png', frame)
    bot.send_photo(message.from_user.id, photo=open('screenshot.png', 'rb'))


# @bot.message_handler(regexp=r'(?i)Яркость на максимум')
def bright_max(message: Message, bot: TeleBot):
    sbc.set_brightness(100)
    bot.send_message(message.chat.id, 'Успешно!')


# @bot.message_handler(regexp=r'(?i)Яркость на минимум')
def bright_min(message: Message, bot: TeleBot):
    sbc.set_brightness(0)
    bot.send_message(message.chat.id, 'Успешно!')


# @bot.message_handler(regexp=r'(?i)Яркость плюс')
def bright_plus(message: Message, bot: TeleBot):
    nums = re.findall(r'\d+', message.text)
    v = [int(i) for i in nums][0]
    brightness = int(sbc.get_brightness()[0])
    sbc.set_brightness(brightness + v)
    bot.send_message(message.chat.id, 'Успешно!')


# @bot.message_handler(regexp=r'(?i)Яркость минус')
def bright_minus(message: Message, bot: TeleBot):
    nums = re.findall(r'\d+', message.text)
    v = [int(i) for i in nums][0]
    brightness = int(sbc.get_brightness()[0])
    sbc.set_brightness(brightness - v)
    bot.send_message(message.chat.id, 'Успешно!')


# @bot.message_handler(regexp=r'(?i)Яркость на')
def bright_up(message: Message, bot: TeleBot):
    try:
        nums = re.findall(r'\d+', message.text)
        v = [int(i) for i in nums][0]
        sbc.set_brightness(v)
        bot.send_message(message.chat.id, 'Успешно!')
    except:
        bot.send_message(message.chat.id,
                         ERRORS['error_input'])


# @bot.message_handler(regexp='Работа с экраном')
def work_with_screen(message: Message, bot: TeleBot):
    # if not jarvis_func[1]:
    #     bot.send_message(message.chat.id, 'Данный раздел не входит в функции подписки!')
    #     return
    # markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    # markup.add("Получить скриншот экрана", "Получить скриншот веб-камеры")
    # markup.add('Яркость на максимум', 'Яркость на минимум')
    # markup.add('Вернуться в главное меню')
    markup = get_work_with_screen_markup()
    bot.send_message(message.chat.id, 'Выберите, что хотите сделать!', reply_markup=markup)
    # markup = InlineKeyboardMarkup()
    # markup.add(InlineKeyboardButton(text='Яркость плюс (число)', switch_inline_query_current_chat="Яркость плюс "))
    # markup.add(
    #     InlineKeyboardButton(text='Яркость минус (число)', switch_inline_query_current_chat="Яркость минус "))
    # markup.add(InlineKeyboardButton(text='Яркость на (число)', switch_inline_query_current_chat="Яркость на "))
    inline_markup = get_inline_markup_work_with_bright()
    bot.send_message(message.chat.id, 'Так же вы можете регулировать яркость', reply_markup=inline_markup)


display_handlers = {r'(?i)Работа с экраном': work_with_screen, r'(?i)Получить скриншот экрана': screenshot,
                    r'(?i)Получить скриншот веб-камеры': screenshot_web_camera,
                    r'(?i)Яркость на максимум': bright_max, r'(?i)Яркость на минимум': bright_min,
                    'Яркость плюс': bright_plus, 'Яркость минус': bright_min, 'Яркость на': bright_up}
