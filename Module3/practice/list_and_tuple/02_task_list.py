# Дан список. Вывести элементы списка, пронумеровав их начиная с единицы.
# Каждый элемент должен быть выведен с новой строки.

fruits = ["яблоко", "банан", "киви", "ананас", "груша"]

# TODO: your code here
i = 1
for fruit in fruits:
    s = f"{i}. {fruit}"
    print(s)
    i += 1
