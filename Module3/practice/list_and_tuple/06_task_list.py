# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

first_number = int(input("Введите первое число: "))     # Первое число
second_number = int(input("Введите второе число: "))    # Второе число

reverse_list = False
if first_number > second_number:
    reverse_list = True
    first_number, second_number = second_number, first_number

num_divided_3 = []
for i in range(first_number, second_number+1):
    if i % 3 == 0:
        num_divided_3.append(i)

if reverse_list:
    num_divided_3 = num_divided_3[::-1]

print(*num_divided_3, sep=", ")
