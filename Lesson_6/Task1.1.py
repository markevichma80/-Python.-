# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# Новое написание
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
a = [0] * int(input('Введите размер массива : '))
x = float('inf')
y = float('-inf')
for index, value in enumerate(a):
    a[index] = random.randint(min_, max_)
    if a[index] < x:
        x = a[index]
        b = index
    elif a[index] > y:
        y = a[index]
        d = index
print(a)
print(f' min : {x}, max :{y}')
a[b], a[d] = a[d], a[b]
print(a)
m = locals()
for n in dir():
    if isinstance(m[n], int) or isinstance(m[n], list) or isinstance(m[n], dict):
        sum_ += show_size(m[n], 0)
        print(n, show_size(m[n], 0), sys.getsizeof(m[n]), type(m[n]))
print(sum_)
