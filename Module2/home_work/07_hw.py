# Дан размер стороны квадрата. Вывести его стороны символами #.
# Формат входных данных
# На вход программе одно целое число a (2<a≤30) - сторона квадрата.
# Формат выходных данных
# Требуется вывести диагонали символами # (см. пример)

# Пример:
# Входные данные
# 6
# Выходные данные
######
#    #
#    #
#    #
#    #
######

# --------------------------------------------------------------
# Вариант 1 - Рисуем диагонали квадрата

a = int(input("Введите длину стороны квадрата от 2 до 30: "))

blank_string = "                               "  # Заготовка из 31 пробела

# Копируем во временную переменную "a" пробелов
s = blank_string[1: a + 1]

# Рисуем построчно диагонали квадрата
for i in range(1, a + 1, 1):
    s = s[:i - 1] + "#" + s[i:]  # Заменяем пробел на "#" для 1-ой диагонали
    s = s[:-i] + "#" if i == 1 else s[:-i] + "#" + s[-i + 1:]  # Заменяем пробел на "#" для 2-ой диагонали
    print(s)
    s = blank_string[1: a + 1]  # Подготавливаем шаблон строк из n пробелов для новой строки

# --------------------------------------------------------------
# Вариант 2 - Рисуем стороны квадрата дублированием символов

a = int(input("Введите длину стороны квадрата от 2 до 30: "))

print("#" * a)
for i in range(1, a - 1):
    print("#" + " " * (a - 2) + "#")
print("#" * a)

# --------------------------------------------------------------
# Вариант 3 - Рисуем стороны квадрата заменой символов

a = int(input("Введите длину стороны квадрата от 2 до 30: "))

s="##############################"
side_up_down = s[1: a+1]  # Верхняя и нижняя сторона квадрата
side_left_right = side_up_down  # Шаблон для левой и правой стороны квадрата

# Заменяем в шаблоне "#" на " " символы со 2-ой позиции до предпоследней
for i in range(1, a-1, 1):
    side_left_right = side_left_right[:i] + " " + side_left_right[i+1:]

# Рисуем стороны квадрата
print(side_up_down)
for j in range(2, a):
    print(side_left_right)
print(side_up_down)

