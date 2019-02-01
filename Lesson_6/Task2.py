# 4. Определить, какое число в массиве встречается чаще всего.
#Новый вид
import random
import sys


def show_size(x, u):
    if hasattr(x, '__iter__'):
        if not isinstance(x, str):
            for item in x:
                show_size(item, u)
                u += sys.getsizeof(item)
    return u + sys.getsizeof(x)


min_ = 0
max_ = 30
sum_ = 0
count = 0
max_count = 0
a = []
for i in range(int(input('Введите размер массива : '))):
    a.append(random.randint(min_, max_))
    b = 0
    for index, value in enumerate(a):
        if a[index] == a[i]:
            b += 1
    if b > count:
        count = b
        max_count = a[i]
print(f'Массив : {a}, наиболее встречаемое число : {max_count}, число повторений {c}')
s = locals()
for v in dir():
    if isinstance(s[v], int) or isinstance(s[v], list) or isinstance(s[v], dict):
        sum_ += show_size(s[v], 0)
        print(v, show_size(s[v], 0), type(s[v]))
print(sum_)
#вариант который сдавал
x = int(input('Введите размер массива :'))
a = [0] * x
b = {}
k = 0
c = 0
for i in range(x):
    a[i] = random.randint(0, 20)
for n in a:
    if n in b:
        b[n] += 1
    else:
        b[n] = 1
for value in b.values():
    if c < value:
        c = value
print(b)
for key, v in b.items():
    if v == c:
        print(key, c)
        break