
кофе = 120
чай = 80
сок = 100
вода = 50
лимонад = 90

print("===== МЕНЮ КАФЕ ☕ =====")
print("1. кофе - 120 руб.")
print("2. чай - 80 руб.")
print("3. сок - 100 руб.")
print("4. вода - 50 руб.")
print("5. лимонад - 90 руб.")

# Выбор напитка
drink = input("выберите напиток (1-5): ")

match drink:  # проверяет, какой напиток выбрал пользователь
    case "1":
        name = "кофе ☕"
        price = кофе
    case "2":
        name = "чай 🍵"
        price = чай
    case "3":
        name = "сок 🧃"
        price =сок
    case "4":
        name = "вода 💧"
        price = вода
    case "5":
        name = "лимонад 🥤"
        price =лимонад
    case _:
        name = ""
        price = 0

if price == 0:
    print("ошибка! такого напитка нет.")
else:
    # количество порций
    try:
        count = int(input("введите количество порций: "))

        match count:
            case n if n > 0:
                total = price * count  # умножаем цену на количество порций

                # скидка
                discount_code = input("введите код скидки (или Enter): ")

                match discount_code.upper():
                    case "STUDENT":
                        discount = total * 0.20
                    case _:
                        discount = 0

                final_price = total - discount  # рассчитывает окончательную стоимость

                match count % 10:  # помогает правильно написать слово «порция»
                    case 1 if count % 100 != 11:
                        portion = "порция"
                    case 2 | 3 | 4 if count % 100 not in (12, 13, 14):
                        portion = "порции"
                    case _:
                        portion = "порций"

                print("\n===== КВИТАНЦИЯ КАФЕ ☕ =====")
                print(f"напиток: {name}")
                print(f"цена за порцию: {price} руб.")
                print(f"количество: {count} {portion}")
                print(f"сумма: {total} руб.")
                print(f"скидка: {discount} руб.")
                print(f"К ОПЛАТЕ: {final_price} руб.")
                print("============================")

            case _:
                print("ошибка! количество должно быть больше нуля.")

    except ValueError:
        print("ошибка! введите количество целым числом.")
