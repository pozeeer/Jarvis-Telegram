from typing import Callable
from jarvis_telegram.handlers.internet_handlers import *
from jarvis_telegram.handlers.screen_handlers import display_handlers
from jarvis_telegram.handlers.mouse_handlers import *
from jarvis_telegram.handlers.video_handlers import *
from jarvis_telegram.handlers.work_with_comp_handler import *
from jarvis_telegram.handlers.change_screen_resolution import *
from jarvis_telegram.handlers.clean_pc_hendlers import *
from jarvis_telegram.handlers.jarvis_ai import *
from jarvis_telegram.handlers.text_handler import *
from jarvis_telegram.handlers.work_with_bot_handlers import *
from jarvis_telegram.handlers.work_with_console_handlers import *
from jarvis_telegram.handlers.work_with_programs_handlers import *
from jarvis_telegram.markups.menu_markup import get_menu_markup

from decouple import config

bot = telebot.TeleBot(token=config('BOT_TOKEN'))
tk = "030449853c61a3cb7d9c32c14561db39"


@bot.message_handler(commands=['start'])
def get_main_menu(message:Message):
    markup = get_menu_markup()
    bot.send_message(message.chat.id,"Добро пожаловать в Jarvis telegram, чем могу быть полезен?",
                     reply_markup=markup)


def register_handlers(bot: telebot.TeleBot, handlers_dicts: dict, func: Callable | None = None):
    logger.info(f"start register handlers {list(handlers_dicts.keys())[0]}")
    for regx, handler in handlers_dicts.items():
        bot.register_message_handler(handler, pass_bot=True, regexp=regx, func=func)
        logger.success(f"register handler:{handler}")


register_handlers(bot, handlers_browser)
register_handlers(bot, display_handlers)
register_handlers(bot, handlers_video)
register_handlers(bot, handlers_mouse)
register_handlers(bot, work_with_pc_handlers)
register_handlers(bot, change_screen_handlers)
register_handlers(bot, clean_pc_handlers)
register_handlers(bot, jarvis_ai_handlers)
register_handlers(bot,text_handlers)
register_handlers(bot, work_with_bot_handlers)
register_handlers(bot, work_with_console_handlers)

# register_handlers(bot, text_handlers)

bot.infinity_polling()
