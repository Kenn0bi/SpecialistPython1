# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def calculate(s):
    """
    Функция рассчитавает сумму или разность дробей введенных в формате: n x/y.
    :param s: математическое выражение заданное строкой
    :return: результат операции в виде строки
    """
    operation = " + " if s.find(" + ") != -1 else " - "
    num1 = s.split(operation)[0]  # Первое число текстом
    num2 = s.split(operation)[1]  # Второе число текстом

    # Переводим 1-ое число в неправильную дробь
    if num1.find(" ") != -1:  # Если в числе есть и целая часть и дробная
        num1_n = int(num1.split(" ")[0])  # Целая часть
        num1_x = int(num1.split(" ")[1].split("/")[0])  # Числитель
        num1_y = int(num1.split(" ")[1].split("/")[1])  # Знаменатель
        num1_x = abs(num1_n) * num1_y + num1_x  # Пересчет числителя в неправильную дробь
        num1_x = num1_x if num1.find("-") == -1 else -num1_x  # Учет знака дроби
    elif num1.find("/") != -1:  # Если в дроби нет целой части
        num1_x = int(num1.split("/")[0])
        num1_y = int(num1.split("/")[1])
    else:  # Если в дроби только целая часть
        num1_x = int(num1)
        num1_y = 1

    # Переводим 2-ое число в неправильную дробь
    if num2.find(" ") != -1:
        num2_n = int(num2.split(" ")[0])
        num2_x = int(num2.split(" ")[1].split("/")[0])
        num2_y = int(num2.split(" ")[1].split("/")[1])
        num2_x = abs(num2_n) * num2_y + num2_x  # Пересчет числителя в неправильную дробь
        num2_x = num2_x if num2.find("-") == -1 else -num2_x    # Учет знака дроби
    elif num2.find("/") != -1:
        num2_x = int(num2.split("/")[0])
        num2_y = int(num2.split("/")[1])
    else:
        num2_x = int(num2)
        num2_y = 1

    # Выполнение операции с неправильными дробями
    if operation == " + ":
        res_x = num1_x * num2_y + num2_x * num1_y
    else:
        res_x = num1_x * num2_y - num2_x * num1_y
    res_y = num1_y * num2_y
    if abs(res_x) >= res_y:
        res_n = res_x // res_y if res_x >= 0 else -(abs(res_x) // res_y)
        res_x = abs(res_x) % res_y
    else:
        res_n = 0

    # Сокращаем числитель и знаменатель
    i = 2
    while i < res_x:
        if res_x % i == 0 and res_y % i == 0:
            res_x /= i
            res_y /= i
            i = 1
        i += 1

    res_x = int(res_x)
    res_y = int(res_y)
    if res_n == 0:
        if res_x != 0:
            return f"{res_x}/{res_y}"
        else:
            return "0"
    elif res_x != 0:
        return f"{res_n} {res_x}/{res_y}"
    else:
        return f"{res_n}"


s = input("Введите две дроби в формате n x/y и знак операции + или -: ")
try:
    print(f"Результат: {calculate(s)}")
except:
    print("Выражение введено некорректно.")


