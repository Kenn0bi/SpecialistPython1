# Данные о сотрудниках в программе хранятся в словаре
staff = [
    {
        'name': 'Алексей',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Павлов',
        'salary': 47800
    },
]
# Вычислите:

i = 0
max_salary = 0
max_salary_person = ""
min_salary = 1e10
min_salary_person = ""
total_salary = 0

for person in staff:
    if max_salary < staff[i]["salary"]:
        max_salary = staff[i]["salary"]
        max_salary_person = staff[i]["name"] + " " + staff[i]["surname"]
    if min_salary > staff[i]["salary"]:
        min_salary = staff[i]["salary"]
        min_salary_person = staff[i]["name"] + " " + staff[i]["surname"]
    total_salary += staff[i]["salary"]
    i += 1
print("Имя и Фамилия сотрудника с самой высокой зарплатой:", max_salary_person)

# TODO: your code here

print("Имя и Фамилия сотрудника с самой низкой зарплатой:", min_salary_person)

# TODO: your code here

print("Среднеарифметическая зарплата всех сотрудников:", total_salary / len(staff))

# TODO: your code here

count = 0

for i in range(len(staff)):
    for j in range(len(staff)):
        if staff[i]["surname"] == staff[j]["surname"] and i != j:
            count += 1

print("Количество однофамильцев в организации", count)

# TODO: your code here

print("*Список всех сотрудников(Имя и Фамилия) в порядке возрастания их зарплаты:")

persons_sorted_by_salary = sorted(staff, key=lambda k: k['salary'])
i = 0

for person in persons_sorted_by_salary:
    print(str(i + 1) + ".", persons_sorted_by_salary[i]["name"], persons_sorted_by_salary[i]["surname"])
    i += 1
# TODO: your code here
