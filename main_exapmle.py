from loguru import logger

from jarvis_telegram.handlers.internet_handlers import *
from jarvis_telegram.handlers.screen_handlers import *
from jarvis_telegram.handlers.mouse_handlers import *
from jarvis_telegram.handlers.video_handlers import *
from jarvis_telegram.handlers.work_with_comp_handler import *
from jarvis_telegram.handlers.text_handler import *

bot = telebot.TeleBot(token='6929408227:AAFg7V3Qgu_86FQPmD3p5ifzvxvUInyJO84')
tk = "030449853c61a3cb7d9c32c14561db39"


def register_handlers(bot: telebot.TeleBot, handlers_dicts: dict):
    logger.info(f"start register handlers {list(handlers_dicts.keys())}")
    for regx, func in handlers_dicts.items():
        bot.register_message_handler(func, pass_bot=True, regexp=regx)
        logger.success(f"register handler:{func}")


register_handlers(bot, handlers_browser)
register_handlers(bot, display_handlers)
register_handlers(bot, handlers_video)
register_handlers(bot, handlers_mouse)
register_handlers(bot, work_with_pc_handlers)
register_handlers(bot, text_handlers)
bot.infinity_polling()
