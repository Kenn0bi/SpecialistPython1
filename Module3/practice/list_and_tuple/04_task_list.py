# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

import random

numbers = []
n = int(input("Введите целое положительное число: "))

for i in range(1, n + 1):
    numbers.append(random.randint(-10, 10))

print(", ".join(map(str, numbers)))
print("Сумма всех положительных элементов равна", sum(map(lambda x: 0 if x < 0 else x, numbers)))
