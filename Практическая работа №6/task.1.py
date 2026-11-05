# Задача 1. Диагностика состояния здоровья

# ввод показателей
temperature = float(input("Введите температуру тела: "))
pressure = int(input("Введите верхнее давление: "))
pulse = int(input("Введите пульс: "))

# проверка значительного отклонения
if (temperature < 35 or temperature > 38
        or pressure < 105 or pressure > 140
        or pulse < 55 or pulse > 110):

    print("Требуется врач")

# проверка нормального состояния
elif (36 <= temperature <= 37
      and 110 <= pressure <= 130
      and 60 <= pulse <= 100):

    print("Нормальное состояние")

# проверка легкого недомогания
else:
    print("Легкое недомогание")