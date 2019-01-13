#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

x = int(input('Введите размер массива :'))
a = [0] * x
min_n = 0
max_n = 10
b = 0
c = max_n
g = 0
h = 0
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
a[g], a[h] = a[h], a[g]
print(a)
