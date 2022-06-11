# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

split_text = text.split(" ")
count = 0

for word in split_text:
    if len(word) > 5:
        count += 1

print("Слов из более 5 букв: ", count)
