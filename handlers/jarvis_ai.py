import requests
from telebot.types import Message
from telebot import TeleBot

from languges import JARVIS, ERRORS


# @bot.message_handler(regexp='Jarvis Ai')
def get_question_for_ai(message: Message, bot: TeleBot):
    # if not jarvis_func[12]:
    #     bot.send_message(message.chat.id, 'Данный раздел не входит в функции подписки!')
    #     return
    message_for_user = bot.send_message(message.chat.id,
                                        JARVIS['question_jarvis_ai'])
    bot.register_next_step_handler(message_for_user, tolk_to_jarvis_ai, bot)


messageGPT = []


def tolk_to_jarvis_ai(message: Message, bot: TeleBot):
    global messageGPTWork
    global messageGPT
    if message.text == 'Стоп' or message.text == 'стоп':
        messageGPTWork = 0
        bot.send_message(message.chat.id, f'Jarvis Ai остановлен')
    elif message.text == 'Очисти память' or message.text == 'очисти память':
        messageGPT = []
        bot.send_message(message.chat.id, f'Готово! Ваш диалог очищен!')
    else:
        print(messageGPT)
        messageGPT.append(message.text)
        msg = bot.send_message(message.chat.id, f'*Jarvis Ai думает над ответом')
        try:
            url = 'https://api.vubni.com/question/'
            headers = {
                'Authorization': '657a99df3f951dea1ba03c5f7627f9f3',
                'Content-Type': 'application/json'
            }
            data = {
                'dialog': messageGPT
            }

            response = requests.post(url, headers=headers, json=data)
            x = response.json()["answer"]
            messageGPT.append(x)
            bot.delete_message(message.chat.id, msg.id)
            bot.send_message(message.chat.id, f'Готово! Ответ:')
            bot.send_message(message.chat.id, x)
            messageGPTWork = 1
        except Exception as e:
            bot.send_message(message.chat.id,
                             ERRORS['errors_gpt'] + str(e))


jarvis_ai_handlers = {r'(?i)Jarvis Ai': tolk_to_jarvis_ai}
