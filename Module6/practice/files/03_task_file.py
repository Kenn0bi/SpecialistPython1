# В файлк salaries.txt даны зарплаты сотрудников

# Задача: выведите всех сотрудников в файл highly_paid.txt, зарплаты которых превышают 60000
# Сотружников вывести в формате: Фамилия И.О. ,например: Иванов И.П. (зарплаты в файл не записывать)
emploee = []

with open("files/salaries.txt", "r", encoding="utf8") as f_in:
    for line in f_in:
        staff = line.split()
        if staff[3].isnumeric():
            emploee.append(staff)

with open("files/highly_paid.txt", "w", encoding="utf8") as f_out:
    for staff in emploee:
        if int(staff[3]) > 60000:
            s = f"{staff[0]} {staff[1][0]}.{staff[2][0]}.\n"
            f_out.write(s)
