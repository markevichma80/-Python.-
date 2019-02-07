# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,заданный случайными числами на промежутке [-100; 100)
# Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).
import random


def puz(array):
    for x in range(1, len(array)):
        for i in range(x, len(array) + 1 - x):
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]
            if array[len(array) - i - 1] > array[len(array) - i]:
                array[len(array) - i - 1], array[len(array) - i] = array[len(array) - i], array[len(array) - i - 1]
    return array


array = [random.randint(-100, 100) for _ in range(int(input('введите количество элементов ряда : ')))]
#print(array)
print(puz(array))
