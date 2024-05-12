import os
from datetime import timezone, timedelta, datetime
from time import sleep

import pymysql

from languges import ERRORS


def compare_dates(target_date, days_to_add):
    # Получаем текущую дату по Московскому времени
    moscow_timezone = timezone(timedelta(hours=3))  # MSK is UTC+3
    moscow_time = datetime.now(moscow_timezone).date()

    # Добавляем заданное количество дней к целевой дате
    target_date += timedelta(days=int(days_to_add))

    # Сравниваем текущую дату с целевой с учетом добавленных дней и возвращаем результат
    return moscow_time < target_date


def check_user(cursor):
    code = open("VubniCodeAuth.txt", 'r').readline()
    if code:
        user_check_sql = "SELECT * FROM users_jarvis WHERE code = %s"
        cursor.execute(user_check_sql, (code,))
        try:
            x = cursor.fetchone()
            if not x:
                print("Аккаунт не найден!")
                sleep(3)
                os._exit(0)
            login = x[2]
            user_check_sql = "SELECT jarvis_date_buy, jarvis_day_use FROM users_info WHERE login = %s"
            cursor.execute(user_check_sql, (login,))
            c = cursor.fetchone()
            if c:
                if int(c[1]) != 0:
                    if not compare_dates(c[0], c[1]):
                        print("Срок действия версии закончился!")
                        sleep(3)
                        os._exit(0)
            x = list(x)[3:]
            x = [bool(x1) for x1 in x]
            return x
        except Exception as e:
            print(e)
            sleep(3)
            os._exit(0)
    else:
        print("Ошибка, не найден файл авторизации!")
        sleep(3)
        os._exit(0)


def check_version():
    try:
        connection = pymysql.connect(
            host='45.146.165.148',
            user='api-root',
            password='OZWQjiZy-R8piGhVU-A6L0tgMn-JARVIS',
            database='accounts'
        )
    except pymysql.MySQLError as e:
        error_text = ERRORS['internet']
        print(error_text)
        sleep(3)
        os._exit(0)

    with connection.cursor() as cursor:
        x = check_user(cursor)
    connection.close()
    return x