# Задача 5. Банкомат

# купюры
BANKNOTE_5000 = 5000
BANKNOTE_2000 = 2000
BANKNOTE_1000 = 1000
BANKNOTE_500 = 500
BANKNOTE_200 = 200
BANKNOTE_100 = 100

# вводим сумму которую хотим снять
summa = int(input("Введите сумму для снятия: "))

remaining = summa
print(f"Выдача суммы {summa} руб :")

count_5000 = remaining // BANKNOTE_5000
remaining = remaining % BANKNOTE_5000
print(f"Купюр по 5000: {count_5000}")

count_2000 = remaining // BANKNOTE_2000
remaining = remaining % BANKNOTE_2000
print(f"Купюр по 2000: {count_2000}")

count_1000 = remaining // BANKNOTE_1000
remaining = remaining % BANKNOTE_1000
print(f"Купюр по 1000: {count_1000}")

count_500 = remaining // BANKNOTE_500
remaining = remaining % BANKNOTE_500
print(f"Купюр по 500: {count_500}")

count_200 = remaining // BANKNOTE_200
remaining = remaining % BANKNOTE_200
print(f"Купюр по 200: {count_200}")

count_100 = remaining // BANKNOTE_100
remaining = remaining % BANKNOTE_100
print(f"Купюр по 100: {count_100}")

print(f"Остаток, который банкомат не смог вам выдать: {remaining} руб.")