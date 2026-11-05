import math

x = float(input("Введите угол в градусах: "))

r = math.radians(x)

result = math.sin(r) + math.cos(r) + math.tan(r)**2

print(result)