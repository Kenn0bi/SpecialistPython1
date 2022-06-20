# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками

def can_triangle(p1, p2, p3):
    # TODO: your code here
    """
    Функция определяет площадь по координатам трех точек.
    Если площадь равна нулю, значит точки лежат на одной прямой и треугольник построить по этим точкам нельзя.
    Формула: Для точек A(x1;y1), B(x2;y2), C(x3;y3) площадь треугольника имеет вид:
    Sabc = abs((x2-x1)(y3-y1)-(x3-x1)(y2-y1)) / 2
    """
    return not abs((p2[0]-p1[0])*(p3[1]-p1[1])-(p3[0]-p1[0])*(p2[1]-p1[1])) / 2 == 0

# Пример вызова функции
print(can_triangle((10, 12), (14, 18), (12, 12)))   # Точки не располагаются на одной линии
print(can_triangle((1, 4), (3, 0), (5, -4)))    # Точки располагаются на одной линии
print(can_triangle((0, 0), (0, 0), (0, 0)))     # Три точки имеют одинаковые координаты
print(can_triangle((-1, 3), (10, 7), (10, 7)))  # Две точки имеют одинаковые координаты


# Не забудьте протестировать вашу функцию
