import os
import platform
import time
from datetime import datetime
import tkinter as tk
import keyboard
import pyautogui as pag
import pytz
import requests
import telebot
import wmi
from telebot import TeleBot, types
from telebot.types import Message
import ctypes
from pydub import AudioSegment
import winsound
import psutil
import GPUtil

from jarvis_telegram.markups.work_with_pc_markups import get_work_with_pc_markups, get_turn_off_markup, \
    get_tun_off_timer_markup, get_warning_markup, get_monitoring_markup
from languges import JARVIS, info_message

tok = "030449853c61a3cb7d9c32c14561db39"
token = '6929408227:AAFg7V3Qgu_86FQPmD3p5ifzvxvUInyJO84'
bot_1 = TeleBot(token=token)


# @bot.message_handler(regexp='работа с пк')
def work_with_pc(message: Message, bot: TeleBot):
    markup = get_work_with_pc_markups()
    # markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    # markup.add("Свернуть все окна", "Развернуть все окна")
    # markup.add("Закрытие окна", "Поменять фон рабочего стола")
    # markup.add('Информация', 'Вывести сообщение на экран', 'Произнести аудио')
    # markup.add('Комплектующие', 'Состояние', 'Мониторинг')
    # markup.add("Выключить пк...", 'Перезагрузить пк', 'Спящий режим')
    # markup.add("Вернуться в главное меню")
    bot.send_message(message.chat.id, 'Что хотите сделать?', reply_markup=markup)


def desktop_wallpaper(message: Message, bot: TeleBot):
    message_for_user = bot.send_message(message.chat.id, "Отправьте картинку.")
    bot.register_next_step_handler(message_for_user, set_desktop_wallpaper, bot=bot)


def set_desktop_wallpaper(message: Message, bot: TeleBot):
    try:
        fileID = message.photo[-1].file_id
        dirname, filename = os.path.split(os.path.abspath(__file__))

        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)

        with open(dirname + '\\' + "image.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
        ctypes.windll.user32.SystemParametersInfoW(20, 0,
                                                   dirname + '\\' + 'image.jpg', 0)
        bot.send_message(message.chat.id, text='Успешно')
    except TypeError as e:
        bot.send_message(message.chat.id, 'Это не похоже на картинку')

def close_all_windows(message: Message, bot: TeleBot):
    keyboard.send('Windows+d')
    bot.send_message(message.chat.id, text='Выполнено!')


def show_all_process():
    right_proc = set()
    for process in psutil.process_iter(['name']):
        if (process.io_counters().read_count > 10 and process.io_counters().write_count > 10
            and process.connections() != []) and process.threads() != []:
            right_proc.add(process.name())
    return right_proc


# @bot.message_handler(regexp='Закрытие окна')
def send_all_process(message: Message, bot: TeleBot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in show_all_process():
        button = types.KeyboardButton(i)
        markup.add(button)
    f = bot.send_message(message.chat.id, reply_markup=markup, text=f'Вот все процессы которые вы можете закрыть\n'
                                                                    f'Если вы не знаете за что отвечает процесс,'
                                                                    f'лучше его не трогать ;)')
    bot.register_next_step_handler(f, close_window, bot=bot)


def close_window(message: Message, bot: TeleBot):
    complete = False
    for process in psutil.process_iter(['name']):
        if process.name() == message.text:
            process.kill()
            complete = True
    if complete:
        bot.send_message(message.chat.id, text='Выполнено!')
    else:
        bot.send_message(message.chat.id, text='Похоже кто то это сделал до меня :(')


def get_local_ip():
    hostname = requests.get(url="https://jsonip.com").json()
    return hostname


def get_info_ip(ip="127.0.0.1"):
    try:
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
        return response
    except requests.exceptions.ConnectionError:
        print("(((")


def get_weather(city, tk):
    responce = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={tk}&units=metric&lang=ru").json()
    weather_info = (responce['main']['temp'], responce['weather'][0]['description'])
    return weather_info


my_ip = get_local_ip()['ip']
time_1 = get_info_ip(my_ip)

local_cite = time_1['city']
tz = pytz.timezone(time_1['timezone'])
time_now = datetime.now(tz).strftime('%H:%M')
my_city = time_1['city']


# @bot.message_handler(regexp="Информация")
def info1(message: Message, bot: TeleBot):
    time1 = time_now
    location = local_cite
    all_about_weather = get_weather(my_city, tok)
    info = all_about_weather[1]
    weather1 = all_about_weather[0]

    bot.send_message(
        message.from_user.id,
        f"Привет! Я Джарвис - Голосовой, виртуальный, многофункциональный, "
        f"роботоподобный скрипт!\nМой создатель - @egor_vubni\n\n А теперь о тебе:\nГород: {location} \n"
        f"Время: {time1} \nПогода: {info} \nТемпература за окном: {weather1}")


# @bot.message_handler(regexp='Произнести аудио')
def say_voice(message: Message, bot: TeleBot):
    message_for_user = bot.send_message(message.from_user.id, "Отправьте аудио которое должно произнестись на пк!")

    def sound_on_pc(message: Message, bot: TeleBot):
        file_info = bot.get_file(message.voice.file_id)
        path = file_info.file_path  # Вот тут-то и полный путь до файла (например: voice/file_2.oga)
        fname1 = os.path.basename(path)  # Преобразуем путь в имя файла (например: file_2.oga)
        fname1 = fname1.split('.')[0]
        doc = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token,
                                                                             file_info.file_path))  # Получаем и  сохраняем присланную голосвуху (Ага, админ может в любой момент отключить удаление айдио файлов и слушать все, что ты там говоришь. А представь, что такую бяку подселят в огромный чат и она будет просто логировать все сообщения [анонимность в телеграмме, ахахаха])
        with open(fname1 + '.oga', 'wb') as f:
            f.write(doc.content)
        sound = AudioSegment.from_ogg(fname1 + ".oga")
        sound.export(fname1 + ".wav", format="wav")
        winsound.PlaySound(fname1 + '.wav', winsound.SND_FILENAME)
        bot.send_message(message.from_user.id, "Произнесено")
        os.remove(fname1 + ".oga")
        os.remove(fname1 + ".wav")

    bot.register_next_step_handler(message_for_user, sound_on_pc, bot)


def get_system_info():
    computer = wmi.WMI()
    computer_info = computer.Win32_ComputerSystem()[0]
    os_info = computer.Win32_OperatingSystem()[0]
    proc_info = computer.Win32_Processor()[0]
    system_info = (computer_info, os_info, proc_info)
    return system_info


def get_amount_ram():
    info_ram = (str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB")
    return info_ram


system = platform.system()
version = platform.version()
proc_info = get_system_info()[2].Name.rstrip()
name_videocard = GPUtil.getGPUs()[0].name
amount_ram = get_amount_ram()


def characteristics(message: Message, bot: TeleBot):
    oper_system = f'Операционная система: {system}'
    system_ver = f'Версия Операционной системы: {version}'
    processor = f'Процессор: {proc_info}'
    ram = f'Оперативная память: {amount_ram}'
    videocard = f'Видеокарта: `{name_videocard}'
    bot.send_message(message.chat.id, f"{oper_system}\n\n{system_ver}\n\n{processor}\n\n{ram}\n\n{videocard}")


def system_condition(message: Message, bot: TeleBot):
    bot.send_message(message.from_user.id, text='секунду, измеряю загруженность процессора')
    virtual_memory = str(psutil.virtual_memory().percent)
    cpu_percent = str(psutil.cpu_percent(3))
    try:
        gpu = int(GPUtil.getGPUs()[0].temperature)
    except:
        gpu = 'Видеокарта отсутсвует или видеокарта от компании AMD, температуру получить невозможно'
    bot.send_message(message.from_user.id,
                     f"  Процессор: \n💥Нагрузка - {cpu_percent}%\n---------------------------------\n"
                     f"  Оперативная память (ОЗУ):\n💥Нагрузка - {virtual_memory}%\n"
                     f"---------------------------------\n  Видеокарта: \n🌡️Температура - {str(gpu)}°")


# @bot.message_handler(regexp='Мониторинг')
def monitoring(message: Message, bot: TeleBot):
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # markup.row('5', '10', '20', '40', '60', '120')
    markup = get_monitoring_markup()
    message_for_user = bot.send_message(message.from_user.id, 'Выберите или напишите время мониторинга в секундах',
                                        reply_markup=markup)
    bot.register_next_step_handler(message_for_user, monitoring_system, bot)


def monitoring_system(message: Message, bot: TeleBot):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Вернуться в главное меню')
    result = message.text
    # WindowMessage(2)
    virtual_memory = str(psutil.virtual_memory().percent)
    cpu_percent = str(psutil.cpu_percent())
    try:
        gpu = int(GPUtil.getGPUs()[0].temperature)
    except:
        gpu = 'Видеокарта отсутсвует или видеокарта от компании AMD, температуру получить невозможно'
    msg = bot.send_message(message.from_user.id,
                           f"Статистика будет показываться еще {str(int(result))} секунд \n  Процессор: \n💥"
                           f"Нагрузка - {cpu_percent}%\n---------------------------------\n"
                           f"  Оперативная память (ОЗУ):\n💥"
                           f"Нагрузка - {virtual_memory}%\n---------------------------------\n "
                           f" Видеокарта: \n🌡️Температура - {str(gpu)}°")
    bot.send_message(message.from_user.id, 'Вы можете продолжать отправлять обычные команды', reply_markup=markup)
    for i in range(int(int(result) + 1)):
        try:
            gpu = int(GPUtil.getGPUs()[0].temperature)
        except:
            gpu = 'Видеокарта отсутсвует или видеокарта от компании AMD, температуру получить невозможно'
        virtual_memory = str(psutil.virtual_memory().percent)
        cpu_percent = str(psutil.cpu_percent())
        if i == int(result):
            bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                  text=f"Обновление данных завершено. Последний результат:\n  Процессор: \n💥Нагрузка"
                                       f" - {cpu_percent}%\n---------------------------------\n  Оперативная память"
                                       f" (ОЗУ):\n💥Нагрузка - {virtual_memory}%\n---------------------------------\n"
                                       f"  Видеокарта: \n 🌡️Температура - {str(gpu)}°")
            bot.reply_to(msg, 'Мониторинг закончен. Последний результат отображается в этом сообщении')
        else:
            bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                  text=f"Статистика будет показываться еще {str(int(int(result) - int(i)))} секунд\n"
                                       f"  Процессор: \n💥Нагрузка - {cpu_percent}%\n---------------------------------"
                                       f"\n  Оперативная память (ОЗУ):\n💥Нагрузка - {virtual_memory}%\n--------------"
                                       f"-------------------\n  Видеокарта: \n🌡️Температура - {str(gpu)}°")
        time.sleep(1)


# @bot.message_handler(regexp='Перезагрузить пк')
def reboot_system(message: Message, bot: TeleBot):
    os.system('reboot now')


# @bot.message_handler(regexp='Спящий режим')
def sleep_mode(message: Message, bot: TeleBot):
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


# @bot.message_handler(regexp='Выключить пк...')
def turn_off_pc(message: Message, bot: TeleBot):
    markup = get_turn_off_markup()
    # markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    # markup.add("Выключить пк", "Поставить таймер на выключение", "Остановить таймер")
    # markup.add("Вернуться в главное меню")
    bot.send_message(message.chat.id, 'Что хотите сделать?', reply_markup=markup)


# @bot.message_handler(regexp='Остановить таймер')
def stop_timer(message: Message, bot: TeleBot):
    os.system("shutdown -a")


# @bot.message_handler(regexp='Поставить таймер на выключение')
def turn_off_timer(message: Message, bot: TeleBot):
    markup = get_tun_off_timer_markup()
    # markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    # markup.row("1", "2", "5", '10', '15', '20')
    # markup.row("30", "40", "50", '60', '90', '120')
    # markup.add("Вернуться в главное меню")
    message_for_user = bot.send_message(message.chat.id, 'Выберите или введите - через сколько минут отключить пк',
                                        reply_markup=markup)
    bot.register_next_step_handler(message_for_user, turn_off_timer_on)


def turn_off_timer_on(message: Message):
    os.system("shutdown -s -t " + str(int(message.text) * 60))


# @bot.message_handler(regexp='Выключить пк')
def turn_off(message: Message, bot: TeleBot):
    bot.send_message(message.chat.id, 'Выключаю...')
    os.system("shutdown -s -t 0")


def very_warning_message(text, title):
    root = tk.Tk()
    root.title("Джарвис. " + title)

    text_label = tk.Label(root, text=text, padx=10, pady=10)
    text_label.pack()

    root.mainloop()


# @bot.message_handler(regexp='Вывести сообщение на экран')
def display_notice(message: Message, bot: TeleBot):
    markup = get_warning_markup()
    # markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    # markup.add('Вывести важное сообщение')
    # markup.add('Вывести предупреждение')
    # markup.add('Вывести информационное сообщение')
    # markup.add("Вернуться в главное меню")
    bot.send_message(message.chat.id, 'Выберите вид сообщения и введите текст', reply_markup=markup)


# @bot.message_handler(regexp='Вывести информационное сообщение')
def display_info_notice(message: Message, bot: TeleBot):
    message_for_user = bot.send_message(message.chat.id, 'Напишите текст информационного сообщения')
    bot.register_next_step_handler(message_for_user, message_information)


def message_information(message: Message):
    very_warning_message(message.text, "Информация!")


# @bot.message_handler(regexp='Вывести предупреждение')
def display_warning(message: Message, bot: TeleBot):
    message_for_user = bot.send_message(message.chat.id, 'Напишите текст предупреждения сообщения')
    bot.register_next_step_handler(message_for_user, message_warning)


def message_warning(message: Message):
    very_warning_message(message.text, "Важное сообщение!")


# @bot.message_handler(regexp='Вывести важное сообщение')
def display_important_notice(message: Message, bot: TeleBot):
    message_for_user = bot.send_message(message.chat.id, 'Напишите текст важного сообщения')
    bot.register_next_step_handler(message_for_user, message_important)


def message_important(message: Message):
    very_warning_message(message.text, "Внимание!")


work_with_pc_handlers = {
    r'(?i)работа с пк': work_with_pc, r'(?i)Поменять фон рабочего стола': desktop_wallpaper,
    r'(?i)Закрытие окна': send_all_process, r'(?i)Развернуть все окна': close_all_windows,
    r'(?i)Свернуть все окна': close_all_windows, r'(?i)Состояние': system_condition,
    r'(?i)Произнести аудио': say_voice, r'(?i)Комплектующие': characteristics, r'(?i)Информация': info1,
    r'(?i)Мониторинг': monitoring, r'(?i)Перезагрузить пк': reboot_system, r'(?i)Спящий режим': sleep_mode,
    r'(?i)Выключить пк...': turn_off_pc, r'(?i)Поставить таймер на выключение': turn_off_timer,
    r'(?i)Остановить таймер': stop_timer, r'(?i)Выключить пк': turn_off,
    r'(?i)Вывести сообщение на экран': display_notice,
    r'(?i)Вывести информационное сообщение': display_important_notice,
    r'(?i)Вывести предупреждение': display_warning, r'(?i)Вывести важное сообщение': display_important_notice
}
