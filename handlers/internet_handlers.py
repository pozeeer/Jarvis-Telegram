import random
import webbrowser
import keyboard
import py_win_keyboard_layout
import requests

from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from telebot import TeleBot
from loguru import logger
from websearch import WebSearch

from jarvis_telegram.markups.internet_markups import get_markup_with_sites

# def any_user(message: Message, bot: TeleBot):
#     bot.send_message(message.chat.id, text='Получилось!')
# @bot.message_handler(regexp='Работа в интернете')
def work_with_internet_markup(message: Message, bot: TeleBot) -> None:
    # if not jarvis_func[4]:
    #     bot.send_message(message.chat.id, 'Данный раздел не входит в функции подписки!')
    #     return
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Открыть браузер по умолчанию")
    markup.add('Открыть Edge')
    markup.add("Открыть новую вкладку", "Обновить текущую страницу")
    markup.add("Открыть новое окно", "Открыть новое окно в режиме инкогнито")
    markup.add("Закрыть вкладку", "Вернуть закрытую вкладку")
    markup.add('Открыть диспетчер задач', 'Открыть диспетчер закладок')
    markup.add("Добавить страницу в закладки", "Добавить все открытые страницы в закладки")
    markup.add('Открыть скачанные файлы', "Открыть параметры печати текущей страницы")
    markup.add("Открыть историю просмотров", "Показать/скрыть панель закладок")
    markup.add("Открыть инструменты разработчика", "Открыть окно 'Очистить историю'")
    markup.add('Перейти на предыдущую вкладку', 'Перейти на следующую вкладку')
    markup.add('Вернуться к прошлой странице', 'Открыть следующую страницу')
    markup.add('Вернуться в главное меню')
    bot.send_message(message.chat.id, 'Перехожу. . .', reply_markup=markup)
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='Открой сайт }url', switch_inline_query_current_chat="Открой сайт }"))
    markup.add(InlineKeyboardButton(text='Найди информацию >запрос',
                                    switch_inline_query_current_chat="Найди информацию >"))
    markup.add(InlineKeyboardButton(text='Погода <город', switch_inline_query_current_chat="Погода <"))
    bot.send_message(message.chat.id, 'Также вы можете работать с интернетом по inline кнопкам!',
                     reply_markup=markup)


def random_complete() -> str:
    text_completes = ['Выполнено!', 'Готово!', 'Сделано!', 'Операция завершена успешно!',
                      'Миссия выполнена!', 'Задание выполнено!']
    random_text = text_completes[random.randrange(len(text_completes))]
    return random_text


# keyboard_shortcuts = ['alt+right']


def click_keyboard_shortcut(keyboard_shortcut: str, bot: TeleBot, chat_id: int, message: str) -> None:
    keyboard.send(keyboard_shortcut)
    logger.info(f'click {keyboard_shortcut}')
    bot.send_message(chat_id, message)


def next_page(message: Message, bot: TeleBot) -> None:
    click_keyboard_shortcut('alt+right', bot, message.chat.id, random_complete())


def last_page(message: Message, bot: TeleBot) -> None:
    click_keyboard_shortcut('alt+left', bot, message.chat.id, random_complete())


# @bot.message_handler(regexp=r'(?i)Перейти на следующую вкладку')
def go_to_next_tab(message: Message, bot: TeleBot) -> None:
    click_keyboard_shortcut('ctrl+tab', bot, message.chat.id, random_complete())


# @bot.message_handler(regexp=r'(?i)Перейти на предыдущую вкладку')
def go_to_last_tab(message: Message, bot: TeleBot) -> None:
    click_keyboard_shortcut('ctrl+shift+tab', bot, message.chat.id, random_complete())


# @bot.message_handler(regexp=r'(?i)Открыть окно "Очистить историю"')
def clean_history(message: Message, bot: TeleBot) -> None:
    click_keyboard_shortcut('ctrl+shift+delete', bot, message.chat.id, random_complete())


# @bot.message_handler(regexp=r'(?i)Открыть инструменты разработчика')
def open_developers_tools(message: Message, bot: TeleBot) -> None:
    click_keyboard_shortcut('ctrl+shift+j', bot, message.chat.id, random_complete())


# @bot.message_handler(regexp=r'(?i)Показать/скрыть панель закладок')
def show_bookmarks_tab(message: Message, bot: TeleBot) -> None:
    click_keyboard_shortcut('ctrl+shift+b', bot, message.chat.id, random_complete())


# @bot.message_handler(regexp=r'(?i)Открыть историю просмотров')
def open_views_history(message: Message, bot: TeleBot) -> None:
    click_keyboard_shortcut('ctrl+h', bot, message.chat.id, random_complete())


# @bot.message_handler(regexp=r'(?i)Открыть параметры печати текущей страницы')
def open_print_settings(message: Message, bot: TeleBot) -> None:
    click_keyboard_shortcut('ctrl+p', bot, message.chat.id, random_complete())


# @bot.message_handler(regexp=r'(?i)Открыть скачанные файлы')
def open_downloads_files(message: Message, bot: TeleBot) -> None:
    click_keyboard_shortcut('ctrl+j', bot, message.chat.id, random_complete())


# @bot.message_handler(regexp=r'(?i)Открыть новое окно в режиме инкогнито')
def new_incognita_page(message: Message, bot: TeleBot) -> None:
    click_keyboard_shortcut('ctrl+shift+n', bot, message.chat.id, random_complete())


# @bot.message_handler(regexp=r'(?i)Открыть новое окно')
def new_window(message: Message, bot: TeleBot) -> None:
    click_keyboard_shortcut('ctrl+n', bot, message.chat.id, random_complete())


# @bot.message_handler(regexp=r'(?i)Обновить текущую страницу')
def refresh_page(message: Message, bot: TeleBot) -> None:
    click_keyboard_shortcut('ctrl+r', bot, message.chat.id, random_complete())


# @bot.message_handler(regexp=r'(?i)Открыть новую вкладку')
def open_new_tab(message: Message, bot: TeleBot) -> None:
    click_keyboard_shortcut('ctrl+t', bot, message.chat.id, random_complete())


# @bot.message_handler(regexp=r'(?i)Добавить все открытые страницы в закладки')
def add_all_pages_in_bookmarks(message: Message, bot: TeleBot) -> None:
    click_keyboard_shortcut('ctrl+shift+d', bot, message.chat.id, random_complete())
    keyboard.send('enter')


# @bot.message_handler(regexp=r'(?i)Добавить страницу в закладки')
def make_page_bookmark(message: Message, bot: TeleBot) -> None:
    click_keyboard_shortcut('ctrl+d', bot, message.chat.id, random_complete())
    keyboard.send('enter')


# @bot.message_handler(regexp=r'(?i)Открыть диспетчер закладок')
def open_bookmark_manager(message: Message, bot: TeleBot) -> None:
    click_keyboard_shortcut('ctrl+shift+o', bot, message.chat.id, random_complete())


# @bot.message_handler(regexp=r'(?i)Открыть диспетчер задач')
def open_yandex_task_manager(message: Message, bot: TeleBot) -> None:
    click_keyboard_shortcut('shift+esc', bot, message.chat.id, random_complete())


# @bot.message_handler(regexp=r'(?i)Вернуть закрытую вкладку')
def close_tab_return(message: Message, bot: TeleBot) -> None:
    click_keyboard_shortcut('ctrl+shift+t', bot, message.chat.id, random_complete())


# @bot.message_handler(regexp=r'(?i)Закрыть вкладку')
def close_tab(message: Message, bot: TeleBot) -> None:
    click_keyboard_shortcut('ctrl+w', bot, message.chat.id, random_complete())


# @bot.message_handler(regexp=r'(?i)Открыть браузер по умолчанию')
def open_default_browser(message: Message, bot: TeleBot) -> None:
    webbrowser.get(using='windows-default').open_new_tab('https://vubni.com/jarvis/')
    bot.send_message(message.chat.id, 'Выполнено!')


# @bot.message_handler(regexp=r'(?i)Открыть Edge')
def open_edge(message: Message, bot: TeleBot) -> None:
    webbrowser.open_new_tab('https://джарвис-вубни.рф')
    bot.send_message(message.chat.id, 'Выполнено!')


# @bot.message_handler(regexp="Открой сайт:")
def open_web_sait(message: Message, bot: TeleBot) -> None:
    text_for_search = message.text.split(':')[-1]
    web_search = WebSearch(text_for_search)
    web_pages = web_search.pages
    web_sites = web_pages[:5]
    markup = get_markup_with_sites(web_sites)
    x = bot.send_message(message.chat.id, text="Вот список ссылок,\nпо какой именно нужно перейти?",
                         reply_markup=markup)
    bot.register_next_step_handler(x, open_specific_page, bot)


def open_specific_page(message: Message, bot: TeleBot) -> None:
    if 'http' in message.text:
        currency_url = message.text
        webbrowser.get(using='windows-default').open_new_tab(currency_url)
        bot.send_message(message.chat.id, "Выполнено!")
    else:
        x = bot.send_message(message.chat.id, "Это не похоже на ссылку ;)\n попробуй ещё раз!")
        bot.register_next_step_handler(x, open_specific_page, bot)


# @bot.message_handler(regexp="Найди информацию >")
def find_information(message: Message, bot: TeleBot) -> None:
    v = str(message.text).split('>')[1]
    webbrowser.get(using='windows-default').open_new_tab('https://yandex.ru/search/?text=' + v)
    bot.send_message(message.chat.id, 'Выполнено!')


# @bot.message_handler(regexp="Погода <")
def weather(message: Message, bot: TeleBot) -> str | None:
    input_city = str(message.text).split('<')[-1]
    logger.info(f"get city:{input_city}")
    response = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={input_city}"
        f"&appid=4e48950e61aa189901c61ad99f57a27a&units=metric&lang=ru")
    if response.status_code == 404:
        bot.send_message(message.chat.id, 'Город не найден')
        return 'Смерть скрипту'
    try:
        temperature = response.json()['main']['temp']
        pressure = response.json()['main']['pressure']
        wind_speed = response.json()['wind']['speed']
        sky_condition = response.json()['weather'][0]['description']
        latitude = response.json()['coord']['lon']
        longitude = response.json()['coord']['lat']
        user_city = response.json()['name']
        bot.send_message(message.chat.id,
                         f"Город: {user_city} \n Скорость ветра: {wind_speed} \n Температура: {temperature} \n"
                         f" Небо: {sky_condition} \n Широта: {latitude} \n Долгота: {longitude} \n Давление: {pressure}")
    except Exception as e:
        bot.send_message(message.chat.id,
                         f'Ошибка, возможные причины:\n1)Сервер погоды умер\n'
                         f'2)Программист накосячил\n\nДля решения можете обращятьс к:\n'
                         f'@Vubni - тех.поддержка\n @excellent25 - Главный в разработке ботов\n'
                         f'@mqproga - младший программист\n'
                         f'@egor_vubni - главный программист и создатель Джарвис\n\n'
                         f'Статус запроса:{response.status_code}|{response.text}\nКод ошибки:{e}')


handlers_browser = {
    r'(?i)Работа в интернете': work_with_internet_markup,
    r'(?i)Открыть следующую страницу': next_page, r'(?i)Вернуться к прошлой странице': last_page,
    r'(?i)Перейти на следующую вкладку': go_to_next_tab, r'(?i)Перейти на предыдущую вкладку': go_to_last_tab,
    r'(?i)Открыть окно "Очистить историю"': clean_history,
    r'(?i)Открыть инструменты разработчика': open_developers_tools,
    r'(?i)Показать/скрыть панель закладок': show_bookmarks_tab,
    r'(?i)Открыть историю просмотров': open_views_history,
    r'(?i)Открыть параметры печати текущей страницы': open_print_settings,
    r'(?i)Открыть скачанные файлы': open_downloads_files,
    r'(?i)Открыть новое окно в режиме инкогнито': new_incognita_page, r'(?i)Открыть новое окно': new_window,
    r'(?i)Обновить текущую страницу': refresh_page, r'(?i)Открыть новую вкладку': open_new_tab,
    r'(?i)Добавить все открытые страницы в закладки': add_all_pages_in_bookmarks,
    r'(?i)Добавить страницу в закладки': make_page_bookmark,
    r'(?i)Открыть диспетчер закладок': open_bookmark_manager,
    r'(?i)Открыть диспетчер задач': open_yandex_task_manager, r'(?i)Вернуть закрытую вкладку': close_tab_return,
    r'(?i)Закрыть вкладку': close_tab, r'(?i)Открыть браузер по умолчанию': open_default_browser,
    r'(?i)Открыть Edge': open_edge, r'(?i)Погода <': weather, r'(?i)Открой сайт:': open_web_sait,
    r'(?i)Найди информацию >': find_information,
}
