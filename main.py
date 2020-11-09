# Case-study #2
# Developers:   Lapochkin D. (0%),
#               Kuznetsov A. (25%),
#               Krivoshapova D. (30%)

br = input('''Из предложенных ниже вариантов выберете соответствующий Вашему семейному положению:
одинок(-а): 1
состою в браке: 2
родитель-одиночка: 3
''')
name_month = ['январе', 'феврале', 'марте', 'апреле', 'мае', 'июне', 'июле', 'августе', 'сентябре', 'октябре', 'ноябре',
              'декабре']
QUESTION = 'Введите ваш доход в'
annual_income = 0
for month in range(12):
    print('{} {}:'.format(QUESTION, name_month[month], end=''))
    income = float(input())
    annual_income += income
r = int(input("Введите ваш налоговый вычет "))
t = annual_income - r  # taxable income

if br == '1':
    numbers = [9075, 36900, 89350, 186350, 405100, 406750]
    a, b, c, d, e, f = list(map(int, numbers))
if br == '2':
    numbers = [18150, 73800, 148850, 226850, 405100, 457600]
    a, b, c, d, e, f = list(map(int, numbers))
if br == '3':
    numbers = [12950, 49400, 127550, 206600, 405100, 432200]
    a, b, c, d, e, f = list(map(int, numbers))
if 0 < t <= a:
    n = t * 0.1
if a < t <= b:
    n = a * 0.1 + (t - a) * 0.15
if b < t <= c:
    n = a * 0.1 + (b - a) * 0.15 + (t - b) * 0.25
if c < t <= d:
    n = a * 0.1 + (b - a) * 0.15 + (c - b) * 0.25 + (t - c) * 0.28
if d < t <= e:
    n = 0.1 * a + 0.15 * (b - a) + 0.25 * (c - b) + 0.28 * (d - c) + 0.33 * (t - d)
if e < t <= f:
    n = 0.1 * a + 0.15 * (b - a) + 0.25 * (c - b) + 0.28 * (d - c) + 0.33 * (e - d) + 0.35 * (t - e)
if t >= f:
    n = 0.1 * a + 0.15 * (b - a) + 0.25 * (c - b) + 0.28 * (d - c) + 0.33 * (e - d) + 0.35 * (f - e) + 0.396 * (t - f)
print('Cумма налога составит:', n)