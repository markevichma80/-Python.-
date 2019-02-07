#2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
#Выведите на экран исходный и отсортированный массивы.
import random
array=[random.random()*50 for _ in range(int(input('введите размер массива : ')))]
def divish(array):
    if len(array)<2:
        return array
    else:
        mas1=divish(array[:len(array)//2])
        mas2=divish(array[len(array)//2:])
    return merge(mas1, mas2)
#print(chto_to(array))
def merge(mas1,mas2):
    result=[]
    i,j=0,0
    while i<len(mas1) and j<len(mas2):
        if mas1[i]<=mas2[j]:
            result.append(mas1[i])
            i+=1
        else:
            result.append(mas2[j])
            j+=1
    else:
        result+=mas1[i:]
        result+=mas2[j:]
    return result
print(array)
print(divish(array))