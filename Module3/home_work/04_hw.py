# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]

# import random
#
# n = int(input("Введите целое положительное число: "))
# numbers = []
#
# for i in range(1, n + 1):
#     numbers.append(random.randint(-100, 100))

numbers = [2, -5, 8, 9, -25, 25, 4]
n = 7

print(*numbers, sep=", ")
new_numbers = []

for i in range(0, n):
    try:
        if numbers[i] !=0 and (numbers[i] ** 0.5) % 1 == 0:
            new_numbers.append(int(numbers[i] ** 0.5))
    except:
        pass

if new_numbers != []:
    print(*new_numbers, sep=", ")
else:
    print("Числа удовлетворяющие условию не найдены.")
