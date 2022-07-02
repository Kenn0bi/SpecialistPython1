# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию написанную на одном из прошлых занятий.
# Получите новый список, элементами которого будут:
#   1. неповторяющиеся(уникальные) элементы исходного списка:
#   например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
#   2. элементы исходного списка, которые не имеют повторений(встречаются только один раз):
#   например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

import random

n = int(input("Введите длину списка: "))
lst = []
for _ in range(n):
    lst.append(random.randint(0, 10))

# lst = [1, 2, 4, 5, 6, 2, 5, 2]

no_duplicates = []
for item in lst:
    if item not in no_duplicates:
        no_duplicates.append(item)

unique = []
for item in lst:
    if lst.count(item) == 1:
        unique.append(item)

print(lst)
print(no_duplicates)
print(unique)
