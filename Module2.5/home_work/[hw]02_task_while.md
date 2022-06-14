## "Кратные пяти из диапазона"

### Задание

Даны два целые числа a и b.

Выведите на экран все целые **кратные 5** от a до b включительно.

### Формат входных данных

Даны два целые числа. **Не гарантируется**, что a < b. \
Если a > b, то выводим все числа из диапазона [b, a].

### Формат выходных данных

Выведите все числа, требуемые по условию задачи.

### Решение задачи

```python
a = int(input("a: "))
b = int(input("b: "))

numbers_divided_5 = []
a_less_b = True
if a > b:
    a, b = b, a
    a_less_b = False

while a <= b:
    if a % 5 == 0:
        numbers_divided_5.append(a)
    a += 1

if a_less_b:
    print(numbers_divided_5)
else:
    print(numbers_divided_5[::-1])
```
