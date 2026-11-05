# Задача 6. Площадь треугольника

import math


def calculate_distance(x1, y1, x2, y2):
    """Вычисляет расстояние между двумя точками."""
    distance = math.sqrt(
        (x2 - x1) ** 2 + (y2 - y1) ** 2
    )
    return distance


def calculate_triangle_area(a, b, c):
    """Вычисляет площадь треугольника по формуле Герона."""

    # проверка существования треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        return None

    # полупериметр
    p = (a + b + c) / 2

    # формула Герона
    area = math.sqrt(
        p * (p - a) * (p - b) * (p - c)
    )

    return area


# ввод координат точки A
print("Введите координаты точки A:")
x1, y1 = map(float, input().split())

# ввод координат точки B
print("Введите координаты точки B:")
x2, y2 = map(float, input().split())

# ввод координат точки C
print("Введите координаты точки C:")
x3, y3 = map(float, input().split())

# Расчет длин сторон
a = calculate_distance(x1, y1, x2, y2)
b = calculate_distance(x2, y2, x3, y3)
c = calculate_distance(x3, y3, x1, y1)

# расчет площади
area = calculate_triangle_area(a, b, c)

# вывод результата
if area is None:
    print("Ошибка! Из данных точек нельзя составить треугольник.")
else:
    print(f"Длина стороны AB: {a:.2f}")
    print(f"Длина стороны BC: {b:.2f}")
    print(f"Длина стороны CA: {c:.2f}")
    print(f"Площадь треугольника: {area:.2f}")