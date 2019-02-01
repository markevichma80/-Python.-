# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# ВАРИАНТ КОТОРЫЙ СДАВАЛ
import random
import sys


def show_size(x, u):
    if hasattr(x, '__iter__'):
        if not isinstance(x, str):
            for item in x:
                show_size(item, u)
                u += sys.getsizeof(item)
    return u + sys.getsizeof(x)


x = int(input('Введите размер массива :'))
a = [0] * x
min_n = 0
max_n = 10
b = 0
c = max_n
g = 0
h = 0
sum_ = 0
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
s = locals()
for v in dir():
    if isinstance(s[v], int) or isinstance(s[v], list) or isinstance(s[v], dict):
        sum_ += show_size(s[v], 0)
        print(v, show_size(s[v], 0), type(s[v]))
print(sum_)

