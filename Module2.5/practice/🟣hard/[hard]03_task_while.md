## "Дружественные числа"

### Задание

Два натуральных числа называются дружественными, если каждое из них равно сумме всех натуральных делителей другого
(само число при этом не рассматривается в качестве собственного делителя). \
Необходимо найти все пары натуральных дружественных чисел (не равных друг другу), до введенного числа.

### Формат входных данных

Дано одно целое положительное число

### Формат выходных данных

Вывести все пары дружественных чисел, удовлетворяющие условию задачи.

### Решение задачи

```python
n = int(input("Введите целое положительное число: "))

digit_1 = 1
digit_2 = 1
simple_digit_1 = False  # Признак того, что 1-ое число простое
found_digits = []

while digit_1 <= n:
    j = 1
    total_sum_1 = 0
    while j < digit_1:
        if digit_1 % j == 0:
            total_sum_1 += j
        elif total_sum_1 == 0 and j > digit_1 // 2 + 1:  # Прерываем цикл, так как 1-ое число простое
            simple_digit_1 = True
            break
        j += 1
    if not simple_digit_1:
        digit_2 = total_sum_1
        total_sum_2 = 0
        j = 1
        while j < digit_2:
            if digit_2 % j == 0:
                total_sum_2 += j
            elif total_sum_2 == 0 and j > digit_2 // 2 + 1:  # Прерываем цикл, так как 2-ое число простое
                break
            j += 1
    if digit_1 == total_sum_2 and digit_2 == total_sum_1 and digit_1 != digit_2 and digit_1 not in found_digits and digit_2 not in found_digits:
        print(digit_1, digit_2)
        found_digits.append(digit_1)
        found_digits.append(digit_2)
    digit_1 += 1
    simple_digit_1 = False
    simple_digit_2 = False

if found_digits == []:
    print("Дружественные числа не найдены.")
```

---

### Данные для самопроверки

| Дано | Результат |
| :---: | --- |
|  300  | 220 284 |
