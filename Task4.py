# 4. Определить, какое число в массиве встречается чаще всего.
import random

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
