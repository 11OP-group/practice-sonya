n = int(input("Введите четырёхзначное число: "))

thousands = n // 1000
hundreds = n // 100 % 10
tens = n // 10 % 10
units = n % 10

print("Цифра в позиции тысяч равна", thousands)
print("Цифра в позиции сотен равна", hundreds)
print("Цифра в позиции десятков равна", tens)
print("Цифра в позиции единиц равна", units)