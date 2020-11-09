br = int(input("Выберете ваше семейное положение. 1 - одинок(-а), 2 - состою в браке. 3 - родитель-одиночка."))
name_month = ['JAN', 'FAB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
QUESTION = 'сколько вы заработали в'
annual_income = 0
for month in range(12):
    print('{} {}:'.format(QUESTION, name_month[month], end=''))
    income = float(input())
    annual_income += income
c = int(input("Введите ваш налоговый вычет"))
t = annual_income - c  # taxable income

if br == 1:
    numbers = [9075, 36900, 89350, 186350, 405100, 406750]
    a, b, c, d, e, f = list(map(int, numbers))