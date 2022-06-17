# Пользователь вводит на экран дату в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.

# Подсказка: создайте списки с названием дней и названиями месяцев
# Примечание: для экономии времени, можно ограничить номер дня десятью.
# Примечание: склонениями названий можно принебречь

import datetime

day = "", "первое", "второе", "третье", "четвертое", "пятое", "шестое", "седьмое", "восьмое", "девятое", "десятое"
month = "", "января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"

date = input("Введите дату в формате dd.mm.yyyy (день укажите не более 10): ")

try:
    if datetime.datetime.strptime(date, "%d.%m.%Y"):
        print(day[int(date[:2])], month[int(date[3:5])], date[6:], "года")
except:
    print("Дата введена некорректно!")

