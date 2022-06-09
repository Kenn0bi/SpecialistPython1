# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

# Вариант 1

month_number = int(input("Введите номер месяца от 1 до 12: "))

if month_number == 1:
    print("зима")
elif month_number == 2:
    print("зима")
elif month_number == 3:
    print("весна")
elif month_number == 4:
    print("весна")
elif month_number == 5:
    print("весна")
elif month_number == 6:
    print("лето")
elif month_number == 7:
    print("лето")
elif month_number == 8:
    print("лето")
elif month_number == 9:
    print("осень")
elif month_number == 10:
    print("осень")
elif month_number == 11:
    print("осень")
else:
    print("зима")

# Вариант 2

season = ["зима", "зима", "весна", "весна", "весна", "лето", "лето", "лето", "осень", "осень", "осень", "зима"]
month_number = int(input("Введите номер месяца от 1 до 12: "))

print(season[month_number - 1])
