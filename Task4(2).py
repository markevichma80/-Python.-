#4. Определить, какое число в массиве встречается чаще всего.
import random

k = 0
x = int(input('Введите размер массива :'))
a = [0] * x
min_n = 0
max_n = 10
s = 0
m = []
for i in range(x):
    a[i] = random.randint(min_n, max_n)
print(a)
for n in a:
    c = 0
    for y in a:
        if n == y:
            c += 1
    if [n, c] not in m:
        m.append([n, c])
for z in m:
    if z[1] > k:
        k = z[1]
        s = z
print(s[0])
