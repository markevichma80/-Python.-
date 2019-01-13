#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
#Сами минимальный и максимальный элементы в сумму не включать.
import random

x = int(input('Введите размер массива :'))
a = [0] * x
min_n = 0
max_n = 10
b = 0
c = max_n
g = 0
h = 0
sum_mas = 0
for i in range(x):
    a[i] = random.randint(min_n, max_n)
print(a)
for x in a:
    if x > b:
        b = x
for y in a:
    if y < c:
        c = y
for z in a:
    if b != z:
        g += 1
    else:
        break
for w in a:
    if c != w:
        h += 1
    else:
        break
if g < h:
    for i in range(g + 1, h):
        sum_mas += a[i]
else:
    for i in range(h + 1, g):
        sum_mas += a[i]
print(g, h)
print(sum_mas)
