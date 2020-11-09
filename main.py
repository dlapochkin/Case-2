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
if br == 2:
    numbers = [18150, 73800, 148850, 226850, 405100, 457600]
    a, b, c, d, e, f = list(map(int, numbers))
if br == 3:
    numbers = [12950, 49400, 127550, 206600, 405100, 432200]
    a, b, c, d, e, f = list(map(int, numbers))

    if 0 < t <= a:
        print(t * 0.1)
    if a < t <= b:
        print(a * 0.1 + (t - a) * 0.15)
    if b < t <= c:
        print(a * 0.1 + (t - a) * 0.15 + (t - a - b) * 0, 25)
    if a < t <= b:
        print(a * 0.1 + (t - a) * 0.15 + (t - a - b) * 0, 25) + (t - a - b - d) * 0.28))