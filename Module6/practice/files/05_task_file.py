# Кассовый аппарат был доработан, теперь он пишет не только цены, но и тип проданных товаров.
# Файл data/items_sold.txt - продажи всех товаров за день.
# Каждая строка файла - покупка одного покупателя.
# Узнайте:
# 1. Какова общая выручка магазина
# 2. Какова выручка магазина по каждому типу товаров
# 3. Какой тип товара был продан на самую большую сумму
# 4. Сколько различных типов товаров было продано за день

def idx_list_of_lists(lst, itm, pos=0):
    """
    Поиск индекса элемента в списке, с учетом его позиции во вложенных списках или кортежах
    :param lst: список
    :param itm: элемент
    :param pos: индекс элемента во вложенном списке 
    :return: возвращает индекс элемента в списке списков или -1, если не найден
    """
    for i, el in enumerate(lst):
        if el[pos] == itm:
            return i
    return -1

items_sold = [] # Список уникальных товаров и их выручки

with open("data/items_sold.txt", encoding="utf-8") as f:
    for line in f:
        items_sold_to_buyer = list(line.strip().split())
        for item in items_sold_to_buyer:
            item_name = item.split(":")[0]
            item_revenue = item.split(":")[1]
            idx = idx_list_of_lists(items_sold, item_name) # Находим индекс товара в списке items_sold
            if idx == -1:
                items_sold.append([item_name, float(item_revenue)])
            else:
                items_sold[idx][1] += float(item_revenue)

items_sold = sorted(items_sold)

total_revenue = 0
max_revenue_item = 0
max_revenue_item_name = ""
len_max_idx = len(str(len(items_sold)))
s = ""

for i, item in enumerate(items_sold, 1):
    total_revenue += item[1]
    if max_revenue_item < item[1]:
        max_revenue_item = item[1]
        max_revenue_item_name = item[0]
    s += f"\t{i:0>{len_max_idx}}. {item[0]}: {item[1]:.2f}\n"

print(f"1. Общая выручка магазина: {total_revenue:.2f}\n")
print(f"2. Выручка магазина по каждому товару:\n{s}")
print(f"3. Максимальная выручка по товару: {max_revenue_item_name}")
print(f"4. Продано типов товаров: {len(items_sold)}.")
