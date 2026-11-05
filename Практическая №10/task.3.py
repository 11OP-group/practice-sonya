maxium = 0

while True:
    number = int(input("Введите число (0 - выход):"))
    if number == 0:
        break
    if number > maxium:
        maxium = number
    print("Наибольшее число, maxium")