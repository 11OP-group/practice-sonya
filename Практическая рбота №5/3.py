EXCHANGE_RATE = 83.56

def usd_to_rub(usd):
    """Конвертирует доллары в рубли."""
    return usd * EXCHANGE_RATE

usd = float(input("Введите сумму в долларах: "))
rub = usd_to_rub(usd)

print(f"{usd:.2f} $ = {rub:.2f} ₽")