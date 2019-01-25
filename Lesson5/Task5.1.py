from collections import namedtuple
import time

a = int(input('Введите количество предприятий '))
Total = namedtuple('Total', 'Names, first, second, third fourth total ')
p = []
less = []
more = []
Total_all = 0
for i in range(a):
    x = input('Введите название предприятия ')
    first_quarter = int(input('Выручка за первый квартал :'))
    second_quarter = int(input('Выручка за второй квартал :'))
    third_quarter = int(input('Выручка за третий квартал :'))
    fourth_quarter = int(input('Выручка за четвёртый квартал :'))
    i = Total(Names=x, first=first_quarter, second=second_quarter, third=third_quarter, fourth=fourth_quarter, total=0)
    i = i._replace(total=i[1] + i[2] + i[3] + i[4])
    # ввожу для проверки на ноль, в получении среднего количество не должно учитывать число предприятий с нулевой выручкой(что быть вполне может)
    if i.total == 0:
        a -= 1
    else:
        Total_all += i.total
    p.append(i)
for ind, val in enumerate(p):
    if val.total < Total_all / a:
        less.append(val.Names)
    elif val.total > Total_all / a:
        more.append(val.Names)
print(f'Предприятия с годовой выручкой меньше среднего: {less}, больше среднего: {more}')
