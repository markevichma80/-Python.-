print('Введите три числа')
x = int(input('x='))
y = int(input('y='))
z = int(input('z='))
if x > y:
    if x < z:
        print(f'x={x} среднее число')
    else:
        print(f'y={y} среднее число')
elif y < z:
    print(f'y={y} среднее число')
elif z > x:
    print(f'z={z} среднее число')
else:
    print(f'x={x} среднее число')
