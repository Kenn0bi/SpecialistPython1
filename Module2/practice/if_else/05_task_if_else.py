# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

# Вариант 1

month_number = int(input("Введите номер месяца от 1 до 12: "))

if month_number == 1:
    print("январь")
elif month_number == 2:
    print("февраль")
elif month_number == 3:
    print("март")
elif month_number == 4:
    print("апрель")
elif month_number == 5:
    print("май")
elif month_number == 6:
    print("июнь")
elif month_number == 7:
    print("июль")
elif month_number == 8:
    print("август")
elif month_number == 9:
    print("сентябрь")
elif month_number == 10:
    print("октябрь")
elif month_number == 11:
    print("ноябрь")
else:
    print("декабрь")

# Вариант 2

month = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
month_number = int(input("Введите номер месяца от 1 до 12: "))

print(month[month_number-1])
