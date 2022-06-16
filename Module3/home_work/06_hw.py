# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
# Найдите:
brands = []
i = 0

# Создаем новый список с уникальными названиями брендов, подсчитываем количество товара и находим самую высокую цену для каждого брэнда
for i in range(len(items)):
    recorded_brand = False
    for j in range(len(brands)):
        if items[i]["brand"] in brands[j]:
            recorded_brand = True
            break
    if not recorded_brand:
        brands.append([items[i]["brand"], 0, 0])
        most_cost = 0
        for k in range(len(items)):
            if items[k]["brand"] == brands[len(brands) - 1][0]:
                brands[len(brands) - 1][2] += 1
                if most_cost < items[k]["price"]:
                    most_cost = items[k]["price"]
                    brands[len(brands) - 1][1] = items[k]["price"]

# Выводим на экран брэнды в алфавитном порядке
brands_tmp = []
for i in range(len(brands)):
    brands_tmp.append(brands[i][0])
brands_tmp = sorted(brands_tmp)

print("Товары на складе представлены брэндами: ", ", ".join(brands_tmp))

# Находим у каких брендов больше всего товаров
most_count = 0
most_count_brand = []

for i in range(len(brands)):
    if most_count <= brands[i][2]:
        most_count = brands[i][2]
for i in range(len(brands)):
    if most_count == brands[i][2]:
        most_count_brand.append(brands[i][0])

most_count_brand = sorted(most_count_brand)

print("На складе больше всего товаров брэнда(ов): ", ", ".join(most_count_brand))

# Находим у каких брендов самая высокая цена
most_cost = 0
most_cost_brand = []

for i in range(len(brands)):
    if most_cost <= brands[i][1]:
        most_cost = brands[i][1]
for i in range(len(brands)):
    if most_cost == brands[i][1]:
        most_cost_brand.append(brands[i][0])

most_cost_brand = sorted(most_cost_brand)

print("На складе самый дорогой товар брэнда(ов): ", ", ".join(most_cost_brand))
