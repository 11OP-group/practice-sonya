TAX = 0.13

users_annual_income = float(input("Введите ваш годовой доход: "))
tax_amount = users_annual_income * TAX
cash_on_hand = users_annual_income - tax_amount

print(f"Общая сумма дохода: {users_annual_income:,.2f} руб.".replace(",", " "))
print(f"Сумма налога: {tax_amount:,.2f} руб.".replace(",", " "))
print(f"Сумма на руки: {cash_on_hand:,.2f} руб.".replace(",", " "))