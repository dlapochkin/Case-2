a = int(input("Выберете ваше семейное положение. 1 - одинок(-а), 2 - состою в браке. 3 - родитель-одиночка."))
Question = (input("Введите ваш налоговый вычет"))

name_month = [JAN, FAB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC]

annual_income = 0
for month in range(12):
    print('{} {}:'.format(Question,name_month[month], end =''))
    income = float(input())
    annual_income += income
print(annual_income)
