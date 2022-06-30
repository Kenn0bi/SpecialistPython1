## "Обработка списка фруктов"

### Задание

Дана ведомость расчета заработной платы [data/workers.txt](data/workers.txt).

Рассчитайте зарплату всех работников, зная что они получат полный оклад, если отработают норму часов. \
Если же они отработали меньше нормы, то их ЗП уменьшается пропорционально, \
а за каждый час переработки они получают удвоенную ЗП, пропорциональную норме. \
Кол-во часов, которые были отработаны, указаны в файле ["data/hours_of.txt](data/hours_of.txt)

### Формат входных данных

Дано два текстовых файла. Один с информацией о сотрудниках, второй с количеством отработанных часов.

Гарантируется, что каждый сотрудник имеет уникальную фамилию(однофамильцев нет).

### Формат выходных данных

Выведите зарплату сотрудников с учетом переработки и недоработки.

### Решение задачи

```python
def find_emploee(lst, itm, pos=0):
    """
    Поиск индекса элемента в списке, с учетом его позиции во вложенных списках или кортежах
    :param lst: список
    :param itm: элемент
    :param pos: индекс элемента во вложенном списке
    :return: возвращает индекс элемента в списке или -1, если не найден
    """
    for i, el in enumerate(lst):
        if el[pos] == itm:
            return i
    return -1


salaries = []  # Ведомость начисленной заработной платы

# Записываем в salaries список всех сотрудников (фамилию + имя), их заработных плат и нормы рабочих часов
with open("data/workers.txt", "r", encoding="utf8") as f:
    for line in f:
        emploee = line.split()
        if emploee[2].isnumeric():
            emploee_salary = [emploee[1] + " " + emploee[0], int(emploee[2]), int(emploee[4])]
            salaries.append(emploee_salary)

# Записываем в hours_of список сотрудников (фамилию + имя) и фактически отработанное ими время
hours_of = []
with open("data/hours_of.txt", "r", encoding="utf8") as f:
    for line in f:
        emploee = line.split()
        if emploee[2].isnumeric():
            emploee_hours_of = [emploee[1] + " " + emploee[0], int(emploee[2])]
            hours_of.append(emploee_hours_of)

# Пересчитываем в salaries заработну плату в соответствии с фактически отработанными часами из hours_of.
for emploee in salaries:
    norma_hours = emploee[2]  # Норма часов
    emploee_name = emploee[0]  # Фамилия и имя сотрудника
    salary = emploee[1]  # Заработная плата
    idx = find_emploee(hours_of, emploee_name)  # Индекс записи в hours_of с временем фактической отработки сотрудника
    worked_hours = hours_of[idx][1]  # Фактически отработанное время
    if idx != -1:
        emploee[2] = worked_hours  # Заменяем норму часов на фактически отработанное время
        if worked_hours < norma_hours:
            # Если отработано меньше нормы
            emploee[1] = int(salary / norma_hours * worked_hours)
        elif worked_hours > norma_hours:
            # Если отработано больше нормы
            emploee[1] = int(salary + (salary / norma_hours) * (worked_hours - norma_hours) * 2)
    else:
        # Если сотрудника нет в списке с фактически отработанными часами
        emploee[1] = 0
        emploee[2] = 0

salaries = sorted(salaries)
s = ""
len_max_idx = len(str(len(salaries)))
for i, emploee in enumerate(salaries, 1):
    s += f"\t{i:0>{len_max_idx}}. {emploee[0]}: {emploee[1]}\n"

print(f"Ведомость начисленной заработной платы:\n{s}")

```

---
