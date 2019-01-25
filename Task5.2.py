from collections import deque
import time


def ten(a, letters):
    """Переводим число из 16-ричной системы в 10-чную"""
    x = 0
    y = 0
    for index, value in enumerate(a):
        if value.isdigit():
            y = int(value)
        else:
            value.lower()
            for ind, val in enumerate(letters):
                if value == val:
                    y = letters[ind + 1]
        x += y * 16 ** (len(a) - index - 1)
    return (x)


def sixteen(z, letters):
    """Переводим 10-чную систему исчисления в 16-тичную"""
    x = deque()
    while z > 0:
        q = z % 16
        if q > 9:
            for i, valu in enumerate(letters):
                if q == valu:
                    y = letters[i - 1]
        else:
            y = q
        x.appendleft(y)
        z = z // 16
    return x


letters = deque(['a', 10, 'b', 11, 'c', 12, 'd', 13, 'e', 14, 'f', 15])
a = deque(input('Введите шестнадцатиричное число '))
b = deque(input('Введите второе шестнадцатиричное число'))
a_des = ten(a, letters)
b_des = ten(b, letters)
summ = a_des + b_des
mult = a_des * b_des
print(sixteen(summ, letters), sixteen(mult, letters), sep='\n')
