# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
import random

m = int(input('ведите натуральное число m : '))
array = [random.randint(0, 49) for _ in range((2 * m) + 1)]
print(array)
for numb in array:
    numb_more, numb_equally = 0, 0
    for arr in array:
        if numb > arr:
            numb_more += 1
        elif numb == arr:
            numb_equally += 1
    if numb_more == m + 1:
        print(f'медиана массива : {numb}')
        break
    elif numb_more < m + 1 and numb_equally + numb_more >= m + 1:
        print(f'медиана равна {numb}')
        break
