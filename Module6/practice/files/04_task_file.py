# Дан файл ("data/fruits.txt") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А.txt, fruits_Б.txt, fruits_В.txt ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв,
#        а также есть пустые строки, которые нужно пропустить.
# Напишите универсальный код, который будет работать с любым списком фруктов и
# распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.

# Возможно пригодится:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

# Вариант 1
"""
Однократный проход файла fruits.txt, но многократное октрытие на дозапись файлов с фруктами по буквам
"""
alphabet = list(map(chr, range(ord('А'), ord('Я')+1)))

with open("files/fruits.txt", "r", encoding="utf-8") as f_in:
    for line in f_in:
        fruit = line.strip()
        if len(fruit) != 0 and fruit.upper()[0] in alphabet:
            f_out_name = f"files/fruits_{fruit.upper()[0]}.txt"
            with open(f_out_name, "a", encoding="utf-8") as f_out:
                f_out.write(fruit + "\n")

# Вариант 2
"""
Многократный проход файла fruits.txt (кратно количеству букв в алфавите), но однократное открытие файлов на запись
"""
alphabet = list(map(chr, range(ord('А'), ord('Я')+1)))

for letter in alphabet:
    with open("files/fruits.txt", "r", encoding="utf-8") as f_in:
        fruits = []
        for line in f_in:
            fruit = line.strip()
            if len(fruit) != 0 and fruit.upper()[0] == letter:
                fruits.append(fruit)
        if len(fruits) !=0:
            f_out_name = f"files/fruits_{letter}.txt"
            with open(f_out_name, "w", encoding="utf-8") as f_out:
                for fruit in fruits:
                    f_out.write(fruit + "\n")
