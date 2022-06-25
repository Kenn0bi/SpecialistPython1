# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palindrome(number):
    return str(number) == str(number)[::-1]

a = int(input("Введите 1-ое целое положительное число: "))
b = int(input("Введите 2-ое целое положительное число: "))
if a > b:
    a, b = b, a
palindrome_nums = []

for i in range(a, b):
    if palindrome(i):
        palindrome_nums.append(i)

if len(palindrome_nums) != 0:
    print(f"Найдено {len(palindrome_nums)} палиндромов.")
else:
    print("Палиндромы не найдены.")
