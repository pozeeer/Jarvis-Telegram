# @bot.message_handler(regexp='Работа с папками и файлами пк')
import os
import tempfile

import win32api
from telebot import TeleBot
from telebot.types import CallbackQuery, Message, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

tempPath = tempfile.gettempdir()


def echo_message142541515(message: Message, bot: TeleBot):
    # if not jarvis_func[8]:
    #     bot.send_message(message.chat.id, 'Данный раздел не входит в функции подписки!')
    #     return
    msg = ""
    markup = InlineKeyboardMarkup()
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    for i in range(len(drives)):
        markup.add(InlineKeyboardButton(text=drives[i], callback_data=str(i) + 'in'))
    markup.add(InlineKeyboardButton(text="Рабочий стол", callback_data=str(i) + 'inРСтол'))
    markup.add(InlineKeyboardButton(text="Последние каталоги", callback_data=str(i) + 'katl'))
    msg = bot.send_message(message.chat.id, 'Выберите букву диска, в которой мы что-нибудь откроем!',
                           reply_markup=markup)

    # @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call: CallbackQuery, bot: TeleBot):
        markup = InlineKeyboardMarkup()
        req = call.data
        for i in range(len(drives)):
            if str(i) + 'katl' in req:
                try:
                    cv = sum(1 for line in open(tempPath + "\\jarvisHistory.txt"))
                    x = open(tempPath + "\\jarvisHistory.txt", encoding='utf-16')
                    for i2 in range(cv):
                        markup.add(InlineKeyboardButton(text=x.readline().replace('\n', ''),
                                                        callback_data=str(i) + 'inJs' + str(i2)))
                    markup.add(InlineKeyboardButton(text="Назад", callback_data=str(i) + '3off'))
                    bot.edit_message_text(chat_id=message.chat.id, message_id=call.message.id,
                                          text=f'Выберите 1 из 10 ваших последних каталогов', reply_markup=markup)
                except:
                    markup.add(InlineKeyboardButton(text="Назад", callback_data=str(i) + '3off'))
                    bot.edit_message_text(chat_id=message.chat.id, message_id=call.message.id,
                                          text=f'История отсутствует!', reply_markup=markup)

            elif str(i) + 'in' in req:
                try:
                    req = str(req).replace(str(i) + "in", "")
                except:
                    req = ""
                if req == 'РСтол':
                    drives[i] = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop').replace('C:\\',
                                                                                                         'C:\\\\')
                elif 'Js' in req:
                    cv = sum(1 for line in open(tempPath + "\\jarvisHistory.txt"))
                    x = open(tempPath + "\\jarvisHistory.txt", encoding='utf-16')
                    req1 = int(req.replace('Js', ''))
                    for i3 in range(cv):
                        if i3 == req1:
                            drives[i] = x.readline().replace('\n', '')
                            break
                        else:
                            x.readline()
                else:
                    drives[i] = drives[i] + req
                markup.add(InlineKeyboardButton(text="Папки", callback_data=str(i) + '0off' + req))
                markup.add(InlineKeyboardButton(text="Файлы", callback_data=str(i) + '1off' + req))
                markup.add(InlineKeyboardButton(text="Открыть текущий путь", callback_data=str(i) + '2off' + req))
                markup.add(InlineKeyboardButton(text="Отправь мне файл из этой директории",
                                                callback_data=str(i) + '01off' + req))
                if len(drives[i]) != 3:
                    markup.add(InlineKeyboardButton(text="Назад", callback_data=str(i) + 'delete'))
                else:
                    markup.add(InlineKeyboardButton(text="Другой диск", callback_data=str(i) + '3off'))
                bot.edit_message_text(chat_id=message.chat.id, message_id=call.message.id,
                                      text=f'Ваше текущее местоположение: {drives[i]}\nВыберите то, что хотите открыть (папку или файл)',
                                      reply_markup=markup)

            elif str(i) + 'delete' in req:
                req = ""
                x = drives[i].split("\\")
                x1 = x[0]
                for i1 in range(len(x) - 2):
                    x1 += "\\" + x[i1 + 1]
                drives[i] = x1
                markup.add(InlineKeyboardButton(text="Папки", callback_data=str(i) + '0off' + req))
                markup.add(InlineKeyboardButton(text="Файлы", callback_data=str(i) + '1off' + req))
                markup.add(InlineKeyboardButton(text="Открыть текущий путь", callback_data=str(i) + '2off' + req))
                markup.add(InlineKeyboardButton(text="Отправь мне файл из этой директории",
                                                callback_data=str(i) + '01off' + req))
                if len(drives[i]) != 3:
                    markup.add(InlineKeyboardButton(text="Назад", callback_data=str(i) + 'delete'))
                else:
                    markup.add(InlineKeyboardButton(text="Другой диск", callback_data=str(i) + '3off'))
                bot.edit_message_text(chat_id=message.chat.id, message_id=call.message.id,
                                      text=f'Ваше текущее местоположение: {drives[i]}\nВыберите то, что хотите открыть (папку или файл)',
                                      reply_markup=markup)

            elif str(i) + '01off' in req:
                x = 0
                files = os.listdir(drives[i])
                for i1 in range(len(files)):
                    if "." in files[i1]:
                        x1 = str(str(i) + 'rt' + str(i1))
                        markup.add(InlineKeyboardButton(text=files[i1], callback_data=x1))
                        x += 1
                markup.add(InlineKeyboardButton(text="Вернуться", callback_data=str(i) + 'in'))
                if x >= 1:
                    bot.edit_message_text(chat_id=message.chat.id, message_id=call.message.id,
                                          text=f'Выберите файл для отправки', reply_markup=markup)
                else:
                    bot.edit_message_text(chat_id=message.chat.id, message_id=call.message.id,
                                          text=f'К сожлению, фйлов в этом каталоге нет!', reply_markup=markup)


            elif str(i) + '3off' in req:
                bot.delete_message(message.chat.id, call.message.id)
                echo_message142541515(message)

            elif str(i) + '2off' in req:
                os.startfile(drives[i])
                bot.edit_message_text(chat_id=message.chat.id, message_id=call.message.id,
                                      text=f'Папка открывается у вас на пк!')
                TempHistoryAdd(drives[i])

            elif str(i) + '0off' in req:
                x = 0
                folder = os.listdir(drives[i])
                for i1 in range(len(folder)):
                    if "." not in folder[i1]:
                        markup.add(
                            InlineKeyboardButton(text=folder[i1], callback_data=str(i) + 'in\\' + folder[i1]))
                        x += 1
                markup.add(InlineKeyboardButton(text="Вернуться", callback_data=str(i) + 'in'))
                if x >= 1:
                    bot.edit_message_text(chat_id=message.chat.id, message_id=call.message.id,
                                          text=f'Выберите папку для открытия', reply_markup=markup)
                else:
                    bot.edit_message_text(chat_id=message.chat.id, message_id=call.message.id,
                                          text=f'К сожлению, папок в этом каталоге нет!', reply_markup=markup)

            elif str(i) + 'rt' in req:
                try:
                    req = str(req).replace(str(i) + "rt", "")
                except:
                    req = ""
                files = os.listdir(drives[i])
                for i1 in range(len(files)):
                    if i1 == int(req):
                        drives1 = drives[i] + '\\' + files[i1]
                        break
                try:
                    bot.edit_message_text(chat_id=message.chat.id, message_id=call.message.id,
                                          text=f'Файл отправляется. . .')
                    f = open(drives1, "rb")
                    bot.send_document(message.chat.id, f)
                except:
                    bot.edit_message_text(chat_id=message.chat.id, message_id=call.message.id, text=Exception)

            elif str(i) + 'pn' in req:
                try:
                    req = str(req).replace(str(i) + "pn", "")
                except:
                    req = ""
                files = os.listdir(drives[i])
                for i1 in range(len(files)):
                    if i1 == int(req):
                        drives1 = drives[i] + '\\' + files[i1]
                        break
                try:
                    os.startfile(drives1)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=call.message.id,
                                          text=f'Файл открывается у вас на пк!')
                    TempHistoryAdd(drives[i])
                except:
                    bot.edit_message_text(chat_id=message.chat.id, message_id=call.message.id, text=Exception)

            elif str(i) + '1off' in req:
                x = 0
                files = os.listdir(drives[i])
                for i1 in range(len(files)):
                    if "." in files[i1]:
                        x1 = str(str(i) + 'pn' + str(i1))
                        markup.add(InlineKeyboardButton(text=files[i1], callback_data=x1))
                        x += 1
                markup.add(InlineKeyboardButton(text="Вернуться", callback_data=str(i) + 'in'))
                if x >= 1:
                    bot.edit_message_text(chat_id=message.chat.id, message_id=call.message.id,
                                          text=f'Выберите файл для открытия', reply_markup=markup)
                else:
                    bot.edit_message_text(chat_id=message.chat.id, message_id=call.message.id,
                                          text=f'К сожлению, фйлов в этом каталоге нет!', reply_markup=markup)


def TempHistoryAdd(path: str):
    if sum(1 for line in open(tempPath + "\\jarvisHistory.txt")) < 10:
        open(tempPath + "\\jarvisHistory.txt", 'a', encoding='utf-16').write(path + "\n")
    else:
        x = open(tempPath + "\\jarvisHistory.txt", encoding='utf-16')
        x1 = []
        for i in range(10):
            x1.append(x.readline())
        x.close
        x = open(tempPath + "\\jarvisHistory.txt", 'w', encoding='utf-16')
        for i in range(9):
            x.write(x1[i + 1])
        x.write(path + "\n")
        x.close
