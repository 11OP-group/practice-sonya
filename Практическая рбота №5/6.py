def calculate_distance(x1, y1, x2, y2):
    """
    Считает расстояние между двумя точками на плоскости
    и возвращает длину отрезка между точками
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def calculate_triangle_area(a, b, c):
    """
    Считает площадь треугольника по формуле Герона
    и возвращает площадь треугольника
    """
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

x1, y1 = map(float, input("Введите координаты точки A: ").split())
x2, y2 = map(float, input("Введите координаты точки B: ").split())
x3, y3 = map(float, input("Введите координаты точки C: ").split())

side_a = calculate_distance(x1, y1, x2, y2)
side_b = calculate_distance(x2, y2, x3, y3)
side_c = calculate_distance(x3, y3, x1, y1)

triangle_area = calculate_triangle_area(side_a, side_b, side_c)

print(f"Площадь треугольника равна {triangle_area:.2f}")