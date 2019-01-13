#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

x = int(input('Введите размер массива :'))
a = [0] * x
min_n = -20
max_n = 10
b = min_n
c = 0
for i in range(x):
    a[i] = random.randint(min_n, max_n)
print(a)
for x in a:
    if x < 0 and x > b:
        b = x
for z in a:
    if b != z:
        c += 1
    else:
        print(f'максимальный из отрицательных {z}, номер элемента в списке {c}')
