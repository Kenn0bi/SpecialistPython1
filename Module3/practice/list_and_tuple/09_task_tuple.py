# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

# TODO: your code here
import random

n = int(input("Задайте длину кортежей: "))

tup1 = ()
tup2 = ()
tup3 = ()

# Заполняем кортежи случайными числами в диапазоне от -10 до 10.
for i in range(n):
    tup1 += random.randint(-10, 10),
for i in range(n):
    tup2 += random.randint(-10, 10),
for i in range(n):
    tup3 += random.randint(-10, 10),

# Подсчитываем количество чисел, которые встречаются во всех трех кортежах. 
count = 0
for num in tup1:
    if num in tup2 and num in tup3:
        count += 1
        
print(tup1, "\n", tup2, "\n", tup3)
print("Количество элементов, которые встречаются во всех трех кортежах:", count)
